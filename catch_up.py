from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, width=70, height=70):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 435:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed

window = display.set_mode((700, 500))
window.fill((10, 10, 10))
clock = time.Clock()

racket_1 = Player('platform_v.png', 25, 150, 3, 20, 80)
racket_2 = Player('platform_v.png', 650, 150, 3, 20, 80)

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill((10, 10, 10))
        racket_1.update_l()
        racket_2.update_r()
        racket_1.reset()
        racket_2.reset()

    display.update()
    clock.tick(60)