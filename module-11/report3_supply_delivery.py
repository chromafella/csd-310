import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Riley",
    database="Bacchus_Winery"
)
cursor = conn.cursor()

print("\n=== Report 3: Supply Orders and Delivery Timeliness ===")
cursor.execute("""
    SELECT s.Supply_Type, sup.Supplier_Name, s.Order_Date, 
           s.Expected_Delivery, s.Actual_Delivery
    FROM Supply s
    JOIN Supplier sup ON s.Supplier_ID = sup.Supplier_ID
""")
for row in cursor.fetchall():
    print(f"Supply: {row[0]}, Supplier: {row[1]}, Ordered: {row[2]}, Expected: {row[3]}, Delivered: {row[4]}")

cursor.close()
conn.close()
