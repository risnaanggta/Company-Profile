import connectdb

def query_booking(nama, notelp, tanggal, people, request):
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("INSERT INTO 672020237_pb_booking (nama, notelp, tanggal, people, request) VALUES (%s, %d, %d, %s, %s )", (nama, notelp, tanggal, people, request))
        conn.commit()
        cur.close()
        return True
    else:
        print("Connection Failed")
        return False

