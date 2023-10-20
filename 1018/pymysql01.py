import pymysql

connection = pymysql.connect(
    host='localhost',
    port=3306,
    user = 'root',
    password='wedding05',
    database='test'
)

try:
    with connection.cursor() as cursor:
        create_table_sql = '''
        CREATE TABLE class_m (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT
        )
        '''

        cursor.execute(create_table_sql)
        print('Table Created')

finally:
    connection.close()
