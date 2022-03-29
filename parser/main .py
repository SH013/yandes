import psycopg2
from config import user, host, password, db_name

connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name   
    )
connection.autocommit = True

"""создовал таблицу в psql и импортировал туда файл для более удобного просмотра таблицы"""

try:
    with connection.cursor() as cursor:
        cursor.execute(""" create table ppd(
            Transaction varchar(100),
            price varchar(100),
            date varchar (100),
            Postcode varchar(100),
            Property  varchar(100),
            OldNew varchar(100),
            Duration varchar(100),
            PAON varchar(100),
            SAON varchar(100),
            Street varchar(100),
            Locality varchar(100),
            Town varchar(100),
            District varchar(100),
            County varchar(100),
            Category  varchar(100),
            Record varchar(100));"""
        )
        print("[INFO] Table created successfully")


    with connection.cursor() as cursor:
        cursor.execute("""COPY ppd From 'G:/qw/pp-complete.csv' 
                        DELIMITER ',' CSV HEADER;"""
                            )
        print("[INFO] Table COPY successfully")


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex) 
   
   
