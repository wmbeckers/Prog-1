import pygame
import random
from pygame.locals import *

pygame.init()

try:
    pygame.mixer.music.load('SF64SWSU.ogg')
    pygame.mixer.music.play(-1)
except pygame.error as e:
    print(f"Erro ao carregar a música: {e}")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        try:
            imagem_nave = pygame.image.load('Player.png').convert_alpha()
            self.surf = pygame.transform.scale(imagem_nave, (105, 42))
            self.rect = self.surf.get_rect()
        except pygame.error as e:
            print(f"Erro ao carregar a imagem do jogador: {e}")

    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_a]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(1, 0)
        self.rect.clamp_ip(pygame.Rect(0, 0, 1000, 800))

    def shoot(self):
        bullet = Bullet(self.rect.right, self.rect.centery)
        bullets.add(bullet)
        all_sprites.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed_multiplier):
        super(Enemy, self).__init__()
        try:
            original_image = pygame.image.load('Asteroid.png').convert_alpha()
            self.surf = pygame.transform.scale(original_image, (80, 80))
            self.rect = self.surf.get_rect(center=(random.randint(1020, 1100), random.randint(0, 800)))
            self.speed = random.uniform(1, 2) * speed_multiplier
        except pygame.error as e:
            print(f"Erro ao carregar a imagem do inimigo: {e}")

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            global score
            score += 100

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        try:
            shot_image = pygame.image.load('Shot.png').convert_alpha()
            self.surf = pygame.transform.scale(shot_image, (int(shot_image.get_width() * 3), int(shot_image.get_height() * 3)))
            self.rect = self.surf.get_rect(center=(x, y))
        except pygame.error as e:
            print(f"Erro ao carregar a imagem do tiro: {e}")

    def update(self):
        self.rect.move_ip(5, 0)
        if self.rect.left > 1000:
            self.kill()

def reset_game():
    global player, enemies, bullets, all_sprites, score, speed_multiplier
    player = Player()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    score = 0
    speed_multiplier = 1.0

screen = pygame.display.set_mode((1000, 800))
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 550)

try:
    background = pygame.image.load('Space Background.png').convert_alpha()
except pygame.error as e:
    print(f"Erro ao carregar a imagem de fundo: {e}")

score = 0
high_score = 0
try:
    font = pygame.font.Font('Minecraft font.ttf', 36)
except pygame.error as e:
    print(f"Erro ao carregar a fonte: {e}")

running = True
game_active = True
speed_multiplier = 1.0

reset_game()

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_SPACE and game_active:
                player.shoot()
            elif event.key == K_r and not game_active:
                reset_game()
                game_active = True
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY and game_active:
            new_enemy = Enemy(speed_multiplier)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    if game_active:
        screen.blit(background, (0, 0))
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()
        bullets.update()

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        for bullet in bullets:
            hit_enemies = pygame.sprite.spritecollide(bullet, enemies, True)
            for enemy in hit_enemies:
                bullet.kill()
                score += 100

        if pygame.sprite.spritecollideany(player, enemies):
            game_active = False
            if score > high_score:
                high_score = score

        if score % 2500 == 0 and score != 0:
            speed_multiplier += 0.5
            score += 1

        score_surf = font.render(f'Score: {score}', True, (255, 255, 255))
        score_rect = score_surf.get_rect(topright=(screen.get_width() - 10, 10))
        screen.blit(score_surf, score_rect)

        high_score_surf = font.render(f'High Score: {high_score}', True, (255, 255, 255))
        high_score_rect = high_score_surf.get_rect(topright=(screen.get_width() - 10, 40))
        screen.blit(high_score_surf, high_score_rect)

        pygame.display.flip()
    else:
        screen.fill((0, 0, 0))
        game_over_surf = font.render('Game Over!', True, (255, 255, 255))
        game_over_rect = game_over_surf.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 50))
        screen.blit(game_over_surf, game_over_rect)

        restart_surf = font.render('Press R to Restart', True, (255, 255, 255))
        restart_rect = restart_surf.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        screen.blit(restart_surf, restart_rect)

        final_score_surf = font.render(f'Final Score: {score}', True, (255, 255, 255))
        final_score_rect = final_score_surf.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 50))
        screen.blit(final_score_surf, final_score_rect)

        high_score_surf = font.render(f'High Score: {high_score}', True, (255, 255, 255))
        high_score_rect = high_score_surf.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 100))
        screen.blit(high_score_surf, high_score_rect)

        pygame.display.flip()

pygame.quit()