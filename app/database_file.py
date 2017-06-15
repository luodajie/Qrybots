import cx_Oracle

from pprint import pprint

user = 'bordee'
passwrd = 'stunner1234'
dsn = 'rtxa1-scan.labcorp.com:1521/lcadwp1.labcorp.com'


# id = 12


def check_existing_tables(tables=None, codes=None, id=None):
    print tables
    con = cx_Oracle.connect('bordee/stunner1234@rtxa1-scan.labcorp.com:1521/lcadwp1.labcorp.com')
    cur = con.cursor()

    for tab in tables:
        try:
            tab = str(tab).format(id)
        except:
            tab = str(tab).format('', id)
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

            # create_table(tab, cur)

    print repr(con.version)
    con.close()


def create_icd_table(table_name=None, cursor=None, con=None, codes=None):
    # searching for codes table
    if 'codes' in table_name:
        # creating ICD codes table
        stmt = 'CREATE TABLE {} (code VARCHAR(500))'.format(table_name)
        cursor.execute(stmt)
        print "Table is created"

        # dummy list of ICD codes
        # mylst = [i for i in codes]

        # inserting data into ICD codes table
        stmt = "INSERT INTO {} (code) VALUES (:1)".format(table_name)
        # execute many needs sequence of rows, that's why we did this for right side argument.
        cursor.executemany(stmt, [(str(v),) for v in codes])
        con.commit()  # commit insertion into database
        print "Data Inserted in ICD table"
        # create_rest_of_the_tables(cursor)


def create_rest_of_the_tables(cursor):
    stmt = "create table Req{0}_Specimen as select distinct specimen_number from Req{0}_codes mycodes, " \
           "proddb2.dd_trrmr65_lhcs_codes codes " \
           "where " \
           "trim(codes.code) = mycodes.code " \
           "and codes.data_year = {3} " \
           "and codes.data_month = {4}".format(id, "12", "13", '2007', '1')
    cursor.execute(stmt)
    print "Table Created"

# lst = ['Req{0}_Specimen', 'Req{0}_codes']
# lst = ['Req{0}_by_state', 'Req{0}_by_zip', 'Req{0}_codes', 'Req{0}_Join', 'Req{0}_Join_DD', 'Req{0}_Specimen']
# check_existing_tables(lst)
