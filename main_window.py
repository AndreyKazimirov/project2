import pygame
import pygame_gui

pygame.init()

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 480, 380
FPS = 7
MAPS_DIR = "maps"
TILE_SIZE = 32

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

button_leaderboard = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 250), (100, 50)),
    text='Leaderboard',
    manager=manager
)

name = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((300, 50), (200, 50)),
    manager=manager
)
# ввод имени игрока

clock = pygame.time.Clock()
# часы до основного цикла программы
run = True

def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    labyrinth = Labyrinth("simple_map.txt", [0, 2], 2)
    hero = Hero((7, 6))
    game = Game(labyrinth, hero)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        game.update_hero()
        screen.fill((0, 0, 0))
        game.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
# запуск программы

def leaderboard():
    leaderboard_window = pygame.Surface((800, 600))
    leaderboard_window.fill(pygame.Color(color))

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
            if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                NAME = event.text
                # имя пользователя
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_start:
                    if NAME == '':
                        continue
                    else:
                        main()
                if event.ui_element == button_leaderboard:
                    leaderboard()

        manager.process_events(event)


    class Labyrinth:

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
            colors = {0: (0, 0, 0), 1: (120, 120, 120), 2: (50, 50, 50)}
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

        def __init__(self, position):
            self.x, self.y = position

        def get_position(self):
            return self.x, self.y

        def set_position(self, position):
            self.x, self.y = position

        def render(self, screen):
            center = self.x * TILE_SIZE + TILE_SIZE // 2, self.y * TILE_SIZE + TILE_SIZE // 2
            pygame.draw.circle(screen, (255, 255, 255), center, TILE_SIZE // 2)


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

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    # отрисовка поверхности background поверх главной window_surface
    manager.draw_ui(window_surface)
    pygame.display.update()