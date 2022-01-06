import random

#Part 1
def mainMenu():
    print('Welcome, mayor of Simp City!')
    print('------------------------------')
    print('1. Start new game')
    print('2. Load saved game')
    print('3. Show high scores')
    print()
    print('0. Exit')
    userOption = input('Your choice? ')        
    return userOption

part1 = mainMenu()

#Part 1.1
def newGame():
    board = [['','','',''],\
            ['','','',''],\
            ['','','',''],\
            ['','','','']]
    
    #5 buildings with 8 copy each
    building = [['HSE',8],['FAC',8],['SHP',8],['HWY',8],['BCH',8]]
    buildingCode = ['HSE','FAC','SHP','HWY','BCH']

    #Random building generator
    randomBuilding1 = random.randint(0,4)
    randomBuilding2 = random.randint(0,4)
    
    turn = 1
    print('Turn {}'.format(turn))    
    

    #Making the board
    print("{:>5}{:>6}{:>6}{:>6}".format("A", "B", "C", "D"))
    for row in range(len(board)):
        column = len(board[row])
        print(' ' + '+-----'*column + '+')
        print(row+1, end = '')
        for line in range(len(board[row])):
            print('|{:^5}'.format(board[row][line]), end = '')
        print('|')
    print(' ' + '+-----'*column + '+')    
    
    
    #Options
    print('1. Build a {}'.format(buildingCode[randomBuilding1]))
    print('2. Build a {}'.format(buildingCode[randomBuilding2]))
    print('3. See remaining buildings')
    print('4. See current score')
    print()
    print('5. Save game')
    print('0. Exit to main menu')
    userOption = input('Your choice? ')
    return userOption,board,randomBuilding1,randomBuilding2,turn,building

#Part 1.2
def LoadSavedGame():
    
    Path = input("Enter the file location which contains the saved file (E.g C:\SimpCity_SaveFile\) ")
    LoadFile = open(Path + 'SaveFile.txt', 'r')
    txt=''
    for i in LoadFile:
        txt+=i
    txt = txt.split('|')
    #Turn
    turn = int(txt[1])
    #Board
    board = []
    for i in txt[0].split(':'):
        row = []
        for o in i.split('.'):
            row.append(o)
        board.append(row)
    #Building
    building = []
    for i in txt[2].split(':'):
        o = i.split(',')
        row = [o[0],int(o[1])]
        building.append(row)
    LoadFile.close()       
    

    #Making the board
    print("{:>5}{:>6}{:>6}{:>6}".format("A", "B", "C", "D"))
    for row in range(len(board)):
        column = len(board[row])
        print(' ' + '+-----'*column + '+')
        print(row+1, end = '')
        for line in range(len(board[row])):
            print('|{:^5}'.format(board[row][line]), end = '')
        print('|')
    print(' ' + '+-----'*column + '+')
    buildingCode = ['HSE','FAC','SHP','HWY','BCH']
    randomBuilding1 = random.randint(0,4)
    randomBuilding2 = random.randint(0,4)
    #Selection
    print('1. Build a {}'.format(buildingCode[randomBuilding1]))
    print('2. Build a {}'.format(buildingCode[randomBuilding2]))
    print('3. See remaining buildings')
    print('4. See current score')
    print()
    print('5. Save game')
    print('0. Exit to main menu')
    userOption = input('Your choice? ')
    return board, turn, userOption, randomBuilding1, randomBuilding2, building

#Part 1.3
def ExitGame():
    End = 'Thanks for playing!'
    return End

#Part 2.3
def currentScore(board,randomBuilding1,randomBuilding2,newBuilding,turn):
    global Total
    #Beach
    beach_points = 0
    counter = 0
    point = ""
    while counter < len(board):
        if board[counter][0] == "BCH":
            beach_points += 3
            point = point + "3 + "
        if board[counter][3] == "BCH":
            beach_points += 3
            point = point + "3 + "
        if board[counter][1] == "BCH":
            beach_points += 1
            point = point + "1 + "
        if board[counter][2] == "BCH":
            beach_points += 1
            point = point + "1 + "
        counter+=1
    point = point[:-2]
    print("BCH: {} = {}".format(point,beach_points))    

    #Factory
    flattened_board = [val for sublist in board for val in sublist]
    board_count = flattened_board.count("FAC")

    if board_count == 0:
        print("FAC:{}".format(" = 0"))
        FAC_points = 0

    if board_count == 1:
        print("FAC: {}".format("1 = 1"))
        FAC_points = 1

    if board_count == 2:
        print("FAC: {}".format("2 + 2 = 4"))
        FAC_points = 4

    if board_count == 3:
        print("FAC: {}".format("3 + 3 + 3 = 9"))
        FAC_points = 9

    if board_count == 4:
        print("FAC: {}".format("4 + 4 + 4 + 4 = 16"))
        FAC_points = 16

    if board_count > 4:
        remaining = board_count - 4
        remaining2 = " + 1"*remaining
        FAC_points = 16 + remaining
        print("FAC: {}{} = {}".format("4 + 4 + 4 + 4",remaining2,FAC_points))

    #House
    house_points = 0
    txt = ''
    print('HSE: ',end = '')
    for Box in range(len(board)):
        for column in range(len(board[Box])):
            CurrentScore = 0
            FAC = False
            if('HSE' in board[Box][column]):
                if (0 <= Box + 1 < len(board[0])):
                    if (board[Box + 1][column] == "HSE"):
                        CurrentScore+=1
                    if (board[Box + 1][column] == "SHP"):
                        CurrentScore+=1
                    if (board[Box + 1][column] == "BCH"):
                        CurrentScore+=2
                    if (board[Box + 1][column] == "FAC"):
                        FAC = True
                if (0 <= Box - 1 < len(board[0])):
                    if (board[Box- 1][column] == "HSE"):
                        CurrentScore+=1
                    if (board[Box- 1][column] == "SHP"):
                        CurrentScore+=1
                    if (board[Box- 1][column] == "BCH"):
                        CurrentScore+=2
                    if (board[Box- 1][column] == "FAC"):
                        FAC = True
                if (0 <= column + 1 < len(board)):
                    if (board[Box][column + 1] == "HSE"):
                        CurrentScore+=1
                    if (board[Box][column + 1] == "SHP"):
                        CurrentScore+=1
                    if (board[Box][column + 1] == "BCH"):
                        CurrentScore+=2
                    if (board[Box][column + 1] == "FAC"):
                        FAC = True
                if (0 <= column - 1 < len(board)):
                    if (board[Box][column - 1] == "HSE"):
                        CurrentScore+=1
                    if (board[Box][column - 1] == "SHP"):
                        CurrentScore+=1
                    if (board[Box][column - 1] == "BCH"):
                        CurrentScore+=2
                    if (board[Box][column - 1] == "FAC"):
                        FAC = True
            if FAC == True:
                CurrentScore = 1
                house_points += CurrentScore
            else:
                house_points+=CurrentScore
            if CurrentScore != 0:
                txt += '{} + '.format(CurrentScore)
    txt = txt[:-2]
    print(txt + '= {}'.format(house_points))
                
    
    #Shop
    SHPscore = 0
    txt = ''
    print('SHP: ',end = '')
    for Box in range(len(board)):
        for column in range(len(board[Box])):
            CurrentScore = 0
            HSE = False
            FAC = False
            BCH = False
            SHP = False
            HWY = False
            if('SHP' in board[Box][column]):
                if (0 <= Box + 1 < len(board[0])):
                    if (board[Box + 1][column] == "HSE")and not HSE:
                        CurrentScore+=1
                        HSE = True
                    if (board[Box + 1][column] == "BCH")and not BCH:
                        CurrentScore+=1
                        BCH = True
                    if (board[Box + 1][column] == "FAC")and not FAC:
                        CurrentScore+=1
                        FAC = True
                    if (board[Box + 1][column] == "SHP")and not SHP:
                        CurrentScore+=1
                        SHP = True
                    if (board[Box + 1][column] == "HWY")and not HWY:
                        CurrentScore+=1
                        HWY = True
                if (0 <= Box - 1 < len(board[0])):
                    if (board[Box- 1][column] == "HSE")and not HSE:
                        CurrentScore+=1
                        HSE = True
                    if (board[Box- 1][column] == "BCH")and not BCH:
                        CurrentScore+=1
                        BCH =True
                    if (board[Box- 1][column] == "FAC")and not FAC:
                       CurrentScore+=1
                       FAC = True
                    if (board[Box- 1][column] == "SHP")and not SHP:
                       CurrentScore+=1
                       SHP = True
                    if (board[Box- 1][column] == "HWY")and not HWY:
                       CurrentScore+=1
                       HWY = True
                if (0 <= column + 1 < len(board)):
                    if (board[Box][column + 1] == "HSE")and not HSE:
                        CurrentScore+=1
                        HSE = True
                    if (board[Box][column + 1] == "BCH")and not BCH:
                        CurrentScore+=1
                        BCH = True
                    if (board[Box][column + 1] == "FAC")and not FAC:
                        CurrentScore+=1
                        FAC = True
                    if (board[Box][column + 1] == "SHP")and not SHP:
                        CurrentScore+=1
                        SHP = True
                    if (board[Box][column + 1] == "HWY")and not HWY:
                        CurrentScore+=1
                        HWY = True
                if (0 <= column - 1 < len(board)):
                    if (board[Box][column - 1] == "HSE")and not HSE:
                        CurrentScore+=1
                        HSE = True
                    if (board[Box][column - 1] == "BCH")and not BCH:
                        CurrentScore+=1
                        BCH = True
                    if (board[Box][column - 1] == "FAC")and not FAC:
                        CurrentScore+=1
                        FAC = True
                    if (board[Box][column - 1] == "SHP")and not SHP:
                        CurrentScore+=1
                        SHP = True
                    if (board[Box][column - 1] == "HWY")and not HWY:
                        CurrentScore+=1
                        HWY = True
            SHPscore += CurrentScore
            if CurrentScore != 0:
                txt += '{} + '.format(CurrentScore)
    txt = txt[:-2]
    print(txt + '= {}'.format(SHPscore))

    #Highway
    txt = ''
    HWYscore = 0
    print('HWY: ',end = '')
    for Box in range(len(board)):
        chain = 0
        for Column in range(len(board[Box])):
            if ('HWY' in board[Box][Column]):
                if chain != 0:
                    chain -= 1
                    continue
                chain = 1
                ColumnMove = Column
                while True:
                    if (0 <= ColumnMove + 1 < len(board)):
                        if (board[Box][ColumnMove + 1] == "HWY"):
                            chain+=1
                            ColumnMove += 1
                        else:
                            break
                    else:
                        break
            if chain != 0:
                txt += "{:} + ".format(chain) * chain
                HWYscore+=chain**2
                chain -= 1
    if txt != "":
        txt = txt[:-2]
        print(txt + '= {}'.format(HWYscore))
    else:
        print("= 0")

    #Total points
    Total = beach_points+FAC_points+house_points+SHPscore+HWYscore

    print('Total score: {}'.format(Total))
    if turn <= 16:
        buildingCode = ['HSE','FAC','SHP','HWY','BCH']
        randomBuilding1 = random.randint(0,4)
        randomBuilding2 = random.randint(0,4)
    
        #Check if the building value reaches 0, it will refresh.
        while True:
            if newBuilding[randomBuilding1][1] <= 0:
                randomBuilding1 = random.randint(0,4)
                continue
            if newBuilding[randomBuilding2][1] <= 0:
                randomBuilding2 = random.randint(0,4)
                continue
            break
    
        #Options
        print('1. Build a {}'.format(buildingCode[randomBuilding1]))
        print('2. Build a {}'.format(buildingCode[randomBuilding2]))
        print('3. See remaining buildings')
        print('4. See current score')
        print()
        print('5. Save game')
        print('0. Exit to main menu')
        userOption = input('Your choice? ')
        return board,randomBuilding1,randomBuilding2,userOption,newBuilding
    else:
        #ADVANCE STUFF - HIGH SCORE
        return

#Part 2.1 % 3.0
def formBuilding(board,building,turn,newBuilding):
    boolean = True
    while boolean:
        validation = ["A1","A2","A3","A4","B1","B2","B3","B4","C1","C2","C3","C4","D1","D2","D3","D4"]
        userOption = input('Build where? ')
        userOption = userOption.upper()
        if userOption not in validation:
            print("Please input correctly")
            continue
        
        else:
            
            #Find location to build the building
            LocationList = [['A',0],['B',1],['C',2],['D',3]]
            for row in LocationList:
                
                if userOption[0] in row:
                    location = [int(userOption[1])-1,row[1]]
                    
                    if (board[location[0]][location[1]] == ''):
                        Valid = False
                        if (0 <= location[0] + 1 < len(board[0])):
                            if (board[location[0] + 1][location[1]] != ""):
                                Valid = True
                        if (0 <= location[0] - 1 < len(board[0])):
                            if (board[location[0]- 1][location[1]] != ""):
                                Valid = True
                        if (0 <= location[1] + 1 < len(board)):
                            if (board[location[0]][location[1] + 1] != ""):
                                Valid = True
                        if (0 <= location[1] - 1 < len(board)):
                            if (board[location[0]][location[1] - 1] != ""):
                                Valid = True

                        if Valid == True or turn == 1:
                            board[location[0]][location[1]] = newBuilding[building][0]
                            boolean = False
                        else:
                            print('You must build to an existing building.')
                    else:
                        print('The location you tried to build has another building.\nPlease choose another location!')

    #Display board
    turn += 1

    #Random building generator
    randomBuilding1 = random.randint(0,4)
    randomBuilding2 = random.randint(0,4)
    
    buildingCode = ['HSE','FAC','SHP','HWY','BCH']
    
    newBuilding[building][1] -= 1
       
    
    #If building quantity reaches 0, it will refresh
    while True:
        if newBuilding[randomBuilding1][1] <= 0:
            randomBuilding1 = random.randint(0,4)
            continue
            
        if newBuilding[randomBuilding2][1] <= 0:
            randomBuilding2 = random.randint(0,4)
            continue
        
        break
        
    
    if turn <= 16:
        print('Turn {}'.format(turn))
        print("{:>5}{:>6}{:>6}{:>6}".format("A", "B", "C", "D"))
        for row in range(len(board)):
            column = len(board[row])
            print(' ' + '+-----'*column + '+')
            print(row+1, end = '')
            for line in range(len(board[row])):
                print('|{:^5}'.format(board[row][line]), end = '')
            print('|')
        print(' ' + '+-----'*column + '+')


        #Options
        print('1. Build a {}'.format(buildingCode[randomBuilding1]))
        print('2. Build a {}'.format(buildingCode[randomBuilding2]))
        print('3. See remaining buildings')
        print('4. See current score')
        print()
        print('5. Save game')
        print('0. Exit to main menu')      
        userOption = input('Your choice? ')          
            
        
            
        
        
    #Part 3
    if turn > 16:
        print()
        print('Final layout of Simp City')
        print("{:>5}{:>6}{:>6}{:>6}".format("A", "B", "C", "D"))
        for row in range(len(board)):
            column = len(board[row])
            print(' ' + '+-----'*column + '+')
            print(row+1, end = '')
            for line in range(len(board[row])):
                print('|{:^5}'.format(board[row][line]), end = '')
            print('|')
        print(' ' + '+-----'*column + '+')
        currentScore(board,randomBuilding1,randomBuilding2,newBuilding,turn)
        highscore(Total)
        

    return userOption,board,randomBuilding1,randomBuilding2,turn,newBuilding

#Part 2.2
def remainingBuildings(newBuilding):
    print("{:<30}{:<20}".format("Building","Remaining"))
    print("{:<30}{:<20}".format("--------","--------"))
    for count in range(len(newBuilding)):
        print("{:<30}{:<20}".format(newBuilding[count][0],newBuilding[count][1]))

    #Options
    buildingCode = ['HSE','FAC','SHP','HWY','BCH']
    randomBuilding1 = random.randint(0,4)
    randomBuilding2 = random.randint(0,4)
    print('1. Build a {}'.format(buildingCode[randomBuilding1]))
    print('2. Build a {}'.format(buildingCode[randomBuilding2]))
    print('3. See remaining buildings')
    print('4. See current score')
    print()
    print('5. Save game')
    print('0. Exit to main menu')
    userOption = input('Your choice? ')
    return randomBuilding1, randomBuilding2, userOption

#Part 2.4 newBuilding = [['HSE',8],['FAC',8],['SHP',8],['HWY',8],['BCH',8]]
def SaveGame(board,turn,newBuilding):
    
    Path = input("Choose which file location you want to save into (E.g C:\SimpCity_SaveFile\) ")
    SaveFile = open(Path + 'SaveFile.txt', 'w')
    txt = ''
    count = 0
    while count < len(board):
        inside = board[count]
        index = 0
        while index < len(inside):
            txt += "{}.".format(inside[index])
            index +=1
        txt = txt[0:-1]
        txt += ":"
        count +=1
    txt = txt[:-1] 
    txt += "|{}|".format(turn)
    
    count = 0
    while count < len(newBuilding):
        txt += "{},{}:".format(newBuilding[count][0],newBuilding[count][1])
        count +=1
    txt = txt[0:-1]
    
    
    
    SaveFile.write(txt)
    SaveFile.close()
    print()
    print('Game Saved!')
    return SaveFile

def Leaderboard():
    path = "C:\\Users\\Ahmad Mikail\\Desktop\\Save File\\"
    LoadFile = open(path + "Leaderboard.txt", "r")
    txt = ""

    for i in LoadFile:
        txt += i

    txt = txt.split("\n")
    seperated = []
    
    count = 0
    while count < len(txt):
        list3 = txt[count].split(";")
        seperated.append(list3)
        count +=1

    print("--------- HIGH SCORES ---------")
    print("{:<6s}{:<20s}{:<6s}".format("Pos","Player","Score"))
    print("{:<6s}{:<20s}{:<6s}".format("---","------","-----"))
    count = 0
    pos = 1
    while count < len(seperated):
        print("{:<6d}{:<20s}{:<6s}".format(pos,seperated[count][1],seperated[count][0]))
        pos +=1
        count +=1

def highscore(Total):
    path = "C:\\Users\\Ahmad Mikail\\Desktop\\Save File\\"
    LoadFile = open(path + "Leaderboard.txt", "r")
    highscore = []
    highscorelist = []
    pos_leaderboard = 0

    for x in LoadFile:
        x = x.strip().split(";")
        highscore.append(x)

    for i in range(len(highscore)):
        if Total > int(highscore[i][0]):
            print('Congratulations! You made the high score board at position {0}!'.format(i+1))
            username_winner = input('Please enter your name (max 20 chars): ')
            while True:
                if len(username_winner) > 20:
                    print('Your name is too long, max chars is 20')
                    username_winner = input('Please enter your name (max 20 chars): ')
                else:
                    break
            highscorelist.append([str(Total),username_winner])
            pos_leaderboard += 1
            break
        else:
            highscorelist.append(highscore[i])
            pos_leaderboard += 1

    while pos_leaderboard < 10:
        highscorelist.append(highscore[pos_leaderboard - 1])
        pos_leaderboard += 1
    

    LoadFile.close()
    LoadFile = open(path + 'Leaderboard.txt','w')

    for x in highscorelist:
        LoadFile.write("{};{}\n".format(x[0],x[1]))
    

    LoadFile.close()
    
    
    
        

#Game Process
while True:
    if part1 == '1':
        userOption,board,randomBuilding1,randomBuilding2,turn,building = newGame()
        while True:
            if turn > 16:
                print()
                part1 = mainMenu()
                break
                #Process Part 2.1
            if userOption == '1':
                userOption,board,randomBuilding1,randomBuilding2,turn,building = formBuilding(board,randomBuilding1,turn,building)

            #Process Part 2.1
            elif userOption == '2':
                userOption,board,randomBuilding1,randomBuilding2,turn,building = formBuilding(board,randomBuilding2,turn,building)

            #Process Part 2.2
            elif userOption == '3':
                randomBuilding1,randomBuilding2,userOption = remainingBuildings(building)

            #Process Part 2.3
            elif userOption == '4':
                board,randomBuilding1,randomBuilding2,userOption,building = currentScore(board,randomBuilding1,randomBuilding2,building,turn)

            #Process Part 2.4
            elif userOption == '5':
                SaveGame(board,turn,building)
                userOption = input('Your choice? ')
            #Process Part 2.5
            elif userOption == '0':
                part1 = mainMenu()
                break
            #Stop if User input wrong
            else:
                print("Invalid input. Please enter 1, 2, 3, 4, 5 or 0")
                userOption = input("Your choice? ")
                continue

    #Process Part 1.2
    elif part1 == '2':
        board, turn, userOption, randomBuilding1, randomBuilding2,building = LoadSavedGame()
        while True:
            if turn > 16:
                print()
                part1 = mainMenu()
                break
                #Process Part 2.1
            if userOption == '1':
                userOption,board,randomBuilding1,randomBuilding2,turn,building = formBuilding(board,randomBuilding1,turn,building)

            #Process Part 2.1
            elif userOption == '2':
                userOption,board,randomBuilding1,randomBuilding2,turn,building = formBuilding(board,randomBuilding2,turn,building)

            #Process Part 2.2
            elif userOption == '3':
                randomBuilding1,randomBuilding2,userOption = remainingBuildings(building)

            #Process Part 2.3
            elif userOption == '4':
                board,randomBuilding1,randomBuilding2,userOption,building = currentScore(board,randomBuilding1,randomBuilding2,building,turn)

            #Process Part 2.4
            elif userOption == '5':
                SaveGame(board,turn,building)
                userOption = input('Your choice? ')
            #Process Part 2.5
            elif userOption == '0':
                part1 = mainMenu()
                break
            #Stop if User input wrong
            else:
                print("Invalid input. Please enter 1, 2, 3, 4, 5 or 0")
                userOption = input("Your choice? ")
                continue
            
    #Process Part 1.3
    elif part1 == '0':
        Part1_3 = ExitGame()
        print(Part1_3)
        break
    
    elif part1 == '3':        
        Leaderboard()
        print()
        part1 = mainMenu()
        
    
    #Stop if User input wrong
    else:
        print("Invalid input. Please enter 1, 2 or 3")
        part1 = input("Your choice? ")                
        continue






