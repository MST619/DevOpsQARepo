'''
S10192803, Dickson Kuan,
S10197943, Min Se Thu,
S10185214, Ethan Leong,
S10194816, Isaiah Low,
S10198398, Jeremiah Long

'''
alphabetList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
gameGridList = []

MainMenuData = \
['Welcome, mayor of Simp City!',
'------------------------------',
'1. Start new game',
'2. Load saved game',
'3. Show high scores\n'
'0. Exit']

def displayMainMenu():
    for i in range(len(MainMenuData)):
            print(MainMenuData[i])

def runMainMenu():
    result = 1
    while result != 0:
        displayMainMenu()
        userInput = input('Enter your option: ')
        result = MainMenuSelection(userInput)


# Exit the game
def exitGame():
	GameEnd = "Thanks for playing!"
	return GameEnd

def MainMenuSelection(userInput):
        if userInput == "0":
            exit = exitGame()
            print(exit)
            return 0
        elif userInput == "1":
            newGame(gameGridList)
        elif userInput == "2":
            print("Feature still under development!\n\n", end = '')
        elif userInput == "3":
            print("Feature still under development!\n\n", end = '')
        else:
            print("Invalid input!\n", end = '')

# def boundaryLine(xAxis,yAxis):
#     print("this ran in boundary line")
#     boundaryLineContent = "  "
#     boundaryLine = []
#     i = 0
#     while i < xAxis :
#         boundaryLineContent += "+-----"
#         i+=1
#
#     boundaryLineContent += "+"
#     boundaryLine.append(boundaryLineContent)
#     return boundaryLine
#
#
# def alphabetLine(xAxis,yAxis):
#     alphabetLineContent = "  "
#     alphabetLine = []
#     i = 0
#     while i < xAxis :
#         alphabetLineContent += "   " + alphabetList[i] + "  "
#         i+=1
#     alphabetLineContent += " "
#     alphabetLine.append(alphabetLineContent)
#     return alphabetLine


def gameGrid(xAxis,yAxis):
    #Start of code to create alphabetLine - First Line of game grid"
    alphabetLineContent = "  "
    alphabetLine = []
    i = 0
    while i < xAxis :
        alphabetLineContent += "   " + alphabetList[i] + "  "
        i+=1
    alphabetLineContent += " "
    alphabetLine.append(alphabetLineContent)
    gameGridList.append(alphabetLine) #add first line to grid list - e.g [   A     B     C     D     E   ]
    #End of code to create alphabetLine - First Line of game grid"

    #Start of code to create boundaryLine - game grid seperating lines"
    boundaryLineContent = "  "
    boundaryLine = []
    i = 0
    while i < xAxis :
        boundaryLineContent += "+-----"
        i+=1

    boundaryLineContent += "+"
    boundaryLine.append(boundaryLineContent)
    gameGridList.append(boundaryLine) #add second line to grid list -     e.g [+-----+-----+-----+-----+-----+]
    #End of code to create boundaryLine - game grid seperating lines"

    #Start of code to create grids
    i = 0
    while i < yAxis:
        row = []
        rowContent = ""
        if i < 9:
            row += ((" " + str(i+1) + "|     |") + (("     |") * (xAxis-1)))
        else:
            row += (("" + str(i+1) + "|     |") + (("     |") * (xAxis-1)))
        row.append(rowContent)
        gameGridList.append(row)
        gameGridList.append(boundaryLine)
        i+=1
        #End of code to create grids
def newGame(gameGridList):
    print(gameGridList)
    print("Please select Game Map size \n")
    xAxis = int(input('Enter in your desired map size width: '))
    yAxis = int(input('Enter in your desired map size height: '))
    print("Hi this runs here")
    gameGrid(xAxis,yAxis)
    #Prints out game grid
    for line in gameGridList:
        print("".join(line))
# code runs here
try:
    runMainMenu()
except:
    pass
