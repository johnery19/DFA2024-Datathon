import psycopg2

hostname='localhost',
database='school_performance_db',
username='postgres',
pwd = 123456
port_id = 5432

try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port = port_id )

    cur = conn.cursor


    cur.close()
    conn.close()
    
except Exception as error:
    print(error)

    finally 