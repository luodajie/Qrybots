import os

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

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# path = os.path.join(BASE_DIR, "config")
# xml_instance = Xml_File_Parser(path)
# xml_instance.get_filename()
