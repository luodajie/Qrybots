import os

# Fetching file path, platform independent
BASE_DIR = os.path.dirname(os.path.abspath(''))
file_directory = os.path.join(BASE_DIR, 'config')


def data_mapping(lst):
    # taking dynamic list and creating dictionary from it, so that we can use it to substitute args in prameterized sql.
    data = {}
    # lst = ["12", "2007", '13', '2015-01-01', '2016-08-01']
    for i in range(5):
        data[i + 1] = lst[i]
    print data

    read_parameterized_sql(data)


def read_parameterized_sql(data):
    actual_path = os.path.join(file_directory, 'parameterized.sql')
    collect_query = []

    with open(actual_path, 'rb') as param_sql:
        for statements in (param_sql.read().split(';')):
            collect_query.append(statements)

    translated_query = []
    for statements in collect_query:
        # keeping blank space coz args {1} start from 1 in parameterized sql
        translated = statements.format("", *data.values())
        translated_query.append(translated)

    write_translated_sql(translated_query)


def write_translated_sql(translated_query):
    actual_path = os.path.join(file_directory, 'Translated_SQL.sql')
    with open(actual_path, 'w') as trans_sql:
        query = ';'.join(translated_query)
        trans_sql.write(query.rstrip('\n'))
        print "File Written"




# use it while reading the file
# with open(os.path.join(file_directory, 'mytranslated.sql'), 'r') as q:
#     for line in q:
#         print line.strip()
