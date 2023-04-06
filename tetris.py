import os, time, keyboard

line = 0
column = 0


def create_play_area():
    """
    Create the area where the game will be played
    """
    global play_area
    play_area = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        ]

def show_play_area():
    """
    Print the play area on the terminal/shell
    """
    for i in play_area:
        for j in i:
            if j == 0:
                print(" * ", end="")
            if j == 1:
                print("[ ]", end="")          
        print("")
    

def update_play_area(line):
    """
    Verify the current line, to update de play_area
    """
    if line <= 9:
        del play_area[line][column]
        play_area[line].insert(column, 1)
    
def move_block(column):
    """
    Move the 'block' based on the keys
    """
    col = column
    if keyboard.is_pressed("right") and col < len(play_area[0]) - 1:
        col += 1
        
    elif keyboard.is_pressed("left") and col > 0:
        col -= 1
        
    return col
    
def reset_play_area(line):
    """
    Clean the terminal to update with new params
    """
    lin = line
    time.sleep(0.3)
    os.system("clear")
    lin += 1
    return lin
    
while True:
    create_play_area()
    
    update_play_area(line)
    
    show_play_area()
    
    column = move_block(column)
    print(f"Linha: {line}")
    print(f"Coluna: {column}")
    
    print(play_area)
    
    line = reset_play_area(line)
    