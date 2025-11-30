# quick_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

merged = pd.read_excel('data/MERGED_BY_TRANSACTION_ID.xlsx')
merged['Date_y'] = pd.to_datetime(merged['Date_y'])
merged['Month'] = merged['Date_y'].dt.to_period('M').astype(str)

# Monthly sales by category
monthly = merged.groupby(['Month','Product Category'])['Sales_Amount'].sum().reset_index()
pivot = monthly.pivot(index='Month', columns='Product Category', values='Sales_Amount')

# Plot and save
ax = pivot.plot(figsize=(10,5), title='Monthly Sales Amount by Product Category')
ax.set_xlabel('Month'); ax.set_ylabel('Sales Amount')
plt.tight_layout()
plt.savefig('charts/monthly_sales_by_category.png')
plt.close()

# Total revenue by category
tot = merged.groupby('Product Category')['Sales_Amount'].sum()
ax = tot.plot(kind='bar', figsize=(6,4), title='Total Revenue by Product Category')
ax.set_xlabel('Category'); ax.set_ylabel('Total Revenue')
plt.tight_layout()
plt.savefig('charts/total_revenue_by_category.png')
