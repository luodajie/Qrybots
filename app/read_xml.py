import os
import xml.etree.ElementTree as ET


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
		print fetched_file
		tree = ET.parse(fetched_file)
		root = tree.getroot()
		x = root.get('sql')
		print x
		# dic = {}
		# lsts1 = []
		for child in root.iter('input'):
		# 	# if not child.attrib['type'] =='csv':
			name = child.get('name')
			type = child.get('type')
			print name, type
		# 	lsts1.append(name)
		# 	dic[x] =  lsts1
		# for key, value in dic.iteritems():
		# 	xml_name.append(key)
		# 	xml_values.append(value)
		# df = pd.DataFrame(data=xml_values, index=xml_name)
		# return df


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# path = os.path.join(BASE_DIR, "config")
# xml_instance = Xml_File_Parser(path)
# xml_instance.get_filename()
# xml_instance.fetch_file_data()
