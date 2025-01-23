import pygame
import random
from pygame.locals import *

# Inicializa o Pygame
pygame.init()

# Configura a música de fundo
try:
    pygame.mixer.music.load('SF64SWSU.ogg')
    pygame.mixer.music.play(-1)  # -1 faz a música tocar em loop
except pygame.error as e:
    print(f"Erro ao carregar a música: {e}")

# Classe que representa o jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        try:
            # Carrega a imagem da nave do jogador e ajusta o tamanho
            imagem_nave = pygame.image.load('Player.png').convert_alpha()
            self.surf = pygame.transform.scale(imagem_nave, (105, 42))
            self.rect = self.surf.get_rect()
        except pygame.error as e:
            print(f"Erro ao carregar a imagem do jogador: {e}")

    def update(self, pressed_keys):
        # Move a nave do jogador com base nas teclas pressionadas
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_a]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(1, 0)

        # Mantém o jogador dentro dos limites da tela
        self.rect.clamp_ip(pygame.Rect(0, 0, 1000, 800))

    def shoot(self):
        # Cria um novo tiro e o adiciona ao grupo de tiros
        bullet = Bullet(self.rect.right, self.rect.centery)
        bullets.add(bullet)
        all_sprites.add(bullet)

# Classe que representa os inimigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed_multiplier):
        super(Enemy, self).__init__()
        try:
            # Carrega a imagem do inimigo e ajusta o tamanho
            original_image = pygame.image.load('Asteroid.png').convert_alpha()
            self.surf = pygame.transform.scale(original_image, (80, 80))
            # Define a posição inicial do inimigo fora da tela, à direita
            self.rect = self.surf.get_rect(center=(random.randint(1020, 1100), random.randint(0, 800)))
            # Define a velocidade do inimigo
            self.speed = random.uniform(1, 2) * speed_multiplier
        except pygame.error as e:
            print(f"Erro ao carregar a imagem do inimigo: {e}")

    def update(self):
        # Move o inimigo para a esquerda
        self.rect.move_ip(-self.speed, 0)
        # Remove o inimigo se ele sair da tela pela esquerda
        if self.rect.right < 0:
            self.kill()
            global score
            score += 100

# Classe que representa os tiros do jogador
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        try:
            # Carrega a imagem do tiro
            shot_image = pygame.image.load('Shot.png').convert_alpha()
            # Aumenta o tamanho do tiro em 50%
            self.surf = pygame.transform.scale(shot_image, (int(shot_image.get_width() * 3), int(shot_image.get_height() * 3)))
            self.rect = self.surf.get_rect(center=(x, y))
        except pygame.error as e:
            print(f"Erro ao carregar a imagem do tiro: {e}")

    def update(self):
        # Move o tiro para a direita
        self.rect.move_ip(5, 0)
        # Remove o tiro se ele sair da tela
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

# Define o tamanho da janela do jogo
screen = pygame.display.set_mode((1000, 800))
# Cria um evento personalizado para adicionar novos inimigos
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 550)

# Carrega a imagem de fundo
try:
    background = pygame.image.load('Space Background.png').convert_alpha()
except pygame.error as e:
    print(f"Erro ao carregar a imagem de fundo: {e}")

# Inicializa a pontuação
score = 0
high_score = 0
# Carrega a nova fonte
try:
    font = pygame.font.Font('Minecraft font.ttf', 36)
except pygame.error as e:
    print(f"Erro ao carregar a fonte: {e}")

# Variável para controlar o loop principal do jogo
running = True
game_active = True
# Multiplicador de velocidade dos inimigos
speed_multiplier = 1.0

# Função para resetar o jogo
reset_game()

# Loop principal do jogo
while running:
    # Processa eventos
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
            # Adiciona um novo inimigo ao jogo
            new_enemy = Enemy(speed_multiplier)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    if game_active:
        # Desenha o fundo na tela
        screen.blit(background, (0, 0))
        # Obtém as teclas pressionadas
        pressed_keys = pygame.key.get_pressed()
        # Atualiza a posição do jogador
        player.update(pressed_keys)
        # Atualiza a posição dos inimigos
        enemies.update()
        # Atualiza a posição dos tiros
        bullets.update()

        # Desenha todos os sprites na tela
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # Verifica colisões entre os tiros e os inimigos
        for bullet in bullets:
            hit_enemies = pygame.sprite.spritecollide(bullet, enemies, True)
            for enemy in hit_enemies:
                bullet.kill()
                score += 100

        # Verifica colisões entre o jogador e os inimigos
        if pygame.sprite.spritecollideany(player, enemies):
            game_active = False  # Para o jogo
            if score > high_score:
                high_score = score

        # Aumenta a velocidade dos inimigos a cada 2500 pontos
        if score % 2500 == 0 and score != 0:
            speed_multiplier += 0.5
            score += 1  # Para evitar aumentar a velocidade múltiplas vezes na mesma pontuação

        # Renderiza o placar no canto superior direito
        score_surf = font.render(f'Score: {score}', True, (255, 255, 255))
        score_rect = score_surf.get_rect(topright=(screen.get_width() - 10, 10))
        screen.blit(score_surf, score_rect)

        # Renderiza a pontuação mais alta abaixo da pontuação atual
        high_score_surf = font.render(f'High Score: {high_score}', True, (255, 255, 255))
        high_score_rect = high_score_surf.get_rect(topright=(screen.get_width() - 10, 40))  # Ajuste a posição conforme necessário
        screen.blit(high_score_surf, high_score_rect)

        # Atualiza a tela
        pygame.display.flip()
    else:
        # Exibe a tela de Game Over
        screen.fill((0, 0, 0))  # Limpa a tela com preto
        game_over_surf = font.render('Game Over!', True, (255, 255, 255))
        game_over_rect = game_over_surf.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 50))
        screen.blit(game_over_surf, game_over_rect)

        restart_surf = font.render('Press R to Restart', True, (255, 255, 255))
        restart_rect = restart_surf.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        screen.blit(restart_surf, restart_rect)

        # Exibe a pontuação final
        final_score_surf = font.render(f'Final Score: {score}', True, (255, 255, 255))
        final_score_rect = final_score_surf.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 50))
        screen.blit(final_score_surf, final_score_rect)

        # Exibe a pontuação mais alta da sessão
        high_score_surf = font.render(f'High Score: {high_score}', True, (255, 255, 255))
        high_score_rect = high_score_surf.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 100))
        screen.blit(high_score_surf, high_score_rect)

        pygame.display.flip()

# Encerra o Pygame
pygame.quit()