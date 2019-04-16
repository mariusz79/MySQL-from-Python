import datetime
import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='Chinook')
                            
try:
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = %s where name = %s;",
        (23, 'Bob'))
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()
