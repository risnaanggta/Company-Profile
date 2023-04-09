import connectdb

def query_testimoni(id, nama, testimoni):
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("INSERT INTO _672020237_pb_testimoni (id, nama, testimoni) VALUES (%s, %s, %s)", (id, nama, testimoni))
        conn.commit()
        cur.close()
        return True
    else:
        print("Connection Failed")
        return False

#query update user testimoni
def query_testimoni(id, nama, testimoni):
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.executecur.execute("UPDATE _672020237_pb_testimoni (id, nama, testimoni) VALUES (%s, %s, %s)", (id, nama, testimoni))
        conn.commit()
        cur.close()
        return True
    else:
        return False

#query delete user testimoni
def query_testimoni(id, nama, testimoni):
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("DELETE FROM _672020237_pb_testimoni (id, nama, testimoni) VALUES (%s, %s, %s)", (id, nama, testimoni))
        conn.commit()
        cur.close()
        return True
    else:
        return False