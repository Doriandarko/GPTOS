import pygame

class WindowManager:
    def __init__(self):
        self.open_windows = []

    def open_window(self, window_name, content=None):
        self.open_windows.append((window_name, content))

    def close_window(self, window_name):
        self.open_windows = [(name, cnt) for name, cnt in self.open_windows if name != window_name]

    def draw_windows(self, screen, font, color, SCREEN_WIDTH, SCREEN_HEIGHT, editor, snake_game):
        for window, content in self.open_windows:
            # Clear the background first to avoid overlapping text
            pygame.draw.rect(screen, color, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

            # Draw the window title at the top
            title_surface = font.render(window, True, (52, 50, 25))
            screen.blit(title_surface, (10, 10))

            if window == 'Snake Game':
                snake_game.display(screen, font)
                continue

            # Update Text Editor content if window matches editor
            if window == editor.current_file:
                content_surface = font.render(editor.content, True, (52, 50, 25))
                screen.blit(content_surface, (10, 50))
            else:
                # Draw other content types
                if content:
                    content_surface = font.render(content, True, (52, 50, 25))
                    screen.blit(content_surface, (10, 50))

            if window == editor.current_file:
                editor.save_button.topleft = (SCREEN_WIDTH - 80, SCREEN_HEIGHT - 30)
                pygame.draw.rect(screen, (52, 50, 25), editor.save_button)
                save_surface = font.render('SAVE', True, (228, 255, 254))
                screen.blit(save_surface, (SCREEN_WIDTH - 70, SCREEN_HEIGHT - 25))

                # Show "Changes saved" only within 1 second after saving
                if editor.save_status and pygame.time.get_ticks() - editor.save_timestamp < 2000:
                    save_status_surface = font.render('Changes saved', True, (52, 50, 25))  # Explicitly set to red
                    screen.blit(save_status_surface, (10, SCREEN_HEIGHT - 30))  # Bottom left corner

            # Draw the close button (x) at the top right corner
            close_surface = font.render("x", True, (52, 50, 25))
            screen.blit(close_surface, (SCREEN_WIDTH - 20, 10))
