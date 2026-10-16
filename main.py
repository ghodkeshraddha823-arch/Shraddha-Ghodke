
import pandas as pd
import matplotlib.pyplot as plt

print("pandas imported successfuly !")
print("Matplotlib imported successfully !")

# 1. Read CSV file
df = pd.read_csv("sales_data.csv")
print(df.columns.tolist())

# 2. Convert Date into date format
df["Date"] = pd.to_datetime(df["Date"])

# 3. Calculate Revenue
df["Revenue"] = df["Quantity"] * df["Unit_Price"]

# 4. Display data
print("\n===== SALES DATA =====")
print(df.to_string(index=False))

# 5. Sales Summary
total_records = len(df)
total_units = df["Quantity"].sum()
total_revenue = df["Revenue"].sum()

print("\n===== SALES SUMMARY =====")
print("Total Records:", total_records)
print("Total Units Sold:", total_units)
print("Total Revenue: Rs.", total_revenue)

# 6. Revenue by Product
product_sales = df.groupby("Product")["Revenue"].sum()
product_sales = product_sales.sort_values(ascending=False)

print("\n===== PRODUCT SALES =====")
print(product_sales)

# 7. Revenue by Region
region_sales = df.groupby("Region")["Revenue"].sum()

print("\n===== REGION SALES =====")
print(region_sales)

# 8. Monthly Revenue
monthly_sales = df.groupby(
    df["Date"].dt.to_period("M")
)["Revenue"].sum()

print("\n===== MONTHLY SALES =====")
print(monthly_sales)

# 9. Product Sales Chart
plt.figure(figsize=(9, 5))
product_sales.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("revenue_by_product.png")
plt.show()

# 10. Region Sales Chart
plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()
plt.savefig("revenue_by_region.png")
plt.show()

# 11. Monthly Sales Chart
monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(8, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_revenue_trend.png")
plt.show()

# 12. Save Report
df.to_csv("sales_report.csv", index=False)

print("\nReport saved successfully!")





# ===== SALES GRAPHS =====

# Graph 1: Product Wise Sales
product_sales = df.groupby("Product")["Revenue"].sum()
product_sales = product_sales.sort_values(ascending=False)

plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")

plt.title("Product Wise Sales")
plt.xlabel("Product Name")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("product_sales.png")


# Graph 2: Region Wise Sales
region_sales = df.groupby("Region")["Revenue"].sum()

plt.figure(figsize=(7, 7))
region_sales.plot(kind="pie", autopct="%1.1f%%")

plt.title("Region Wise Sales")
plt.ylabel("")
plt.tight_layout()
plt.savefig("region_sales.png")


# Graph 3: Monthly Sales
monthly_sales = df.groupby(
    df["Date"].dt.to_period("M")
)["Revenue"].sum()

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(8, 5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales.png")

# Show all graphs
plt.show()

print("All graphs created successfully!")
