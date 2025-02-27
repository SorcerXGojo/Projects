import pygame
import time
import random

pygame.font.init()  

WIDTH, HEIGHT = 800, 600  
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("Space Dodge")  

BG = pygame.transform.scale(pygame.image.load("Background.jpeg"), (WIDTH, HEIGHT))
CHARACTER = pygame.transform.scale(pygame.image.load("Space_Ship.png"), (50, 60))  

PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60  

FONT = pygame.font.SysFont("comicsans", 30)  


class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.SysFont("comicsans", 40)

    def draw(self, win):
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.rect(win, self.hover_color if self.rect.collidepoint(mouse_pos) else self.color, self.rect)

        text_render = self.font.render(self.text, True, (255, 255, 255))
        text_x = self.rect.x + (self.rect.width - text_render.get_width()) // 2  
        text_y = self.rect.y + (self.rect.height - text_render.get_height()) // 2  
        win.blit(text_render, (text_x, text_y))

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)


def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))  

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, (255, 255, 255))
    WIN.blit(time_text, (10, 10))

    WIN.blit(CHARACTER, (player.x, player.y))

    for star in stars:
        pygame.draw.rect(WIN, (0, 255, 0), star)

    pygame.display.update()  


def main(player_vel, star_vel, star_count):
    run = True  
    FPS = 60  
    clock = pygame.time.Clock()  
    start_time = time.time()  
    elapsed_time = 0  

    star_add_increment = 2000  
    star_timer = 0  
    stars = []  
    hit = False  

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    while run:  
        star_timer += clock.tick(FPS)  
        elapsed_time = time.time() - start_time  

        if star_timer > star_add_increment:
            for _ in range(star_count):  
                star_x = random.randint(0, WIDTH - 10)  
                star = pygame.Rect(star_x, -20, 10, 20)  
                stars.append(star)  

            star_add_increment = max(200, star_add_increment - 50)  
            star_timer = 0  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                run = False  
                break  

        keys = pygame.key.get_pressed()  
        if keys[pygame.K_LEFT] and player.x - player_vel >= 0:  
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.width <= WIDTH:  
            player.x += player_vel

        for star in stars[:]:  
            star.y += star_vel  
            if star.y > HEIGHT:  
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):  
                stars.remove(star)  
                hit = True  
                break  

        if hit:  
            lost_text = FONT.render("You Lost!", 1, (255, 255, 255))  
            WIN.blit(lost_text, (WIDTH//2 - lost_text.get_width()//2, HEIGHT//2 - lost_text.get_height()//2))  
            pygame.display.update()  
            pygame.time.delay(2000)  
            start_screen()
            return  

        draw(player, elapsed_time, stars)  

    pygame.quit()  


def level_selection():
    button_width, button_height = 200, 60  
    button_x = (WIDTH - button_width) // 2  

    easy_button = Button(button_x, HEIGHT // 3, button_width, button_height, "Easy", (0, 255, 0), (50, 205, 50))
    medium_button = Button(button_x, HEIGHT // 2, button_width, button_height, "Medium", (255, 165, 0), (255, 140, 0))
    hard_button = Button(button_x, (HEIGHT // 3) * 2, button_width, button_height, "Hard", (255, 0, 0), (178, 34, 34))

    while True:
        WIN.blit(BG, (0, 0))  
        easy_button.draw(WIN)  
        medium_button.draw(WIN)  
        hard_button.draw(WIN)  
        pygame.display.update()  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  
            if easy_button.is_clicked(event):  
                main(player_vel=7, star_vel=3, star_count=3)  
                return  
            if medium_button.is_clicked(event):  
                main(player_vel=6, star_vel=5, star_count=5)  
                return  
            if hard_button.is_clicked(event):  
                main(player_vel=5, star_vel=8, star_count=7)  
                return  


def start_screen():
    button_width, button_height = 200, 60  
    button_x = (WIDTH - button_width) // 2  
    button_y = (HEIGHT - button_height) // 2  

    start_button = Button(button_x, button_y, button_width, button_height, "Start", (0, 128, 255), (0, 180, 255))  

    while True:
        WIN.blit(BG, (0, 0))  
        start_button.draw(WIN)  
        pygame.display.update()  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  
            if start_button.is_clicked(event):  
                level_selection()  
                return  


if __name__ == "__main__":
    start_screen()
