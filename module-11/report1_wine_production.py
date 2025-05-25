import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Riley",
    database="Bacchus_Winery"
)
cursor = conn.cursor()

print("\n=== Report 1: Wine Production vs Distribution ===")
cursor.execute("""
    SELECT Wine_Name, Total_Produced, Total_Distributed, 
           (Total_Produced - Total_Distributed) AS Remaining
    FROM Wine
""")
for row in cursor.fetchall():
    print(f"Wine: {row[0]}, Produced: {row[1]}, Distributed: {row[2]}, Remaining: {row[3]}")

cursor.close()
conn.close()
