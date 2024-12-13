class NameID:
    def setID(self, ID: str):
        if isinstance(ID, str) and ID != "":
            self._ID = ID
            return 1
        else:
            print("ID must be an non-empty string\n")
            return 0

    def setName(self, name: str):
        if isinstance(name, str) and name != "":
            self._name = name
            return 1
        else:
            print("Name must be an non-empty string\n")
            return 0

    def getName(self):
        return self._name

    def getID(self):
        return self._ID
