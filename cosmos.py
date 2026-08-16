import pygame,controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Score


def run():
    pygame.init()
    screen = pygame.display.set_mode((700,800))
    pygame.display.set_caption("Space Batle")
    bg_color = (0,0,0)

    gun = Gun(screen)
    bullets = Group()
    alliens = Group()
    controls.create_army(screen,alliens)
    stats = Stats()
    sc = Score(screen,stats)


    while True:
        controls.events(screen,gun,bullets)
        if stats.run_game:

            gun.updateLocation()
            controls.update(bg_color,screen,stats, sc, gun,alliens,bullets)
            controls.update_bullets(screen,stats,sc,alliens,bullets)
            controls.update_alliens(stats, screen,sc, gun,alliens,bullets)
run()