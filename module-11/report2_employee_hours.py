import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Riley",
    database="Bacchus_Winery"
)
cursor = conn.cursor()

print("\n=== Report 2: Employee Hours by Department ===")
cursor.execute("""
    SELECT d.Department_Name, e.Employee_Name, e.Total_Hours
    FROM Employee e
    JOIN Department d ON e.Department_ID = d.Department_ID
    ORDER BY d.Department_Name
""")
for row in cursor.fetchall():
    print(f"Department: {row[0]}, Employee: {row[1]}, Hours: {row[2]}")

cursor.close()
conn.close()
