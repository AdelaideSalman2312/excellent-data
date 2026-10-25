from os import system 


board = '''
 1 # 2 # 3

############
  4 # 5# 6
############
  7 # 8 # 9
  '''
player_X =[]
player_O =[]
winning_combinations = ([1,2,3],[4,5,6],[7,8,9]
                        [1,4,7],[2,5,8][3,6,9]
                        [1,5,9],[3,5,7])
player_X_won = False
player_O_won = False
for i in range(9):
    system('cls||clear')
    print(board)
    if i % 2== 0:
      player_X.append(input('Select a number'))
      board = board.replace(player_X[-1],'X') 
      for combinations in winning_combinations:
        count=0
        for j in range(3):
          if str(combinations[j]) in player_X:
            count+=1
        if count == 3:
          player_X_won = True
          system('cls||clear')
          print(board)
          print('player_X_won!')
          break
        if player_X_won:
          break
    else:
      player_O.append(input('Select a number:'))
      board = board.replace(player_O[-1],'o')



#Needs a second thought to play the game



