import os

class FileSystem:
    def __init__(self):
        self.files = {}

    def create_file(self, filename):
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                self.files[filename] = ''
        else:
            print(f"File {filename} already exists.")

    def delete_file(self, filename):
        if os.path.exists(filename):
            os.remove(filename)
            self.files.pop(filename, None)
        else:
            print(f"File {filename} does not exist.")

    def write_to_file(self, filename, content):
        if os.path.exists(filename):
            with open(filename, 'w') as file:
                file.write(content)
                self.files[filename] = content
        else:
            print(f"File {filename} does not exist.")

    def display(self):
        return f'File System: {", ".join(self.files.keys())}'