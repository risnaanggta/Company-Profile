import connectdb

def query_booking(nama, notelp, tanggal, people, pesan):
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("INSERT INTO _672020237_pb_booking (nama, notelp, tanggal, people, pesan) VALUES (%s, %s, %s, %s, %s )", (nama, notelp, tanggal, people, pesan))
        conn.commit()
        cur.close()
        return True
    else:
        print("Connection Failed")
        return False

