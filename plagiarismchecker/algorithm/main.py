
from nltk.corpus import stopwords
from plagiarismchecker.algorithm import webSearch
import sys
import re

# Given a text string, remove all non-alphanumeric
# characters (using Unicode definition of alphanumeric).


def getQueries(text, n):
    sentenceEnders = re.compile("['.!?]")
    sentenceList = sentenceEnders.split(text)
    sentencesplits = []
    en_stops = set(stopwords.words('english'))

    for sentence in sentenceList:
        x = re.compile(r'\W+', re.UNICODE).split(sentence)
        for word in x:
            if word.lower() in en_stops:
                x.remove(word)
        x = [ele for ele in x if ele != '']
        sentencesplits.append(x)
    finalq = []
    for sentence in sentencesplits:
        l = len(sentence)
        if l > n:
            l = int(l/n)
            index = 0
            for i in range(0, l):
                finalq.append(sentence[index:index+n])
                index = index + n-1
            if index != len(sentence):
                finalq.append(sentence[len(sentence)-index:len(sentence)])
        else:
            finalq.append(sentence)
    return finalq


def findSimilarity(text):
    # n-grams N VALUE SET HERE
    n = 9
    queries = getQueries(text, n)
    print('GetQueries task complete')
    q = [' '.join(d) for d in queries]
    output = {}
    c = {}
    i = 1
    count = len(q)
    if count > 100:
        count = 100
    for s in q[0:count]:
        output, c = webSearch.searchWeb(s, output, c)
        print('Web search task complete')
        # print(output,c)
        sys.stdout.flush()
        i = i+1
    numqueries = 0
    for s in q[0:count]:
        if(len(s) != 0):
            numqueries = numqueries + 1
    totalPercent = 0
    outputLink = []
    for link in output:
        percentage = (output[link]*c[link]*100)/numqueries
        if percentage > 20:
            totalPercent = totalPercent + percentage
            outputLink.append(link)

    print(totalPercent, outputLink)
    print("\nDone!")
    return totalPercent, outputLink

# str = 'Sequential Search: In this, the list or array is traversed sequentially and every element is checked. For example: Linear Search.Interval Search: These algorithms are specifically designed for searching in sorted data-structures. These type of searching algorithms are much more efficient than Linear Search as they repeatedly target the center of the search structure and divide the search space in half.'
# main(str)
