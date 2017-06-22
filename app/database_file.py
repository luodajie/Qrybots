import cx_Oracle
import csv
import os


# global variable for oracle


# global variable for file path
BASE_DIR = os.path.dirname(os.path.abspath(''))
file_directory = os.path.join(BASE_DIR, 'config')


def check_existing_tables(tables=None, codes=None, id=None, file_download_location=None):
    print "Tables are: ", tables
    con = cx_Oracle.connect('username/password@proxyserver')
    cur = con.cursor()

    for table_name, value in tables.iterrows():
        try:
            tab = str(table_name).format(id)
        except:
            tab = str(table_name).format('', id)
        try:
            stmt = "SELECT table_name FROM user_tables WHERE table_name = '" + tab.upper() + "'"
            cur.execute(stmt)
            checker = (bool(cur.fetchone()))
            # pprint(checker)

            if not checker:
                create_icd_table(table_name=tab, cursor=cur, con=con, codes=codes)

            else:
                stmt = 'Drop Table {}'.format(tab)
                cur.execute(stmt)
                print 'Table Dropped'

                create_rest_of_the_tables(con=con, cursor=cur)

        except:
            pass

    export_tables_to_csv(tables=tables, cursor=cur, id=id, file_download_location=file_download_location)
    drop_unused_tables(tables=tables, cursor=cur, id=id)
    print repr(con.version)
    cur.close()
    con.close()


def create_icd_table(table_name=None, cursor=None, con=None, codes=None):
    # searching for codes table
    if 'codes' in table_name:
        # creating ICD codes table
        stmt = 'CREATE TABLE {} (code VARCHAR(500))'.format(table_name)
        cursor.execute(stmt)
        print "ICD Table is created"

        # inserting data into ICD codes table
        stmt = "INSERT INTO {} (code) VALUES (:1)".format(table_name)
        # execute many needs sequence of rows, that's why we did this for right side argument.
        cursor.executemany(stmt, [(str(v),) for v in codes])
        con.commit()  # commit insertion into database
        print "Data Inserted in ICD table"
        create_rest_of_the_tables(con=con, cursor=cursor)


def create_rest_of_the_tables(con=None, cursor=None):
    # use it while reading the file
    with open(os.path.join(file_directory, 'Translated_SQL.sql'), 'rb') as q:
        split_queries = [qry for qry in q.read().split(';')]
        for qry in split_queries:
            if qry == " ":
                pass
            else:
                stmt = """{}""".format(qry.strip('\n'))
                print stmt
                if stmt == '':
                    pass
                else:

                    cursor.execute(stmt)
                    con.commit()
                    print "Other Tables Created"


def export_tables_to_csv(tables=None, cursor=None, id=None, file_download_location=None):
    # try:
    for table_name, value in tables.iterrows():
        try:
            tab = str(table_name).format(id)
        except:
            tab = str(table_name).format('', id)
        if value.export == 'False':
            pass
        else:
            stmt = 'SELECT * from {}'.format(tab)
            cursor.execute(stmt)
            columns = [i[0] for i in cursor.description]
            download_data = cursor.fetchall()

            file_location = str(os.path.join(str(file_download_location), tab)) + '.csv'
            with open(file_location, "wb") as outputfile:
                writer = csv.writer(outputfile, dialect='excel')
                writer.writerow(columns)
                for row in download_data:
                    writer.writerow(row)

            print tab, 'Table are exported because "export" is True for the table in xml file'

            # except:
            #     pass


def drop_unused_tables(tables=None, cursor=None, id=id):
    for table_name, value in tables.iterrows():
        try:
            tab = str(table_name).format(id)
        except:
            tab = str(table_name).format('', id)
        if value.keep == 'False':
            stmt = 'Drop Table {}'.format(tab)
            cursor.execute(stmt)
            print tab, 'Table Dropped because "keep" is False for the table in xml file'
