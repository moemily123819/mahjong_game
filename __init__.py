import sqlite3
from sqlite3 import Error
 
    
#CREATE TABLE IF NOT EXISTS users (
# id integer PRIMARY KEY,
# name text NOT NULL,
# pwd text,
# status varchar(1)
#);


 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
#            conn = sqlite3.connect(':memory:')
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
  #  finally:
  #      conn.close()
    return None    

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def main():
    database = "db/mahjong.db"
 
    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        NAME text NOT NULL,
                                        PWD text,
                                        STATUS VARCHAR(1)
                                    ); """
    # create a database connection
    conn = create_connection(database)
    print('create connection ended')
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_users_table)
    else:
        print("Error! cannot create the database connection.")        
        
if __name__ == '__main__':
    main()        