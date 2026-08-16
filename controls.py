import pygame
import sys
from bullet import Bullet
from alien import Allien
import time
def events(screen, gun, bullets):
    # Обработка событий
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type ==pygame.KEYDOWN:
                 if event.key == pygame.K_d:
                      gun.moveRight = True
                 elif event.key == pygame.K_a:
                      gun.moveLeft = True
                 elif event.key == pygame.K_SPACE:
                      new_bullet = Bullet(screen,gun)
                      bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                 if event.key == pygame.K_d:
                      gun.moveRight = False
                 elif event.key == pygame.K_a:
                      gun.moveLeft = False
def update(bg_color, screen,stats, sc, gun,alliens, bullets):
        screen.fill(bg_color)
        sc.show_score()
        for bullet in bullets.sprites():
             bullet.draw_bullet()
        gun.output()
        alliens.draw(screen)
        pygame.display.flip()

def update_bullets(screen,stats,sc ,alliens,bullets):
     bullets.update()
     for bullet in bullets.copy():
          if bullet.rect.bottom <=0:
               bullets.remove(bullet)
     collisions = pygame.sprite.groupcollide(bullets, alliens,True,True)
     if collisions:
          for alliens in collisions.values():

               stats.score +=10 * len(alliens)
               sc.image_score()
               check_hs(stats,sc)
               sc.image_guns()
     if len(alliens) ==0:
          bullets.empty()
          create_army(screen, alliens)

    # print(len(bullets))

def gun_kill(stats,screen,sc, gun,alliens,bullets):
     if stats.guns_left >0:
          stats.guns_left -=1
          sc.image_guns()
          alliens.empty()
          bullets.empty()
          create_army(screen,alliens)
          gun.create_gun()
          time.sleep(1)
     else:
          stats.run_game = False
          sys.exit()

def update_alliens(stats, screen, sc, gun,alliens,bullets):
     alliens.update()
     if pygame.sprite.spritecollideany(gun,alliens):
          gun_kill(stats, screen,sc,  gun,alliens,bullets)
     alliens_chek(stats,screen,sc,gun,alliens,bullets)

def create_army(screen,alliens):
     allien = Allien(screen)
     allien_width = allien.rect.width
     number_allien_x = int((700-2 * allien_width) / allien_width)
     allien_height = allien.rect.height
     number_allien_y = int((800 - 100 -   2* allien_height)/ allien_height)

     for row_number in range(number_allien_y - 1):
        for allien_number in range(number_allien_x):
            allien = Allien(screen)
            allien.x = allien_width + allien_width* allien_number
            allien.y = allien_height + allien_height* row_number
        
            allien.rect.x = allien.x
            allien.rect.y = allien.rect.height +  allien.rect.height * row_number
            alliens.add(allien)

def alliens_chek(stats,screen,sc,gun,alliens,bullets):
    screen_rect = screen.get_rect()
    for allien in alliens.sprites():
         if allien.rect.bottom >= screen_rect.bottom:
              gun_kill(stats,screen, sc,gun,alliens,bullets)
              break
         
def check_hs(stats,sc):
     if stats.score > stats.high_score:
          stats.high_score = stats.score
          sc.image_high_score()
          with open('high_score.txt','w')as f:
               f.write(str(stats.high_score))