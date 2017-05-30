import cx_Oracle
import pandas as pd


def check_existing_table(ord_accts_table_data, tests_table_data, user='bordee', passwrd='Eliezer!456', req_num=None):
    dsn = 'rtxa1-scan.labcorp.com:1521/lcadwp1.labcorp.com'

    con = cx_Oracle.connect(user='bordee', password='Eliezer!456', dsn=dsn)
    cur = con.cursor()
    cur1 = con.cursor()

    # To check whether table exist or not:
    stmt = "SELECT tname FROM tab WHERE tname = 'TRENDS_DEMO_{}'".format(req_num)
    cur.execute(stmt)
    trends_demo_tablename = cur.fetchone()

    stmt1 = "SELECT tname FROM tab WHERE tname = 'TRENDS_RESULTS_{}'".format(req_num)
    cur1.execute(stmt1)
    trends_result_tablename = cur1.fetchone()

    # create_trends_ords_table(trends_demo_tablename, cur, req_num)
    # create_trends_rslts_table(trends_result_tablename, cur1, req_num)
    #
    # insert_data_trends_ords_table(ord_accts_table_data, user, passwrd, req_num)
    # insert_data_trends_rslt_table(tests_table_data, user, passwrd, req_num)

    cur1.close()
    cur.close()
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


def specimen_table(cur, id):
    query = "create table Req'{0}'_Specimen as" \
            "select distinct specimen_number " \
            "from Req'{0}'_codes mycodes, " \
            "proddb2.trrmr65_lhcs_codes codes " \
            "where " \
            "trim(codes.code) = mycodes.code " \
            "and codes.data_month = 9;".format(id)


def join_table(cur, id):
    query = "create table Req'{0}'_Join as " \
            "select distinct spec.specimen_number, spec.data_year, spec.data_month, spec.draw_date, " \
            "(upper(trim(patient_name_last)) || upper(trim(patient_name_first)) || to_char(date_of_birth,'YYYY-MM-DD') " \
            "as pseudo_lpid, " \
            "report_state, report_zip5 " \
            "from proddb2.trrmr58_lhcs_spec spec, " \
            "proddb2.trllr18_d_cust1 cust, " \
            "Req'{0}'_Specimen myspec " \
            "where myspec.specimen_number = spec.specimen_number " \
            "and spec.data_year = 2015 " \
            "and spec.data_month = 9 " \
            "and spec.draw_date <= TO_DATE('2015-09-10','YYYY-MM-DD') " \
            "and spec.draw_date >= TO_DATE('2015-09-10','YYYY-MM-DD') " \
            "and spec.ordering_acct_num = cust.account_number;".format(id)


def join_dd_table(cur, id):
    query = "create table Req'{0}'_Join_DD as " \
            "select a.* " \
            "from Req'{0}'_Join a, " \
            "(select specimen_number, max(data_year*100+data_month) as yrmo from Req'{0}'_Join group " \
            "by specimen_number) b " \
            "where a.specimen_number=b.specimen_number " \
            "and (a.data_year*100+a.data_month) = b.yrmo;".format(id)


def patcnt_by_state_table(cur, id):
    query = "create table Req98_by_state as " \
            "select report_state, count(distinct pseudo_lpid) as patient_count " \
            "from Req'{0}'_Join_DD group by report_state;".format(id)


def patcnt_by_zip_table(cur, id):
    query = "create table Req98_by_zip as " \
            "select report_zip5, count(distinct pseudo_lpid) as " \
            "patient_count from Req'{0}'_Join_DD group by report_zip5;".format(id)
