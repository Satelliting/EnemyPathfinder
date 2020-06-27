# Course: CS4242
# Student Name: Jordan Allen
# Student ID: 000719555
# Assignment #: #2
# Due Date: 06/27/2020
# Signature: ________________
# Grade: ____________________

from pprint import pprint
import tkinter as tk


# Handles The GUI Functionality
class MainGUI:
    def __init__(self, mapLayout):
        self.mapLayout = mapLayout

        # GUI Main Section
        self.master = tk.Tk()
        self.master.title('Enemy Pathfinder Solution')

        # GUI Title Label
        tk.Label(self.master, text="Current Map Layout", width=18, justify='center').grid(row=5,column=0,columnspan=4)

        # Map Layout Labels
        self.mapLayout1  = tk.Label(self.master, text=mapLayout[0][0])
        self.mapLayout2  = tk.Label(self.master, text=mapLayout[0][1])
        self.mapLayout3  = tk.Label(self.master, text=mapLayout[0][2])
        self.mapLayout4  = tk.Label(self.master, text=mapLayout[0][3])
        self.mapLayout5  = tk.Label(self.master, text=mapLayout[0][4])
        self.mapLayout6  = tk.Label(self.master, text=mapLayout[1][0])
        self.mapLayout7  = tk.Label(self.master, text=mapLayout[1][1])
        self.mapLayout8  = tk.Label(self.master, text=mapLayout[1][2])
        self.mapLayout9  = tk.Label(self.master, text=mapLayout[1][3])
        self.mapLayout10 = tk.Label(self.master, text=mapLayout[1][4])
        self.mapLayout11 = tk.Label(self.master, text=mapLayout[2][0])
        self.mapLayout12 = tk.Label(self.master, text=mapLayout[2][1])
        self.mapLayout13 = tk.Label(self.master, text=mapLayout[2][2])
        self.mapLayout14 = tk.Label(self.master, text=mapLayout[2][3])
        self.mapLayout15 = tk.Label(self.master, text=mapLayout[2][4])
        self.mapLayout16 = tk.Label(self.master, text=mapLayout[3][0])
        self.mapLayout17 = tk.Label(self.master, text=mapLayout[3][1])
        self.mapLayout18 = tk.Label(self.master, text=mapLayout[3][2])
        self.mapLayout19 = tk.Label(self.master, text=mapLayout[3][3])
        self.mapLayout20 = tk.Label(self.master, text=mapLayout[3][4])
        self.mapLayout21 = tk.Label(self.master, text=mapLayout[4][0])
        self.mapLayout22 = tk.Label(self.master, text=mapLayout[4][1])
        self.mapLayout23 = tk.Label(self.master, text=mapLayout[4][2])
        self.mapLayout24 = tk.Label(self.master, text=mapLayout[4][3])
        self.mapLayout25 = tk.Label(self.master, text=mapLayout[4][4])

        self.mapLayout1.grid(row=0,column=0)
        self.mapLayout2.grid(row=0,column=1)
        self.mapLayout3.grid(row=0,column=2)
        self.mapLayout4.grid(row=0,column=3)
        self.mapLayout5.grid(row=0,column=4)
        self.mapLayout6.grid(row=1,column=0)
        self.mapLayout7.grid(row=1,column=1)
        self.mapLayout8.grid(row=1,column=2)
        self.mapLayout9.grid(row=1,column=3)
        self.mapLayout10.grid(row=1,column=4)
        self.mapLayout11.grid(row=2,column=0)
        self.mapLayout12.grid(row=2,column=1)
        self.mapLayout13.grid(row=2,column=2)
        self.mapLayout14.grid(row=2,column=3)
        self.mapLayout15.grid(row=2,column=4)
        self.mapLayout16.grid(row=3,column=0)
        self.mapLayout17.grid(row=3,column=1)
        self.mapLayout18.grid(row=3,column=2)
        self.mapLayout19.grid(row=3,column=3)
        self.mapLayout20.grid(row=3,column=4)
        self.mapLayout21.grid(row=4,column=0)
        self.mapLayout22.grid(row=4,column=1)
        self.mapLayout23.grid(row=4,column=2)
        self.mapLayout24.grid(row=4,column=3)
        self.mapLayout25.grid(row=4,column=4)

        # GUI Positional Labels & Entries (Enemy & Player)
        self.EnemyLabel  = tk.Label(self.master, text="Enemy Position: ", width=15).grid(row=0, column=5)
        self.PlayerLabel = tk.Label(self.master, text="Player Position: ", width=15).grid(row=2, column=5)

        self.EnemyPositionX = tk.Entry(self.master)
        self.EnemyPositionY = tk.Entry(self.master)

        self.PlayerPositionX = tk.Entry(self.master)
        self.PlayerPositionY = tk.Entry(self.master)

        self.EnemyPositionX.grid(row=0, column=6)
        self.EnemyPositionY.grid(row=1, column=6)

        self.PlayerPositionX.grid(row=2, column=6)
        self.PlayerPositionY.grid(row=3, column=6)

        # GUI Solve Button
        self.solveButton = tk.Button(self.master, text='Solve A* Route', command=lambda: main(self, self.mapLayout), state='active')
        self.solveButton.grid(row=4, column=6, sticky='nsew')
        self.solveLabel  = tk.Label(self.master, text="")
        self.solveLabel.grid(row=5,column=6, sticky='nsew')


        # GUI Mainloop
        tk.mainloop()

# The following is a Node class
# that is used to handle A* pathfinding
# based on the given parameters
# Parameters: (nodeParent=None, nodePosition=None)
class aStarNode():
    # Initializes the values with the creation of the instance
    def __init__(self, nodeParent=None, nodePosition=None):
        # Initial values
        self.nodeParent = nodeParent
        self.nodePosition = nodePosition

        # Starting values to assist with A* pathfinding
        self.data = 0
        self.level = 0
        self.fValue = 0

    # Handles when the aStarNode is called upon for equality
    def __eq__(self, other):
        return self.nodePosition == other.nodePosition

# Handles The Pathfinder Functionality
def pathfinder(mapLayout, enemyLocation, userLocation):
    # Initializes all enemyLocationNode variables
    enemyLocationNode = aStarNode(None, enemyLocation)
    enemyLocationNode.data = 0
    enemyLocationNode.level = 0
    enemyLocationNode.fValue = 0

    # Initializes all userLocationNode variables
    userLocationNode = aStarNode(None, userLocation)
    userLocationNode.data = 0
    userLocationNode.level = 0
    userLocationNode.fValue = 0


    # Initializes open & closed lists (for checking)
    openList = []
    closedList = []

    # Starts off by using the enemy's original location
    openList.append(enemyLocationNode)

    # Used in case of hang up over no possible outcomes
    mapSpaces = 0
    checkedSpaces = 0
    for mapRows in mapLayout:
        mapSpaces += len(mapRows)

    while len(openList) > 0:
        currentEnemyNode = openList[0]
        currentNodeIndex = 0

        for index, item in enumerate(openList):
            # Checks if the fValue values are the same
            if item.fValue < currentEnemyNode.fValue:
                currentEnemyNode = item
                currentNodeIndex = index

        # Removes the currentNodeIndex from the openList (to move towards more checking)
        openList.pop(currentNodeIndex)
        # Appends the currentEnemyNode to closedList (to move towards more checking)
        closedList.append(currentEnemyNode)

        # If the currentEnemyNode is not userLocationNode, we have not finished creating the path
        if currentEnemyNode == userLocationNode:
            # Instatiates the enemyPath
            enemyPath = []
            # Starts the enemyPath with the currentEnemyNode (to create data starting point for the path)
            currentCheckNode = currentEnemyNode

            # While currentCheckNode is not None, the list must grow
            while currentCheckNode is not None:
                enemyPath.append(currentCheckNode.nodePosition)
                currentCheckNode = currentCheckNode.nodeParent
            
            # When finished, returns data tuple of the path for the enemy to take to get to the user the quickest using A*
            return enemyPath[::-1]

        # Generates all the enemyChildren
        enemyChildren = []
        # Checks all possible adjacent squares
        for newEnemyPosition in [(0, -1), (0, 1), (1, 1), (1, 0), (-1, 1), (-1, -1), (1, -1), (-1, 0)]:
            enemyNodePosition = (currentEnemyNode.nodePosition[0] + newEnemyPosition[0], currentEnemyNode.nodePosition[1] + newEnemyPosition[1])

            # Checks if the enemyNodePosition is in the range
            if enemyNodePosition[0] > (len(mapLayout) - 1) or enemyNodePosition[0] < 0 or enemyNodePosition[1] > (len(mapLayout[len(mapLayout)-1]) -1) or enemyNodePosition[1] < 0:
                continue

            # Checks if the terrain is not blocked
            if mapLayout[enemyNodePosition[0]][enemyNodePosition[1]] != 0:
                continue

            # Generates the newEnemyNode for the list of enemyChildren
            newEnemyNode = aStarNode(currentEnemyNode, enemyNodePosition)
            
            # Appends the newEnemyNode to create the list of enemyChildren
            enemyChildren.append(newEnemyNode)

        # Loops through enemyChildren to check if any are in openList
        for enemyChild in enemyChildren:
            # Loops through all the enemyChildren in the closedList
            for closedPositionChild in closedList:
                # If enemyChild in closedList, NOT to be appended to openList
                if enemyChild == closedPositionChild:
                    continue
            # Creates the enemyChild data, level, fValue values
            enemyChild.data = currentEnemyNode.data + 1
            enemyChild.level = ((enemyChild.nodePosition[0] - userLocationNode.nodePosition[0]) ** 2) + ((enemyChild.nodePosition[1] - userLocationNode.nodePosition[1]) ** 2)
            enemyChild.fValue = enemyChild.data + enemyChild.level

            # Loops through all the enemyChildren in openList
            for openEnemyChild in openList:
                # If enemyChild already in openList & if the data value matches (for verification of exact value), NOT to be appended to openList
                if enemyChild == openEnemyChild and enemyChild.data > openEnemyChild.data:
                    continue

            # If passes through all checks, append enemyChild to openList
            openList.append(enemyChild)

        checkedSpaces += 1
        # Ensures no possible hang up over no possible solution
        if checkedSpaces == mapSpaces:
            return "N/A"


def main(gui, mapLayout):
    enemyLocation = (int(gui.EnemyPositionX.get()), int(gui.EnemyPositionY.get()))
    playerLocation = (int(gui.PlayerPositionX.get()), int(gui.PlayerPositionY.get()))

    aStarPath = pathfinder(mapLayout, enemyLocation, playerLocation)
    print("A* Star Enemy Path To User Starting From "+str(aStarPath[0])+": "+str(len(aStarPath)-1)+" Steps")

    for pathLocation in aStarPath:
        gui.newLabel = tk.Label(gui.master, text="*").grid(row=pathLocation[0], column=pathLocation[1])
    gui.solveButton['state'] = 'disabled'
    gui.solveLabel['text'] = f"Steps To Solve: {str(len(aStarPath)-1)}"
    pprint(aStarPath[1:])


# Current Map Layout
# Can Be Changed To Any Size Box
# 0 = Free Movable Space
# 1 = Wall or Obstacle (Not Movable Space)
# Simply Ensure There is at least 1 possible path from enemy to user when testing

# When Using GUI, Current Keep It To a 5x5 Box <-- !IMPORTANT
mapLayout = [
    [0,0,0,1,0],
    [0,1,0,0,0],
    [0,0,0,1,0],
    [1,0,0,0,1],
    [0,1,0,1,0],
]

print()
print("Current Map Layout")
print("=======================")
pprint(mapLayout)
print("=======================")
print()

masterGUI = MainGUI(mapLayout)
