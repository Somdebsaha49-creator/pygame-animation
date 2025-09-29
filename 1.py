import pygame
pygame.init()
screen=pygame.display.set_mode((700,700))
clock=pygame.time.Clock()
circle_x=90
circle_y=250
circle_speed_y=5
rectangle_x=60
rectangle_y=240
rectangle_speed_x=5
running=True
circles_x=610
circles_y=250
circles_speed_y=5
while running:
    screen.fill((0, 0, 255))
    pygame.draw.circle(screen,(255, 165, 0),(circle_x,circle_y),70)
    pygame.draw.rect(screen,(198, 134, 66),(rectangle_x,rectangle_y,140,70))
    pygame.draw.circle(screen,(255,0,0),(circles_x,circles_y),70)
    circle_y+=circle_speed_y
    if circle_y>630 or circle_y<70:
        circle_speed_y*=-1
    rectangle_x+=rectangle_speed_x
    if rectangle_x>460 or rectangle_x<0:
        rectangle_speed_x*=-1
    circles_y+=circles_speed_y
    if circles_y>630 or circles_y<70:
        circles_speed_y*=-1
    pygame.display.flip()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()