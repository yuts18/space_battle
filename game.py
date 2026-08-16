import pygame
import sys
from pygame.color import THECOLORS
pygame.init()

screen = pygame.display.set_mode((1200,800))
screen.fill(THECOLORS['black'])
r = pygame.Rect(500,500,200,100)
#e = pygame.Rect(250,250,100,200)
pygame.draw.rect(screen,(255,150,0),r,0)
pygame.draw.polygon(screen,(150,255,68),[(500,700),(700,600),(500,400),],0)

#font = pygame.font.SysFont('couriernew', 40)
#text = font.render(str('HELLO'),True,THECOLORS['green'])
#screen.blit(text,(50,50))
#pygame.draw.circle(screen,(255,255,0),(150,150), 75)
#pygame.draw.line(screen,(0,255,255),(250,250),(500,500),1)
#pygame.draw.ellipse(screen,(100,100,55), e, 0)
#pygame.draw.polygon(screen,(150,255,68),((600,10),(400,250),(300,250),(10,200)),0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
           