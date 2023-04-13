import connectdb
import os
from werkzeug.utils import secure_filename

def query_get_all_testimoni():
    conn = connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT nama, testimoni FROM \"_672020237_pb_testimoni\"")
        rows = cur.fetchall()
        cur.close()
        testimoni_list = []
        for row in rows:
            testimoni = {
                "nama": row[0],
                "testimoni": row[1],
            }
            testimoni_list.append(testimoni)
        return testimoni_list
    else:
        print("Connection Failed")
        return None


def query_add_testimoni(nama, testimoni):
    conn = connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()

        cur.execute("INSERT INTO _672020237_pb_testimoni (nama, testimoni) VALUES (%s, %s)", (nama, testimoni))
        conn.commit()
        cur.close()
        return True
    else:
        print("Connection Failed")
        return False


    
    