import pygame
import sys
from cli import CLI
from filesystem import FileSystem
from text_editor import TextEditor
from process_manager import ProcessManager
from window_manager import WindowManager
from snake_game import SnakeGame
from task_manager import TaskManager
from file_viewer import FileViewer
import time

pygame.init()
cli = CLI()
fs = FileSystem()
editor = TextEditor()
pm = ProcessManager()
wm = WindowManager()
snake_game = SnakeGame()
task_manager = TaskManager()
file_viewer = FileViewer()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FONT_SIZE = 20
HEADING_FONT_SIZE = 22
LIGHT_COLOR = (228, 255, 254)
DARK_COLOR = (52, 50, 25)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SimpleOS')
font = pygame.font.Font('assets/font.ttf', FONT_SIZE)
heading_font = pygame.font.Font('assets/font.ttf', HEADING_FONT_SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if wm.open_windows and wm.open_windows[-1][0] == 'Snake Game':
                snake_game.handle_input(event.key)
            else:
                cli.handle_input(event.key, fs, editor, pm, wm, snake_game, task_manager, file_viewer)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            x, y = pygame.mouse.get_pos()
            if wm.open_windows and wm.open_windows[-1][0] == editor.current_file:
                if editor.save_button.collidepoint(x, y):  # Check if the "Save" button is clicked
                    editor.save()
            # Check if the mouse is within the "x" button area
            if SCREEN_WIDTH - 20 <= x <= SCREEN_WIDTH - 10 and 10 <= y <= 20:
                if wm.open_windows and wm.open_windows[-1][0] == 'Snake Game':
                    snake_game.running = False  # Stop the snake game
                wm.close_window(wm.open_windows[-1][0] if wm.open_windows else None)
    
    screen.fill(DARK_COLOR)
    if snake_game.running:
        snake_game.update()
        snake_game.display(screen, font)
        pygame.time.delay(snake_game.speed)


    if wm.open_windows and wm.open_windows[-1][0] == editor.current_file:
        editor.save_button.topleft = (SCREEN_WIDTH - 80, SCREEN_HEIGHT - 30)
        pygame.draw.rect(screen, DARK_COLOR, editor.save_button)
        save_surface = font.render('SAVE', True, LIGHT_COLOR)
        screen.blit(save_surface, (SCREEN_WIDTH - 70, SCREEN_HEIGHT - 25))
        
        # Show "Changes saved" only within 1 second after saving
        current_ticks = pygame.time.get_ticks()  # Get current ticks
        if editor.save_status:
            print(f"Current: {current_ticks}, Saved at: {editor.save_timestamp}, Difference: {current_ticks - editor.save_timestamp}")  # Debugging line
            if current_ticks - editor.save_timestamp < 1000:
                save_status_surface = font.render('Changes saved', True, (255, 0, 0))  # Explicitly set to red
                screen.blit(save_status_surface, (100, 100))
            elif current_ticks - editor.save_timestamp >= 1000:
                editor.save_status = False


    cli_text = cli.display()
    cli_surface = heading_font.render(cli_text, True, LIGHT_COLOR)
    screen.blit(cli_surface, (20, 20))

    fs_text = fs.display()
    fs_surface = font.render(fs_text, True, LIGHT_COLOR)
    screen.blit(fs_surface, (420, 60))  # Adjusted y-coordinate

    editor_text = editor.display()
    editor_surface = font.render(editor_text, True, LIGHT_COLOR if not wm.open_windows or wm.open_windows[-1][0] != editor.current_file else DARK_COLOR)  # Change the text color to dark when a file is opened
    screen.blit(editor_surface, (20, 120))

    pm_text = pm.display()
    pm_surface = font.render(pm_text, True, LIGHT_COLOR)
    screen.blit(pm_surface, (420, 120))

   

    task_manager_text = task_manager.display(pm)
    task_manager_surface = font.render(task_manager_text, True, LIGHT_COLOR)
    screen.blit(task_manager_surface, (420, 320))

    file_viewer_text = file_viewer.display()
    file_viewer_surface = font.render(file_viewer_text, True, LIGHT_COLOR)
    screen.blit(file_viewer_surface, (20, 320))

    clock_text = time.strftime('%H:%M:%S')
    clock_surface = font.render(f'Clock: {clock_text}', True, LIGHT_COLOR)
    screen.blit(clock_surface, (20, 560))

    wm.draw_windows(screen, font, LIGHT_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT, editor, snake_game)




    pygame.display.update()