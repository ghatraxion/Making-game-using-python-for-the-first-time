import pygame
import sys

pygame.init()

layar = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Rotated rectangle!")

# warna
putih = (255, 255, 255)
merah = (255, 0, 0)

# biar gerak
x, y = 200, 150
angle = 0
speed = 5

# karakter
asli = pygame.Surface((40, 40), pygame.SRCALPHA)
pygame.draw.rect(asli, merah, (0, 0, 40, 40))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
        angle += 10
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
        angle -= 10
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= speed
        angle -= 10
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed
        angle += 10
    
    # jarak
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x > layar.get_width() - 40:
        x = layar.get_width() - 40
    if y > layar.get_height() - 40:
        y = layar.get_height() - 40
    
    rotated = pygame.transform.rotate(asli, angle)
    rect = rotated.get_rect(center=(x+20, y+20))
    
    layar.fill(putih)
    layar.blit(rotated, rect)
    pygame.display.flip()

    pygame.time.Clock().tick(60)