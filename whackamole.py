import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        ranX = 0
        ranY = 0
        molePos = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if x > ranX*32 and x < (ranX+1)*32 and y > ranY*32 and y < (ranY+1)*32:

                        ranX = random.randrange(0,20)
                        ranY = random.randrange(0,16)



            const = 32
            screen.fill("paleturquoise")
            for i in range(1, 20):
                pygame.draw.line(screen, "dark blue", (const * i, 0), (const * i, 512))
            for i in range(1, 17):
                pygame.draw.line(screen, "dark blue", (0, const * i), (640, const * i))
            screen.blit(mole_image, mole_image.get_rect(topleft=(ranX*32, ranY*32)))




            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
