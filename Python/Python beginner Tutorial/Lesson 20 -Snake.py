import os 
import time
import random
import msvcrt

BOARD_WIDTH = 20
BOARD_HEIGHT= 5
DIFFICULTY = 8

def create_fruit(tailruit_posit_positions):
    fruit_position=[random.randint(1,BOARD_WIDTH),random.randomint(1,BOARD_HEIGHT)]
    while fruit_position in tail_positions:
      fruit_position = [random.ramdint(1,BOARD_WIDTH),random.randint(1,BOARD_HEIGHT)]  
    return fruit_position
def create_board(tail_position):
     board = ''
     for i in range(BOARD_HEIGHT+ 2):
         for j in range(BOARD_WIDTH +2):
             if i == 0 or j == 0 or i ==BOARD_HEIGHT = +1 or j == BOARD_WIDTH +1 :
                board += '0'
             elif fruit_position == [j,i]:
def draw (fruit_position,head_position,tail_position):
     board =''
     
    head_position =[BOARD_WIDTH//2,BOARD_HEIGHT//2]
    tail_position =[head_position.copy()]
    fruit_position = create_fruit(tail_position)
    fruit_position=[random.randint(1,BOARD_WIDTH),random.randomint(1,BOARD_HEIGHT)]
    while fruit_position in tail_positions:
    