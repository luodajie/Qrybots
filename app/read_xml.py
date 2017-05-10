import os
import pandas as pd
from tabulate import tabulate
import xml.etree.ElementTree as ET

from query_dialog import Query_Window


class XmlFileParser(object):
    def __init__(self, path):
        self.path = path

    def get_filename(self):
        filename_list = []
        for files in os.listdir(self.path):
            if ".xml" in files:
                name, ext = files.split('.')
                filename_list.append(name)

        return filename_list

    def fetch_file_data(self, file_name):
        fetched_file = os.path.join(self.path, file_name)
        tree = ET.parse(fetched_file)
        root = tree.getroot()
        description = root.get('desc')
        field_name = []
        field_type = []
        field_ids = []
        # x = root.get('sql')
        for child in root.iter('input'):
            name = child.get('name')
            type = child.get('type')
            field_id = child.get('id')
            tab = child.get('table')
            if tab:
                print "-------------------------------"
                print "|    Input Table: ", tab,    '|'
                print "-------------------------------"

            field_name.append(name)
            field_type.append(type)
            field_ids.append(field_id)
        df = pd.DataFrame({'Type': field_type, 'Id': field_ids}, index=field_name)
        print tabulate(df, headers='keys', tablefmt='psql')
        for chi in root.iter('tables'):
            for t in root.iter('table'):
                print t.get('name')
        self.wind = Query_Window(fields=df, desc=description)
        self.wind.show()

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# path = os.path.join(BASE_DIR, "config")
# xml_instance = Xml_File_Parser(path)
# xml_instance.get_filename()
# xml_instance.fetch_file_data()
