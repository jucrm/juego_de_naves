#Código hecho por Juan Camilo Rodríguez Montes 
import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Naves")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 30)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 50)
        self.rect.y = random.randint(-100, -40)

    def update(self):
        self.rect.y += 5  # Mover hacia abajo
        if self.rect.top > HEIGHT:  # Si el enemigo sale de la pantalla
            self.rect.x = random.randint(0, WIDTH - 50)
            self.rect.y = random.randint(-100, -40)

def check_collisions(player, enemies):
    if pygame.sprite.spritecollide(player, enemies, False):
        print("¡Colisión! Fin del juego 😭.")
        pygame.quit()
        sys.exit()

def main():
    player = Player()
    enemies = pygame.sprite.Group()


    for _ in range(5):
        enemy = Enemy()
        enemies.add(enemy)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(enemies)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        all_sprites.update()  
        check_collisions(player, enemies) 

        screen.fill(BLACK)  
        all_sprites.draw(screen)  
        pygame.display.flip()  
        clock.tick(60)  

if __name__ == "__main__":
    main()
