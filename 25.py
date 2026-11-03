import matplotlib.pyplot as plt

# Data from the provided table
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [45000, 52000, 48000, 61000, 58000, 65000, 62000, 70000, 68000, 75000, 72000, 80000]

# Identify highest and lowest sales
max_sales = max(sales)
min_sales = min(sales)
max_month = months[sales.index(max_sales)]
min_month = months[sales.index(min_sales)]

print(f"Highest Sales: {max_month} (₹{max_sales})")
print(f"Lowest Sales: {min_month} (₹{min_sales})")

# Create a figure with 2 subplots (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Line Chart
ax1.plot(months, sales, marker='o', color='b', linestyle='-')
ax1.set_title('Monthly Sales Revenue (Line Chart)')
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales (₹)')
ax1.grid(True, linestyle='--', alpha=0.7)

# Plot 2: Bar Chart
ax2.bar(months, sales, color='skyblue', edgecolor='black')
ax2.set_title('Monthly Sales Revenue (Bar Chart)')
ax2.set_xlabel('Month')
ax2.set_ylabel('Sales (₹)')

# Highlight the max and min bars
ax2.get_children()[sales.index(max_sales)].set_color('green')
ax2.get_children()[sales.index(min_sales)].set_color('red')

plt.tight_layout()
plt.show()
