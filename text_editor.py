import pygame
import os




class TextEditor:
    def __init__(self):
        self.current_file = None
        self.content = ''
        self.save_button = pygame.Rect(0, 0, 80, 30)  # Update the position and size as needed
        self.save_status = False
        self.save_timestamp = 0

    def edit_file(self, filename):
        self.current_file = filename
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.content = file.read()
        else:
            print(f"File {filename} does not exist.")
            self.current_file = None
            self.content = ''

    def handle_key(self, key):
        if self.save_status:  # Reset the flag when a new key is pressed
            self.save_status = False

        print(f"Handling key: {key}")  # Debug print
        if key == pygame.K_BACKSPACE:
            self.content = self.content[:-1]
        elif key == pygame.K_RETURN:
            self.content += '\n'
        elif 0 <= key <= 1114111:  # Valid Unicode range
            self.content += chr(key)

    def save(self):
        if self.current_file:
            with open(self.current_file, 'w') as file:
                file.write(self.content)
            self.save_status = True
            self.save_timestamp = pygame.time.get_ticks()  # Record the time of saving
            print(f"File saved at {self.save_timestamp}, save_status: {self.save_status}")  # Debugging line

    def display(self):
        return f'Text Editor: Editing {self.current_file}' if self.current_file else 'Text Editor: No file selected'
