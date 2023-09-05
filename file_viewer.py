import os
class FileViewer:
    def __init__(self):
        self.current_file = None
        self.content = ''

    def open_file(self, filename, fs):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.current_file = filename
                self.content = file.read()
                fs.files[filename] = self.content
        else:
            print(f"File {filename} does not exist.")
            self.current_file = None
            self.content = ''

    def display(self):
        if self.current_file:
            return f'File Viewer: {self.current_file} Content: {self.content}'
        else:
            return 'File Viewer: No file selected'