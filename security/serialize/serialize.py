"""
Serialize module analyze json/yml or whatever to pass the data to
cryptor module:
 - yml to binary string
"""

import yaml
import pickle


from reader.reader import Reader
raw_result = Reader.write_result()  # но мы же его уже вызываем в main


class Parser:
    def __init__(self):
        self.raw = raw_result
        pass

    def yaml_to_string(self):
        """
        Yaml parsing (because yml returns objects, not strings)
        :return: binary string
        """
        with open('parser.pickle', "wb") as file:
            pickle.dump(obj, file, protocol=None, *, fix_imports=True)





