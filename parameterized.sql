create table Req{1}_Specimen as
select distinct specimen_number
from Req{1}_codes mycodes,
     proddb2.trrmr65_lhcs_codes codes
where 
trim(codes.code) = mycodes.code
and codes.data_year = {2}
and codes.data_month = {3};

create table Req{1}_Join as
select distinct spec.specimen_number, spec.data_year, spec.data_month, spec.draw_date, 
	(upper(trim(patient_name_last)) || upper(trim(patient_name_first)) || to_char(date_of_birth,'YYYY-MM-DD')) as pseudo_lpid,
	report_state, report_zip5	
from proddb2.trrmr58_lhcs_spec spec,
	 proddb2.trllr18_d_cust1 cust,
	 Req{1}_Specimen myspec
where 
myspec.specimen_number = spec.specimen_number
and spec.data_year = {2}
and spec.data_month = {3}
and spec.draw_date <= TO_DATE('{4}','YYYY-MM-DD') 
and spec.draw_date >= TO_DATE('{5}','YYYY-MM-DD')
and spec.ordering_acct_num = cust.account_number;

create table Req{1}_Join_DD as 
select a.* 
from Req{1}_Join a, 
    (select specimen_number, max(data_year*100+data_month) as yrmo from Req{1}_Join group by specimen_number) b
where a.specimen_number=b.specimen_number 
and (a.data_year*100+a.data_month) = b.yrmo;

create table Req{1}_by_state as
select report_state, count(distinct pseudo_lpid) as patient_count from Req{1}_Join_DD group by report_state;

create table Req{1}_by_zip as
select report_zip5, count(distinct pseudo_lpid) as patient_count from Req{1}_Join_DD group by report_zip5;
