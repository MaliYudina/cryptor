"""
User_interface module determine the way of information collection from a user
"""
import subprocess


class Interface:
    def __init__(self):
        collection_dict = {}
        self.collection = collection_dict


    def collect_input(self, source):
        """
        Collect user's information regardless the type of information origin:
         - input
         - file from hard memory
        """

        # collection2 = subprocess.Popen([r".../textedit.app"])
        with open(source, 'w', encoding='UTF-8'):
            return self.collection

    def delete_record(self, delete=None):
        """
        Delete any record if needed
        """
        delete = input('key to delete')

        collect_dict = self.collection
        collect_dict.pop(delete)
        return collect_dict


    def display_record(self):
        """
        display the records of the received information:
         - per record (using unique name)
         - all records
        """
        collect_dict = {}
        user_command_input = input(
            'Input command to display the records\nall - all records\n'
            'name - specific name record\n'
            'del - del record\n')
        if user_command_input == 'all':
            return collect_dict
        if user_command_input == "name_record":
            name = input('some name')
        if user_command_input == "del":
            return delete_record()
        raise ValueError('Unknown command')

        pass



    collect_input(source = input('Please write file name'))
    delete_record()



