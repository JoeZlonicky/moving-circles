import pygame
import math

SCREEN_SIZE = (700, 700)
CENTER = (350, 350)
BG_COLOUR = (0, 0, 0)
LINE_COLOUR = (64, 64, 64)
MAX_N = 8
LINE_RADIUS = 300
CIRCLE_SIZE = 20
SPEED = 1
FPS = 60

def main():
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    n = 1
    delta = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    n = min(MAX_N, n + 1)
                elif event.key == pygame.K_s:
                    n = max(1, n - 1)
        screen.fill(BG_COLOUR)

        # Draw lines
        theta = 0.0
        for i in range(2**(n-1)):
            start_x = math.cos(theta) * LINE_RADIUS + CENTER[0]
            end_x = -math.cos(theta) * LINE_RADIUS + CENTER[0]
            start_y = math.sin(theta) * LINE_RADIUS + CENTER[1]
            end_y = -math.sin(theta) * LINE_RADIUS + CENTER[1]
            pygame.draw.line(screen, LINE_COLOUR, (start_x, start_y), (end_x, end_y))

            theta += math.pi /(2**(n-1))

        # Draw circles
        theta = 0.0
        for i in range(2**(n-1)):
            r = math.sin(delta * SPEED / 1000 + theta)
            x = r * math.cos(theta) * LINE_RADIUS + CENTER[0]
            y = r * math.sin(theta) * LINE_RADIUS + CENTER[1]
            color = calculate_color(math.degrees(theta * 2))
            pygame.draw.circle(screen, color, (int(x), int(y)), CIRCLE_SIZE)

            theta +=  math.pi / (2**(n-1))
        
        # Update display, handle fps, and update delta
        pygame.display.flip()
        delta += clock.tick(60)


# Return a rgb based on a value between 0 and 360
def calculate_color(val):
    val %= 360
    r = g = b = 0

    if val <= 120:
        r = min(255, 510 - 255 * val / 60)
        g = min(255, 255 * val / 60)
    elif val <= 240:
        offsetted = val - 120
        g = min(255, 510 - 255 * offsetted / 60)
        b = min(255, 255 * offsetted / 60)
    else:
        offsetted = val - 240
        r = min(255, 255 * offsetted / 60)
        b = min(255, 510 - 255 * offsetted / 60)
    return (r, g, b)


if __name__ == "__main__":
    main()
