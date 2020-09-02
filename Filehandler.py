class FileHandler:
    def __init__(self, filePath):
        self.filePath = filePath
        self.file = None;
    
    def write_to_file(self, data):
        self.__open_file_write()
        self.file.write(data + "\n")
        self.__close_file()
        
    def append_to_file(self, data):
        self.__open_file_append()
        self.file.write(data + "\n")
        self.__close_file()
        
    def read_from_file(self):
        self.__open_file_read()
        data = self.file.read()
        self.__close_file()
        return data;
    
    def __open_file_write(self):
        self.file = open(self.filePath, "w")
        
    def __open_file_append(self):
        self.file = open(self.filePath, "a+")
    
    def __open_file_read(self):
        self.file = open(self.filePath, "r")
        
    def __close_file(self):
        self.file.close()