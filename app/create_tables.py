import cx_Oracle
import pandas as pd


# def check_existing_table(ord_accts_table_data, tests_table_data, user='bordee', passwrd='Eliezer!456', req_num=None):

def check_existing_table(user=None, passwrd=None, id=None):
    table_list = [
        'Req{1}_by_state',
        ' Req{1}_by_zip',
        'Req{1}_codes',
        ' Req{1}_Join',
        ' Req{1}_Join_DD',
        ' Req{1}_Specimen',
    ]
    dsn = 'rtxa1-scan.labcorp.com:1521/lcadwp1.labcorp.com'

    con = cx_Oracle.connect("{0}/{1}@{2}".format(user, passwrd, dsn))
    cur = con.cursor()
    print "Connection Successful", con.version
    table_name = 'Req{0}_codes'.format(id)

    for table in table_list:
        table_name = table.format(id)
        print table_name
    # cur1 = con.cursor()
    #
    # # To check whether table exist or not:
    stmt = "SELECT tname FROM tab WHERE tname = '" + table_name + "'"
    cur.execute(stmt)
    trends_demo_tablename = cur.fetchone()
    print trends_demo_tablename
    #
    # stmt1 = "SELECT tname FROM tab WHERE tname = 'TRENDS_RESULTS_{}'".format(req_num)
    # cur1.execute(stmt1)
    # trends_result_tablename = cur1.fetchone()

    # create_trends_ords_table(trends_demo_tablename, cur, req_num)
    # create_trends_rslts_table(trends_result_tablename, cur1, req_num)
    #
    # insert_data_trends_ords_table(ord_accts_table_data, user, passwrd, req_num)
    # insert_data_trends_rslt_table(tests_table_data, user, passwrd, req_num)

    # cur1.close()
    # cur.close()
    con.close()


# def create_trends_ords_table(trends_demo_tablename, cur, req_num):
# 	create_stmt = "CREATE TABLE TRENDS_DEMO_%s (EID VARCHAR2(80),ORDER_CODE VARCHAR2(60),ORDER_NAME VARCHAR2(512),PSEUDO_LPID VARCHAR2(130),DATE_OF_BIRTH DATE,PATIENT_SEX VARCHAR2(50), " \
# 				  "ORDERING_ACCT_NUM VARCHAR2(8),ACCOUNT_FACILITY VARCHAR2(30),ACCOUNT_ADDRESS VARCHAR2(35), " \
# 				  "ACCOUNT_ST VARCHAR2(2),ACCOUNT_ZIP VARCHAR2(5),NPI_NUM VARCHAR2(50),LPID VARCHAR2(256),FILLERORDERNO VARCHAR2(60),DRAW_DATE DATE)" % req_num
#
# 	drop_stmt = "DROP TABLE TRENDS_DEMO_%s" % req_num
#
# 	grant_stmt = "GRANT SELECT ON TRENDS_DEMO_%s TO PUBLIC" % req_num
#
# 	if trends_demo_tablename:
# 		print "Table Found:", trends_demo_tablename[0]
# 		cur.execute(drop_stmt)
# 		print "Table Dropped"
#
# 	cur.execute(create_stmt)
# 	cur.execute(grant_stmt)
# 	print "Table Created"

def icd_codes_table(cur, id):
    query = "create TABLE Req'{0}'_codes (Code VARCHAR(20))".format(id)


def auto_generated_parameterized_sql(cur, id):
    pass


check_existing_table(user='bordee', passwrd='Eliezer!456', id=1)
