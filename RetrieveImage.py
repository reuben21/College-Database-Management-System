import pymysql
import sys
from PIL import Image
import base64
import io
import PIL.Image

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(f"{filename}", 'wb') as file:
        file.write(data)

def readBLOB():
    print("Reading BLOB data from python_employee table")


    host="localhost";user="root";
    dbname="studentDBMS"
    conn = pymysql.connect(host, user=user,port=3306,passwd="reuben", db=dbname)
    cursor = conn.cursor()
    sql_fetch_blob_query = """SELECT * from images where ImageID = %s"""

    cursor.execute(sql_fetch_blob_query, (2,))
    record = cursor.fetchall()
    for row in record:
        print("Id = ", row[0], )
        image = row[1]
        print(type(image))
        print("Storing employee image and bio-data on disk \n")
        write_file(image,"Andy21342134121412.jpg")
        # file12=base64.b64decode(row[1])
        # file_like=io.BytesIO(file12)
        # img=PIL.Image.open(file_like)
        # img.show()
    conn.commit()
    conn.close()




readBLOB()