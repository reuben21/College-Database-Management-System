import pymysql


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def upload_to_aws(photo):
    print("Inserting BLOB into python_employee table")
    try:
        host="localhost";user="root";
        dbname="studentDBMS"
        conn = pymysql.connect(host, user=user,port=3306,passwd="reuben", db=dbname)

        cursor = conn.cursor()
        sql_insert_blob_query = """ INSERT INTO images
                          (picture) VALUES (%s)"""

        empPicture = convertToBinaryData(photo)
    

        # Convert data into tuple format
        insert_blob_tuple = (empPicture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        conn.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)
        cursor.close()
        conn.close()

    except Exception as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))



insertBLOB("C:\\Users\\Reuben Coutinho\\Downloads\\Andy-509.jpg")