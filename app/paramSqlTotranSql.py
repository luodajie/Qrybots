import os

# Fetching file path, platform independent
BASE_DIR = os.path.dirname(os.path.abspath(''))
file_directory = os.path.join(BASE_DIR, 'config')


def data_mapping(lst, sqlfile):
    # taking dynamic list and creating dictionary from it, so that we can use it to substitute args in prameterized sql.
    data = {}
    try:
        for i in range(len(lst)):
            data[i + 1] = lst[i]
        print data

        read_parameterized_sql(data, sqlfile)

    except:
        pass


def read_parameterized_sql(data, sqlfile):
    actual_path = os.path.join(file_directory, sqlfile)
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
    with open(actual_path, 'wb') as trans_sql:
        for i in translated_query:
            lines = "{};".format(i)
            trans_sql.write(lines)
    # with open(actual_path, 'w') as trans_sql:
    #     query = ';'.join(translated_query)
    #     trans_sql.write(query.rstrip('\n'))
        print "File Written"

