# Event class file

class Event:
    def __init__(self, name, id):
        self.title = name
        self.id = id


    def addAddress(self, address):
        self.location = address