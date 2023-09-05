import pygame
import sys

class CLI:
    def __init__(self):
        self.commands = ['help', 'exit', 'create', 'delete', 'edit', 'open', 'close', 'play', 'tasks', 'view']
        self.current_command = ''
    
    def handle_input(self, key, fs, editor, pm, wm, snake_game, task_manager, file_viewer):
        """Handle input events. If return key is pressed, execute current command."""
        if wm.open_windows and wm.open_windows[-1][0] == editor.current_file and editor.current_file is not None:
            print(f"Text editor active. Key: {key}")  # Debug print
            if key == pygame.K_s:  # Save changes when 's' key is pressed
                editor.save()
            else:
                editor.handle_key(key)
        else:
            # If the text editor window is not active, handle key inputs in the CLI
            keys = pygame.key.get_pressed()
            shift_pressed = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

            if key == pygame.K_RETURN:
                self.execute_command(fs, editor, pm, wm, snake_game, task_manager, file_viewer)
                self.current_command = ''
            elif key == pygame.K_BACKSPACE:
                self.current_command = self.current_command[:-1] if self.current_command else ''
            elif key == pygame.K_MINUS and shift_pressed:  # Check if the minus key is pressed with shift
                self.current_command += '_'
            elif 32 <= key <= 126:  # ASCII values for alphanumeric characters
                char = chr(key)
                if shift_pressed:
                    char = char.upper()
                self.current_command += char
    
    def execute_command(self, fs, editor, pm, wm, snake_game, task_manager, file_viewer):
        parts = self.current_command.split()
        command = parts[0]
    
        if command in ['create', 'delete', 'edit', 'open', 'close', 'view'] and len(parts) < 2:
            print(f"The {command} command requires a filename as an argument.")
            return
        
        if command == 'exit':
            pygame.quit()
            sys.exit()
        elif command == 'create':
            fs.create_file(parts[1])
        elif command == 'delete':
            fs.delete_file(parts[1])
        elif command == 'open':
            file_viewer.open_file(parts[1], fs)
            wm.open_window(parts[1], file_viewer.content)
        elif command == 'edit':
            editor.edit_file(parts[1])
            wm.open_window(parts[1], editor.content)
        elif command == 'close':
            wm.close_window(parts[1])
        elif command == 'play':
            args = parts[1:]
            if len(args) == 1:
                game_name = args[0]
                if game_name == 'snake_game.py':
                    snake_game.start()
                    wm.open_window('Snake Game')
        elif command == 'tasks':
            task_manager.toggle()
        elif command == 'view':
            file_viewer.open_file(parts[1], fs)
    
    def display(self):
        return f'CLI: {self.current_command} | Available Commands: {", ".join(self.commands)}'
