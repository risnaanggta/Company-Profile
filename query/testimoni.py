import connectdb
import os
from werkzeug.utils import secure_filename

def query_get_all_testimoni():
    conn = connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT nama, testimoni, id FROM \"_672020237_pb_testimoni\"")
        rows = cur.fetchall()
        cur.close()
        testimoni = []
        for row in rows:
            testimoni = {
                "nama": row[0],
                "testimoni": row[1],
                "id": row[2],
            }
            testimoni.append(testimoni)
        return testimoni
    else:
        print("Connection Failed")
        return None

def query_add_testimoni(nama, testimoni):
    conn = connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        
        # Simpan gambar ke folder di backend
      
        
        # Simpan informasi produk ke database
        cur.execute("INSERT INTO _672020237_pb_testimoni (nama, testimoni) VALUES (%s, %s)", (nama, testimoni))
        conn.commit()
        cur.close()
        return True
    else:
        print("Connection Failed")
        return False

#query update testimoni
def query_update_testimoni(nama, testimoni, id):
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("UPDATE _672020237_pb_testimoni SET nama = %s, testimoni = %s WHERE id = %s", (nama, testimoni, id))
        conn.commit()
        cur.close()
        return True
    else:
        print("Connection Failed")
        return False

#query delete testimoni
def query_delete_testimoni(id):
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("DELETE FROM _672020237_pb_testimoni WHERE id = %s", (id,))
        conn.commit()
        cur.close()
        return True
    else:
        print("Connection Failed")
        return False
    
    
#ambil data  berdasarkan id
def query_get_testimoni_by_id(id):
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        
        cur.execute("SELECT nama, testimoni, id FROM public.\"_672020237_pb_testimoni\" WHERE id = %s", (id,))
        rows = cur.fetchall()
        cur.close()
        testimoni = []
        for row in rows:
            testimoni = {
                "nama": row[0],
                "testimoni": row[1],
                "id": row[2]
            }
            testimoni.append(testimoni)
        return testimoni
    else:
        print("Connection Failed")
        return None