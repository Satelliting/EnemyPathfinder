from pprint import pprint


# The following is a Node class
# that is used to handle A* pathfinding
# based on the given parameters
# Paramters: (nodeParent=None, nodePosition=None)
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
			return "No possible path to user."


if __name__ == '__main__':
	
	# Current Map Layout
	# Can Be Changed To Any Size Box
	# 0 = Free Movable Space
	# 1 = Wall or Obstacle (Not Movable Space)
	# Simply Ensure There is at least 1 possible path from enemy to user when testing
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

	enemyStartX = input("Starting Enemy X Coordinate: ")
	enemyStartY = input("Starting Enemy Y Coordinate: ")

	userStartX = input("User X Coordinate: ")
	userStartY = input("User Y Coordinate: ")

	startCoordinates  = (int(enemyStartX),int(enemyStartY))
	userCoordinates   = (int(userStartX), int(userStartY))

	print()
	print("=======================")
	print("Enemy Coordinates: "+str(startCoordinates))
	print("User Coordinates:  "+str(userCoordinates))
	print()


	aStarPath = pathfinder(mapLayout, startCoordinates, userCoordinates)

	# Prints Path & # of Steps (minus starting position)
	print("A* Star Enemy Path To User Starting From "+str(aStarPath[0])+": "+str(len(aStarPath)-1)+" Steps")
	pprint(aStarPath[1:])

