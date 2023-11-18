import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='root'
)

cur = conn.cursor()

cur.execute("COPY customers FROM 'C:\customers_data.csv' DELIMITER ',' CSV HEADER;")
cur.execute("COPY employees FROM 'C:\employees_data.csv' DELIMITER ',' CSV HEADER;")
cur.execute("COPY orders FROM 'C:\orders_data.csv' DELIMITER ',' CSV HEADER;")
conn.commit()

cur.close()
conn.close()