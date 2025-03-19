import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('My first game screen')

image = pygame.image.load('image.jpg')

background_color = (58, 58, 58)
image_rect = image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2-30))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)
    screen.blit(image, image_rect)
    pygame.display.flip()

pygame.quit()