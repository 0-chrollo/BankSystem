import json

class DataStorage:
    file_path= "C:\\Users\\lucas\Desktop\\Files\\ALL_ACCOUNTS.json"

    def __init__(self, File_Path):
        self.file_path = File_Path

    def SaveData(self,obj:object):
        with open(self.file_path, "w") as file:
            json.dump(obj, file)

    def LoadData(self):
     try:
          with open(self.file_path, "r") as file:

            return json.load(file)
     except FileNotFoundError:
         return None

    def hasFile(self):
        try:
            with open(self.file_path):
                return True
        except FileNotFoundError:
            return False





