import pygame
import math


class Application:
    """ Draws lines and circles to the screen that creates a cool effect.
            Press w/s to increase or decrease the number of circles, respectively. """
    SCREEN_SIZE = (700, 700)
    CENTER = (350, 350)
    BG_COLOUR = (0, 0, 0)
    LINE_COLOUR = (64, 64, 64)
    MAX_N = 8
    LINE_RADIUS = 300
    CIRCLE_SIZE = 20
    SPEED = 1
    FPS = 60

    def __init__(self):
        """ Create a new application """
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        pygame.display.set_caption("Moving Circles")
        self.clock = pygame.time.Clock()
        self.n = 1
        self.delta = 0
        self.running = True
        self.loop()

    def loop(self):
        """ Handle events and draw to screen """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.n = min(self.MAX_N, self.n + 1)
                    elif event.key == pygame.K_s:
                        self.n = max(1, self.n - 1)
            self.screen.fill(self.BG_COLOUR)
            self.draw_lines()
            self.draw_circles()  
            pygame.display.flip()
            self.delta += self.clock.tick(self.FPS)

    def draw_lines(self):
        """ Draw background lines """
        theta = 0.0
        print(2**(self.n - 1))
        for _ in range(2**(self.n - 1)):
            start_x = int(math.cos(theta) * self.LINE_RADIUS + self.CENTER[0])
            end_x = int(-math.cos(theta) * self.LINE_RADIUS + self.CENTER[0])
            start_y = int(math.sin(theta) * self.LINE_RADIUS + self.CENTER[1])
            end_y = int(-math.sin(theta) * self.LINE_RADIUS + self.CENTER[1])
            pygame.draw.line(self.screen, self.LINE_COLOUR, (start_x, start_y), (end_x, end_y))

            theta += math.pi /(2**(self.n - 1))

    def draw_circles(self):
        """ Draw the moving circles """
        theta = 0.0
        for _ in range(2**(self.n - 1)):
            r = math.sin(self.delta * self.SPEED / 1000 + theta)
            x = int(r * math.cos(theta) * self.LINE_RADIUS + self.CENTER[0])
            y = int(r * math.sin(theta) * self.LINE_RADIUS + self.CENTER[1])
            color = self.calculate_color(math.degrees(theta * 2))
            pygame.draw.circle(self.screen, color, (int(x), int(y)), self.CIRCLE_SIZE)

            theta +=  math.pi / (2**(self.n - 1))

    def calculate_color(self, val):
        """ Return a (r, g, b) based on a value between 0 and 360 """
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
    Application()
