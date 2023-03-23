import io


class CustomFileWriter:
    def __init__(self, filename) -> None:
        self.filename = filename
        
    def __enter__(self):
        self.file = open(self.filename,"w")
        return self.file
    
    def __exit__(self, type, value, traceback):
        if type == io.UnsupportedOperation :
            print(value.args)
        print(type)
        print(value)
        self.file.close()
        return True
    