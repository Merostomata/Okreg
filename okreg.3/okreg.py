from turtle import *
from time import time
from time import sleep


class coord:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

'''_________________________________________________________________________________________________________'''
def cell_display(x,y):
    global world
    global player_place
    global screen_size
    
    block_size = screen_size/max( len(world), len(world[0]) )
    
    up()
    goto(x*block_size, y*block_size)# ustawienie żółwia w miejscu startowym dla danego kwadracika
    down()  

    if (player_place.y == y and player_place.x == x):
        fillcolor("blue")# czarny - 1, zielony - 0, niebieski - gracz
    else:
        if(world[len(world)-2-y][x] == "0"):
            fillcolor("green")
        else:
            fillcolor("black")

    begin_fill()  
    for g in range (4):# kwadracik
        seth(g*90)
        fd(block_size)
    end_fill()


def game_display(whole_screen):
    global world
    global player_place
    global players_old_place
    tracer(0)
    ht()

    if whole_screen == True:
        for y in range(len(world)):
            for x in range(len(world[y])-1):
                cell_display(x, y)
    else:
        if(players_old_place != player_place):
            cell_display(player_place.x, player_place.y)
            cell_display(players_old_place.x, players_old_place.y)        
    tracer(1)
    
'''_________________________________________________________________________________________________________'''

def w():
    global recent_input
    recent_input = 'w'
def a():
    global recent_input
    recent_input = 'a'
def s():
    global recent_input
    recent_input = 's'
def d():
    global recent_input
    recent_input = 'd'
    
def game_input ():
    listen(xdummy=None, ydummy=None)
    onkey(w, "w")
    onkey(a, "a")
    onkey(s, "s")
    onkey(d, "d")

'''_________________________________________________________________________________________________________'''

def can_I_move_here (player_place):
    global world
    if player_place.y < 0:
        return False
    if player_place.x < 0:
        return False
    if player_place.y >= len(world):
        return False
    if player_place.x >= len(world[player_place.y]):
        return False
    if world[len(world)-2-player_place.y][player_place.x] != "0":
        return False
        
    



def game_update ():
    global recent_input
    global player_place
    global players_old_place

    
    players_old_place.y = player_place.y
    players_old_place.x = player_place.x
    
    
    if recent_input == 'w':
        player_place.y += 1
    if recent_input == 's':
        player_place.y -= 1
    if recent_input == 'a':
        player_place.x -= 1
    if recent_input == 'd':
        player_place.x += 1

    if can_I_move_here(player_place) == False:
        player_place.y = players_old_place.y
        player_place.x = players_old_place.x
    recent_input = '4'

'''_________________________________________________________________________________________________________'''

screen_size = 200  
world = (open("okreg_world.txt.txt", "r").readlines())
player_place = coord(0, 0)
players_old_place = coord(0, 0)
fps_max = (1/30)
recent_input = '4'

clock_last_call = time()#funkcja diagnostyczna
def clock ():
    global clock_last_call
    print(time() - clock_last_call)
    clock_last_call = time()



game_display(whole_screen = True)
while True:
    last_frame_time = time()
   # print('d')#################################    Z clock() wynika, że to display zajmuje najwięcej czasu (aż do 0.5s). Trzeba zrobić tak, żeby rysował od nowa tylko zmieniające się elementy.
    #clock()
    game_input()
   # print('i')
   # clock()
    game_update()

    game_display(whole_screen = False)
#    print('u')
   # clock()
    sleep(max(fps_max - (time() - last_frame_time),0))
