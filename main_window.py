import pygame
import pygame_gui


class Labyrinth:

    def __init__(self, filename, partnersname, chestsname, free_tiles, finish_tile):
        self.map = []
        with open(f"{MAPS_DIR}/{filename}") as input_file:
            for line in input_file:
                self.map.append(list(map(int, line.split())))
        # получение списка полей карты
        self.map_partners = []
        with open(f"{MAPS_DIR}/{partnersname}") as input_file_2:
            for line in input_file_2:
                self.map_partners.append(list(map(int, line.split())))
        # получение списка врагов на карте
        self.map_chests = []
        self.map_chests = chests(chestsname)
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.tile_size = TILE_SIZE
        self.free_tiles = free_tiles
        self.finish_tile = finish_tile

    def render(self, screen):
        colors = {0: (0, 0, 0), 1: (120, 120, 120), 2: (50, 50, 50)}
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * self.tile_size + 100, y * self.tile_size + 50,
                                   self.tile_size, self.tile_size)
                screen.fill(colors[self.get_tile_id((x, y))], rect)
        # отрисовка полей поля
        for i in range(len(self.map_partners)):
            height_partner = self.map_partners[i][0]
            width_partner = self.map_partners[i][1]
            partner = height_partner * self.tile_size + TILE_SIZE // 2 + 100,\
                      width_partner * self.tile_size + TILE_SIZE // 2 + 50
            pygame.draw.circle(screen, (0, 255, 0), partner, TILE_SIZE // 2 - 1)

        # отрисовка врагов
        for i in range(len(self.map_chests)):
            rect = pygame.Rect(self.map_chests[i][0] * TILE_SIZE + 101, self.map_chests[i][1] * TILE_SIZE + 51,
                               TILE_SIZE - 2, TILE_SIZE - 2)
            screen.fill((200, 200, 200), rect)
        # отрисовка сундуков

    def get_tile_id(self, position):
        return self.map[position[1]][position[0]]

    def is_free(self, position):
        return self.get_tile_id(position) in self.free_tiles
    # проверка можно ли двигаться

    def returning(self):
        return self.map_partners_2

    def fight(self, position, screen):
        global k
        self.x, self.y = position
        self.screen = screen

        rect = pygame.Rect(self.x * self.tile_size + 100, self.y * self.tile_size + 50,
                           self.tile_size, self.tile_size)
        self.screen.fill((50, 50, 50), rect)
        for i in range(len(self.map_partners)):
            if self.map_partners[i][0] == self.x and self.map_partners[i][1] == self.y:
                self.map_partners[i] = [-10000, -100000, self.map_partners[i][2]]
        # удаление сундуков и врагов с карты

class Labyrinth4:

    def __init__(self, filename, partnersname, chestsname, free_tiles, finish_tile):
        self.map = []
        with open(f"{MAPS_DIR}/{filename}") as input_file:
            for line in input_file:
                self.map.append(list(map(int, line.split())))
        # получение списка полей карты
        self.map_partners = []
        with open(f"{MAPS_DIR}/{partnersname}") as input_file_2:
            for line in input_file_2:
                self.map_partners.append(list(map(int, line.split())))
        # получение списка врагов на карте
        self.map_chests = []
        self.map_chests = chests(chestsname)
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.tile_size = TILE_SIZE
        self.free_tiles = free_tiles
        self.finish_tile = finish_tile

    def render(self, screen):
        colors = {0: (0, 0, 0), 1: (0, 128, 0), 2: (50, 50, 50)}
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * self.tile_size + 100, y * self.tile_size + 50,
                                   self.tile_size, self.tile_size)
                screen.fill(colors[self.get_tile_id((x, y))], rect)
        # отрисовка полей поля
        for i in range(len(self.map_partners)):
            height_partner = self.map_partners[i][0]
            width_partner = self.map_partners[i][1]
            partner = height_partner * self.tile_size + TILE_SIZE // 2 + 100,\
                      width_partner * self.tile_size + TILE_SIZE // 2 + 50
            pygame.draw.circle(screen, (0, 255, 0), partner, TILE_SIZE // 2 - 1)

        # отрисовка врагов
        for i in range(len(self.map_chests)):
            rect = pygame.Rect(self.map_chests[i][0] * TILE_SIZE + 101, self.map_chests[i][1] * TILE_SIZE + 51,
                               TILE_SIZE - 2, TILE_SIZE - 2)
            screen.fill((200, 200, 200), rect)
        # отрисовка сундуков

    def get_tile_id(self, position):
        return self.map[position[1]][position[0]]

    def is_free(self, position):
        return self.get_tile_id(position) in self.free_tiles
    # проверка можно ли двигаться

    def returning(self):
        return self.map_partners_2

    def fight(self, position, screen):
        global k
        self.x, self.y = position
        self.screen = screen

        rect = pygame.Rect(self.x * self.tile_size + 100, self.y * self.tile_size + 50,
                           self.tile_size, self.tile_size)
        self.screen.fill((50, 50, 50), rect)
        for i in range(len(self.map_partners)):
            if self.map_partners[i][0] == self.x and self.map_partners[i][1] == self.y:
                self.map_partners[i] = [-10000, -100000, self.map_partners[i][2]]
        # удаление сундуков и врагов с карты

class Labyrinth4:
    def __init__(self, filename, free_tiles, finish_tile):
        self.map = []
        with open(f"{MAPS_DIR}/{filename}") as input_file:
            for line in input_file:
                self.map.append(list(map(int, line.split())))
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.tile_size = TILE_SIZE
        self.free_tiles = free_tiles
        self.finish_tile = finish_tile

    def render(self, screen):
        colors = {0: (0, 0, 0), 1: (0, 128, 0), 2: (50, 50, 50)}
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * self.tile_size, y * self.tile_size,
                                   self.tile_size, self.tile_size)
                screen.fill(colors[self.get_tile_id((x, y))], rect)

    def get_tile_id(self, position):
        return self.map[position[1]][position[0]]

    def is_free(self, position):
        return self.get_tile_id(position) in self.free_tiles

class Hero:
    def __init__(self, pic, position):
        self.x, self.y = position
        self.image = pygame.image.load(f"images/{pic}")

    def get_position(self):
        global labyrinth, hero, game
        global screen, num_level
        self.image = pygame.image.load(f"images/hero.png")
        if self.x == 9 and self.y == 0 and num_level == 1:
            labyrinth = Labyrinth2("simple_map2.txt", [0, 2], 2)
            hero = Hero("hero.png", (7, 6))
            game = Game(labyrinth, hero)
            game.update_hero()
            screen.fill((0, 0, 0))
            game.render(screen)
            pygame.display.flip()
            num_level = 2
        if self.x == 6 and self.y == 7 and num_level == 2:
            labyrinth = Labyrinth3("simple_map3.txt", [0, 2], 2)
            hero = Hero("hero.png", (7, 6))
            game = Game(labyrinth, hero)
            game.update_hero()
            screen.fill((0, 0, 0))
            game.render(screen)
            pygame.display.flip()
            num_level = 3
        if self.x == 7 and self.y == 1 and num_level == 3:
            labyrinth = Labyrinth4("simple_map4.txt", [0, 2], 2)
            hero = Hero("hero.png", (7, 6))
            game = Game(labyrinth, hero)
            game.update_hero()
            screen.fill((0, 0, 0))
            game.render(screen)
            pygame.display.flip()
            num_level = 4
        if self.x == 2 and self.y == 2 and num_level == 4:
            num_level = 5
        return self.x, self.y

    def set_position(self, position):
        self.x, self.y = position

    def render(self, screen):
        delta = (self.image.get_width() - TILE_SIZE) // 2
        screen.blit(self.image, (self.x * TILE_SIZE - delta, self.y * TILE_SIZE - delta))

class Game:
    def __init__(self, labyrinth, hero):
        self.labyrinth = labyrinth
        self.hero = hero

    def render(self, screen):
        self.labyrinth.render(screen)
        self.hero.render(screen)

    def update_hero(self):
        next_x, next_y = self.hero.get_position()
        if pygame.key.get_pressed()[pygame.K_a]:
            next_x -= 1
        if pygame.key.get_pressed()[pygame.K_d]:
            next_x += 1
        if pygame.key.get_pressed()[pygame.K_w]:
            next_y -= 1
        if pygame.key.get_pressed()[pygame.K_s]:
            next_y += 1
        if self.labyrinth.is_free((next_x, next_y)):
            self.hero.set_position((next_x, next_y))


pygame.init()

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 480, 380
FPS = 7
MAPS_DIR = "maps"
TILE_SIZE = 32

num_level = 1

NAME = ''

pygame.display.set_caption('Start')
window_surface = pygame.display.set_mode((800, 600))
# создание окна

background = pygame.Surface((800, 600))
# вторая поверхность

color = (125, 116, 109)

background.fill(pygame.Color(color))
# заливка окна

manager = pygame_gui.UIManager((800, 600))
# менеджер для кнопок

button_start = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 200), (100, 50)),
    # расположение кнопки и её размеры
    text='Play',
    manager=manager
)
# кнопка для начала игры



clock = pygame.time.Clock()
# часы до основного цикла программы
run = True

screen = ""

labyrinth = Labyrinth("simple_map.txt", [0, 2], 2)
hero = Hero("hero.png", (7, 6))
game = Game(labyrinth, hero)

def main():
    global screen
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if num_level == 5:
            screen.fill('black')
            font = pygame.font.Font(None, 50)
            text = font.render("The end!", True, 'white')
            text_x = 480 // 2 - text.get_width() // 2
            text_y = 380 // 2 - text.get_height() // 2
            screen.blit(text, (text_x, text_y))
            pygame.display.flip()
        else:
            game.update_hero()
            screen.fill((0, 0, 0))
            game.render(screen)
            pygame.display.flip()
            clock.tick(FPS)
    pygame.quit()
# запуск программы


while run:
    time_delta = clock.tick(60) / 1000.0
    # таймер для элементов пользовательского интерфейса
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            confirmation_dialog = pygame_gui.windows.UIConfirmationDialog(
                rect=pygame.Rect((250, 200), (300, 200)),
                manager=manager,
                window_title='Подтверждение',
                action_long_desc='Вы уверены, что  хотите выйти?',
                action_short_name='OK',
                blocking=True
            )
            # попытка выхода из игры
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                run = False
                # подтверждение выхода из игры
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_start:
                        main()

        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    # отрисовка поверхности background поверх главной window_surface
    manager.draw_ui(window_surface)
    pygame.display.update()
