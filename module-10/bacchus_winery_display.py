import mysql.connector


connection = mysql.connector.connect(
    host="localhost",   
    user="root",  
    password="Rileypop15!!",  
    database="Bacchus_Winery"
)

cursor = connection.cursor()

def display_table(table_name):
    print(f"\n-- {table_name} --")
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    print(f"{' | '.join(columns)}")
    print("-" * 80)
    for row in rows:
        print(" | ".join(str(value) for value in row))
    print("-" * 80)

try:
    tables = [
        "Department", "Employee", "Work_Hours", 
        "Supplier", "Supply", "Inventory", 
        "Wine", "Distributor", "Wine_Order"
    ]

    for table in tables:
        display_table(table)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    connection.close()
    print("\nConnection closed.")
