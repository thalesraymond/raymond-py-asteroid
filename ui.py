import pygame

_font = None

def _get_font():
    global _font
    if _font is None:
        _font = pygame.font.Font(None, 36)
    return _font

def draw_ui(screen, player):
    font = _get_font()
    lives_text_surface = font.render(f"Lives: {player.lives}", True, "white")
    screen.blit(lives_text_surface, (10, 10))
    
    score_text_surface = font.render(f"Score: {player.score}", True, "white")
    screen.blit(score_text_surface, (10, 50))
    
    pygame.display.flip()