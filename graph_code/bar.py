import pandas as pd
import matplotlib.pyplot as plt

bar_df = pd.read_csv('csv/bar_assignment.csv') 

bar_df['COUNT'] = bar_df['COUNT'].map({1: 'Yes', 0: 'No'})
bar_pivot = bar_df.pivot_table(index='LABEL', columns='COUNT', aggfunc='size', fill_value=0)

plt.figure(figsize=(10, 6))
bar_pivot.plot(kind='barh', stacked=True, colormap='coolwarm')
plt.xlabel('Count')
plt.ylabel('Label')
plt.title('Horizontal Stacked Bar Chart')
plt.legend(title='Response')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.savefig('images/bar.png', dpi=300, bbox_inches='tight')  

plt.show()
