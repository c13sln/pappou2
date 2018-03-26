import sqlite3

print("Hello World")


# Creates a db with name
def create_db(name):
    print("Creating db with name: " + name)
    sqlite_file = name+'.sqlite'    # name of the sqlite database file
    table_name1 = 'my_table_1'  # name of the table to be created
    table_name2 = 'my_table_2'  # name of the table to be created
    new_field = 'my_1st_column' # name of the column
    field_type = 'INTEGER'  # column data type

    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    # Creating a new SQLite table with 1 column
    c.execute('CREATE TABLE {tn} ({nf} {ft})'\
            .format(tn=table_name1, nf=new_field, ft=field_type))

    # Creating a second table with 1 column and set it as PRIMARY KEY
    # note that PRIMARY KEY column must consist of unique values!
    c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
            .format(tn=table_name2, nf=new_field, ft=field_type))

    # Committing changes and closing the connection to the database file
    conn.commit()
    conn.close()


# Creates and adds new column to database.
def add_column(db_name, table_name, col_name):
    sqlite_file = db_name  # name of the sqlite database file
    table_name = table_name  # name of the table to be created
    id_column = 'my_1st_column'  # name of the PRIMARY KEY column
    new_column1 = 'my_2nd_column'  # name of the new column
    new_column2 = 'my_3nd_column'  # name of the new column
    column_type = 'TEXT'  # E.g., INTEGER, TEXT, NULL, REAL, BLOB
    default_val = 'Hello World'  # a default value for the new column rows

    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    # A) Adding a new column without a row value
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}" \
              .format(tn=table_name, cn=new_column1, ct=column_type))

    # B) Adding a new column with a default row value
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'" \
              .format(tn=table_name, cn=new_column2, ct=column_type, df=default_val))

    # Committing changes and closing the connection to the database file
    conn.commit()
    conn.close()


def insert_row(db_name, table_name, id_col, col_name):
    sqlite_file = db_name
    table_name = table_name
    id_column = id_col
    column_name = col_name

    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    # A) Inserts an ID with a specific value in a second column
    try:
        c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')". \
                  format(tn=table_name, idf=id_column, cn=column_name))
    except sqlite3.IntegrityError:
        print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))

    # B) Tries to insert an ID (if it does not exist yet)
    # with a specific value in a second column
    c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')". \
              format(tn=table_name, idf=id_column, cn=column_name))

    # C) Updates the newly inserted or pre-existing entry
    c.execute("UPDATE {tn} SET {cn}=('Hi World') WHERE {idf}=(123456)". \
              format(tn=table_name, cn=column_name, idf=id_column))

    conn.commit()
    conn.close()


print("Goodbye World!")
