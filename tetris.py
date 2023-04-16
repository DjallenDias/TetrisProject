import os, time, keyboard, random
os.system("clear")

# j - column
# i - row

a = 0
current = 0

def showPlayarea():
    for i in play_area:
        for j in i:
            if j == 0:
                print(" * ", end="")
            if j == 1:
                print("[ ]", end="")          
        print("")
            
def updatePlayarea():
    for item in element[0]:
        line = item[0]
        column = item[1]
        
        del play_area[line][column]
        play_area[line].insert(column, 1)
        

def moveRightLeft():
    way = 0
    for item in element[0]:
        col = item[1]
        
        if keyboard.is_pressed("right") and max(element[0])[1] < len(play_area[0]) - 1:
            col += 1
            
        elif keyboard.is_pressed("left") and min(element[0])[1] > 0 :
            col -= 1
        
        del element[0][way][1]
        element[0][way].insert(1, col)
        way += 1
    
def moveDown():
    way = 0
    for item in element[0]:
        line = item[0]
        del element[0][way][0]
        element[0][way].insert(0, line+1)
        way += 1

def isElementValid():
    try:
        if max(element[0])[0] <= 18:
            return False
        
        else:
            return True
        
    except NameError:
        return True
    
    else:
        return False
    

def choseElement():
    line_element = [[[0,0],[0,1],[0,2],[0,3]], "line"]
    Z_element = [[[0,0],[0,1],[1,1],[1,2]], "Z"]
    square_element = [[[0,0],[0,1],[1,0],[1,1]], "square"]
    L_element = [[[0,0],[0,1],[0,2],[1,2]], "L"]
    T_element = [[[0,0],[0,1],[0,2],[1,1]], "T"]
    
    elementC = "Z" + "_element"
    
    print(isElementValid())
    
    if isElementValid():
        return eval(elementC)
    
    else:
        return element

while True:
    play_area = [[0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],]

    element = choseElement()
    
    print(element)
    
    updatePlayarea()
    moveRightLeft()
    moveDown()
    showPlayarea()
    
    time.sleep(1)
    a += 1
    os.system("clear")
    current += 1
    
    if current == 18:
        current = 0