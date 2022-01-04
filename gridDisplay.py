alphabetList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","Q","R","S","X","Y","Z"]
gameGridList = []

def boundaryLine(xAxis,yAxis):
    boundaryLineContent = "  "
    boundaryLine = []
    i = 0
    while i < xAxis :
        boundaryLineContent += "+-----"
        i+=1
    boundaryLineContent += "+"
    boundaryLine.append(boundaryLineContent)
    return boundaryLine


def alphabetLine(xAxis,yAxis):
    alphabetLineContent = "  "
    alphabetLine = []
    i = 0
    while i < xAxis :
        alphabetLineContent += "   " + alphabetList[i] + "  "
        i+=1
    alphabetLineContent += " "
    alphabetLine.append(alphabetLineContent)
    return alphabetLine


def gameGrid(xAxis,yAxis,boundaryLine,alphabetLine):
    gameGridList.append(alphabetLine) #add first line to grid list - e.g [   A     B     C     D     E   ]
    gameGridList.append(boundaryLine) #add second line to grid list -     e.g [+-----+-----+-----+-----+-----+]

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
boundaryLine = boundaryLine(8,5)
alphabetLine= alphabetLine(8,5)
gameGrid(8,5,boundaryLine,alphabetLine)
for line in gameGridList:
    print("".join(line))
