import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
data = {'Month': ['07/2019', '08/2019', '09/2019', '10/2019', '11/2019'],
        'Searches': [50, 53, 59, 56, 62],
        'Direct': [39, 47, 42, 51, 51],
        'Social Media': [70, 80, 83, 87, 92]}

# Create a DataFrame
df = pd.DataFrame(data)

#creating the bar chart
width = 0.2# the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(df['Month'], df['Searches'], width, label='Searches')
rects2 = ax.bar(np.array(range(len(df['Month']))) + width, df['Direct'], width, label='Direct')
rects3 = ax.bar(np.array(range(len(df['Month']))) + 2 * width, df['Social Media'], width, label='Social Media')

ax.set_ylabel('Visitors in thousands')
ax.set_title('Visitors by web traffic sources')
ax.set_xticks(np.array(range(len(df['Month']))) + width)
ax.set_xticklabels(df['Month'])
ax.legend()

fig.tight_layout()
plt.show()