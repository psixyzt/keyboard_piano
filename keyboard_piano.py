import pygame
import sys

# Initialize pygame
pygame.init()

# Define key-to-note mapping
key_note_map = {
    pygame.K_1: "c3", pygame.K_q: "c3#", pygame.K_a: "d3", pygame.K_z: "d3#",
    pygame.K_2: "e3", pygame.K_w: "f3", pygame.K_s: "f3#", pygame.K_x: "g3",
    pygame.K_3: "g3#", pygame.K_e: "a4", pygame.K_d: "a4#", pygame.K_c: "b4",
    pygame.K_4: "c4", pygame.K_r: "c4#", pygame.K_f: "d4", pygame.K_v: "d4#",
    pygame.K_5: "e4", pygame.K_t: "f4", pygame.K_g: "f4#", pygame.K_b: "g4",
    pygame.K_6: "g4#", pygame.K_y: "a5", pygame.K_h: "a5#", pygame.K_n: "b5",
    pygame.K_7: "c5", pygame.K_u: "c5#", pygame.K_j: "d5", pygame.K_m: "d5#",
    pygame.K_8: "e5", pygame.K_i: "f5", pygame.K_k: "f5#", pygame.K_COMMA: "g5",
    pygame.K_9: "g5#", pygame.K_o: "a6", pygame.K_l: "a6#", pygame.K_PERIOD: "b6",
    pygame.K_0: "c6", pygame.K_p: "c6#", pygame.K_SEMICOLON: "d6", pygame.K_SLASH: "d6#",
    pygame.K_MINUS: "e6", pygame.K_LEFTBRACKET: "f6", pygame.K_QUOTE: "f6#",
    pygame.K_RSHIFT: "g6", pygame.K_EQUALS: "g6#", pygame.K_RIGHTBRACKET: "a7",
    pygame.K_RETURN: "a7#", pygame.K_BACKSPACE: "b7", pygame.K_BACKSLASH: "c7"
}

# Load sounds
sounds = {}
for key, note in key_note_map.items():
    try:
        sounds[key] = pygame.mixer.Sound(f"sounds/{note}.wav")
    except pygame.error:
        print(f"Warning: Missing sound file for {note}")

# Set up display
WIDTH, HEIGHT = 800, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Keyboard Piano")
font = pygame.font.Font(None, 24)

sustain = False
pressed_keys = set()

# Keyboard layout
def draw_keyboard():
    screen.fill((0, 0, 0))  # Black background
    white_keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
                  pygame.K_8, pygame.K_9, pygame.K_0, pygame.K_MINUS, pygame.K_EQUALS]
    black_keys = [pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_t, pygame.K_y, pygame.K_u,
                  pygame.K_i, pygame.K_o, pygame.K_p, pygame.K_LEFTBRACKET, pygame.K_RIGHTBRACKET]
    key_width = WIDTH // len(white_keys)
    black_key_width = key_width // 2
    
    # Draw white keys
    for i, key in enumerate(white_keys):
        rect = pygame.Rect(i * key_width, 100, key_width, 150)
        pygame.draw.rect(screen, (255, 255, 255), rect, 0 if key in pressed_keys else 2)
        text = font.render(key_note_map.get(key, ""), True, (0, 0, 0))
        screen.blit(text, (i * key_width + 10, 230))
    
    # Draw black keys
    for i, key in enumerate(black_keys):
        if i % 7 not in [2, 6]:  # Skip non-existent black keys
            rect = pygame.Rect(i * key_width + (3 * black_key_width // 4), 100, black_key_width, 100)
            pygame.draw.rect(screen, (0, 0, 0), rect, 0 if key in pressed_keys else 2)
            text = font.render(key_note_map.get(key, ""), True, (255, 255, 255))
            screen.blit(text, (i * key_width + (3 * black_key_width // 4) + 5, 120))

running = True
while running:
    # draw_keyboard()
    text = font.render("Press keys to play notes", True, (255, 255, 255))
    screen.blit(text, (20, 50))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                sustain = True
            elif event.key in sounds:
                sounds[event.key].play()
                pressed_keys.add(event.key)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_TAB:
                sustain = False
                for key in pressed_keys:
                    sounds[key].stop()
                pressed_keys.clear()
            elif event.key in sounds and not sustain:
                sounds[event.key].stop()
                if event.key in pressed_keys:
                    pressed_keys.remove(event.key)

    pygame.display.flip()

pygame.quit()
sys.exit()
