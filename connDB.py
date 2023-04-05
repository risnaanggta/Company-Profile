import psycopg2

instance_name = "sat-kapita-selekta-b:asia-southeast2:training-kapita-selekta"
port = 5432
db = "postgres"
user = "postgres"
password = "FwF6qfEA5AzlztzG"

param = f"host='localhost' port={port} dbname='{db}' user='{user}' password='{password}'"
conn = psycopg2.connect(param)

query = 'SELECT current_date'
curs = conn.cursor()
curs.execute(query)
data=curs.fetchall()
print (data)