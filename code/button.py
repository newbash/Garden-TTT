import pygame


class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.alpha = 0
        self.font = pygame.font.SysFont('Arial', 36)

        # Creates peristent surface for the button
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)

    def draw(self, screen):
        if self.alpha < 255:
            self.alpha += 9

        self.surface.set_alpha(self.alpha)
        self.surface.fill((0, 0, 0, 0))

        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(
            mouse_pos) else self.color

        pygame.draw.rect(self.surface, current_color,
                         (0, 0, self.rect.width, self.rect.height))

        text_surface = self.font.render(self.text, True, 'white')

        text_rect = text_surface.get_rect(
            center=(self.rect.width // 2, self.rect.height // 2))
        self.surface.blit(text_surface, text_rect)

        screen.blit(self.surface, self.rect.topleft)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False
