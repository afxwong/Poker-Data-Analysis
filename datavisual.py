from matplotlib import pyplot as plt
from matplotlib import axes, axis
import seaborn as sns
import pandas as pd
import csv

'''
file = open('Hand_Percentages', 'r')
lines = file.readlines()
#line = lines[0]
#print(line[0:12], line[14:])
hand = []
per = []
for line in lines:
    hand.append(line[0:12])
    per.append(line[14:])

plt.bar(range(len(hand)), per)
plt.show()
'''
'''
with open('test2.csv', 'w') as f:
    f_write = csv.writer(f)
    f_write.writerow(['Hand', 'Percentage'])
'''

with open('test2.csv', 'w') as f:
    f_write = csv.writer(f)
    f_write.writerow(['Hand', 'Percentage'])
    file = open('Hand_Percentages', 'r')
    lines = file.readlines()
    count = 0
    for line in lines:
        hand = line[0:12]
        per = float(line[14:])
        if per > 63.0:
            f_write.writerow([hand, float(per)])


df = pd.read_csv('test2.csv')
sns.set(rc={'figure.figsize':(100.7, 8.27)})
sns.barplot(data=df, x='Hand', y='Percentage')
ax = sns.countplot(x='Hand', data=df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha='right', fontsize=7)
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2, height + 1, '{:1.2f}'.format(height), ha='center', fontsize=7)
plt.tight_layout()
plt.show()

