"""
Parse module gets the text information from the offered files
Extracts necessary data such as passwords, secret questions, private information
"""
import yaml


class Reader:
    """
    Class for all secure information
    """
    def __init__(self):
        pass

    def read(self):
        """
        Reads collected information from user_interface module
        """
        user_input = input('')
        return user_input

    def write_result(self, user_input=None):
        """
        Save result into permanent files

        """
        with open('user_raw_data.yml', 'w') as f:
            yaml.dump(user_input, f)






