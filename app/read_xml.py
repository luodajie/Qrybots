import os
import pandas as pd
import xml.etree.ElementTree as ET

from query_dialog import Query_Window


class Xml_File_Parser(object):
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
		fetched_file =  os.path.join(self.path, file_name)
		tree = ET.parse(fetched_file)
		root = tree.getroot()
		dicst = {}
		field_name = []
		field_type = []
		# x = root.get('sql')
		for child in root.iter('input'):
			name = child.get('name')
			type = child.get('type')
			dicst[name] = type
			field_name.append(name)
			field_type.append(type)
		df = pd.DataFrame(data=field_type, index= field_name)
		self.wind = Query_Window(fields=df)
		self.wind.show()


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# path = os.path.join(BASE_DIR, "config")
# xml_instance = Xml_File_Parser(path)
# xml_instance.get_filename()
# xml_instance.fetch_file_data()
