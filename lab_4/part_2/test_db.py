import psycopg2
import time

create_table_query = '''
CREATE TABLE Products (
            product_id SERIAL PRIMARY KEY,
            product_name VARCHAR(255) NOT NULL
        )
'''
insert_value_query = 'INSERT INTO Products VALUES (1, \'Beer\')'
select_query = 'SELECT * FROM Products'
queries = (create_table_query, insert_value_query, select_query)

time.sleep(10)
try:

	conn = psycopg2.connect(
		dbname='test_db', 
		user='postgres', 
	    password='postgres', 
	    host='pg_db'
		)
	cursor = conn.cursor()

	for i, query in enumerate(queries):
		cursor.execute(query)
		if i == 2:
			for row in cursor:
				print(row)

	cursor.close()
	conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
	print(error)
finally:
	if conn is not None:
		conn.close()

