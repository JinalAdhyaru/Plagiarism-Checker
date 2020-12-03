import re
import math


def findFileSimilarity(database, inputQuery):

    universalSetOfUniqueWords = []
    matchPercentage = 0

    lowercaseQuery = inputQuery.lower()

    # Replace punctuation by space and split
    queryWordList = re.sub("[^\w]", " ", lowercaseQuery).split()
    
    for word in queryWordList:
        if word not in universalSetOfUniqueWords:
            universalSetOfUniqueWords.append(word)

    database1 = database.lower()

    # Replace punctuation by space and split
    databaseWordList = re.sub("[^\w]", " ", database1).split()
    # databaseWordList = map(str, databaseWordList)			#And this also leads to divide by zero error

    for word in databaseWordList:
        if word not in universalSetOfUniqueWords:
            universalSetOfUniqueWords.append(word)

    queryTF = []
    databaseTF = []

    for word in universalSetOfUniqueWords:
        queryTfCounter = 0
        databaseTfCounter = 0

        for word2 in queryWordList:
            if word == word2:
                queryTfCounter += 1
        queryTF.append(queryTfCounter)

        for word2 in databaseWordList:
            if word == word2:
                databaseTfCounter += 1
        databaseTF.append(databaseTfCounter)

    dotProduct = 0
    for i in range(len(queryTF)):
        dotProduct += queryTF[i]*databaseTF[i]

    queryVectorMagnitude = 0
    for i in range(len(queryTF)):
        queryVectorMagnitude += queryTF[i]**2
    queryVectorMagnitude = math.sqrt(queryVectorMagnitude)

    databaseVectorMagnitude = 0
    for i in range(len(databaseTF)):
        databaseVectorMagnitude += databaseTF[i]**2
    databaseVectorMagnitude = math.sqrt(databaseVectorMagnitude)

    matchPercentage = (float)(
        dotProduct / (queryVectorMagnitude * databaseVectorMagnitude))*100

    print(matchPercentage)
    return matchPercentage


def multipleFile(text, database):
    max = 0
    maxSimFile = ''
    for file in database:
        sim = findFileSimilarity(text, database[file])
        if(sim > max):
            max = sim
            maxSimFile = file
    return maxSimFile, max