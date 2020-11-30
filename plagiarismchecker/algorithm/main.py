# -*- coding: utf-8 -*-
# Master script for the plagiarism-checker
# Coded by: Shashank S Rao

<<<<<<< HEAD
# import other modules
# from algorithm import webSearch
# import importlib
# from webSearch import searchWeb
from plagiarismchecker.algorithm import webSearch
=======
from algorithm import webSearch
>>>>>>> 63ab4db46e378830896cdb82213ffd96ad07b30d
# importlib.module_name('webSearch')
# import required modules
import codecs
import traceback
import sys
import operator

# Given a text string, remove all non-alphanumeric
# characters (using Unicode definition of alphanumeric).


def getQueries(text, n):
    import re
    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(text)
    sentencesplits = []
    for sentence in sentenceList:
        x = re.compile(r'\W+', re.UNICODE).split(sentence)
        x = [ele for ele in x if ele != '']
        sentencesplits.append(x)
    finalq = []
    for sentence in sentencesplits:
        l = len(sentence)
        l = int(l/n)
        index = 0
        for i in range(0, l):		
            finalq.append(sentence[index:index+n])
            index = index + n-1
        if index != len(sentence):
            finalq.append(sentence[len(sentence)-index:len(sentence)])
    return finalq


def findSimilarity(text):
    # n-grams N VALUE SET HERE
    n = 9
    queries = getQueries(text, n)
    print('GetQueries task complete')
    q = [' '.join(d) for d in queries]
    # using 2 dictionaries: c and output
    # output is used to store the url as key and number of occurences of that url in different searches as value
    # c is used to store url as key and sum of all the cosine similarities of all matches as value
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
    outputPercent = {}
    for link in output:
        percentage = (output[link]*c[link]*100)/numqueries
        outputPercent[link] = percentage
    print(outputPercent)
    print("\nDone!")
    return outputPercent

# str = 'Sequential Search: In this, the list or array is traversed sequentially and every element is checked. For example: Linear Search.Interval Search: These algorithms are specifically designed for searching in sorted data-structures. These type of searching algorithms are much more efficient than Linear Search as they repeatedly target the center of the search structure and divide the search space in half.'
# main(str)