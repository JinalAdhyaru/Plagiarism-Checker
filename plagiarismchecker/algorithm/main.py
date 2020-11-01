# -*- coding: utf-8 -*-
# Master script for the plagiarism-checker
# Coded by: Shashank S Rao

# import other modules
from webSearch import searchWeb

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


def main(text):
    # n-grams N VALUE SET HERE
    n = 9
    queries = getQueries(text, n)
    print('GetQueries task complete')
    q = [' '.join(d) for d in queries]
    found = []
    # using 2 dictionaries: c and output
    # output is used to store the url as key and number of occurences of that url in different searches as value
    # c is used to store url as key and sum of all the cosine similarities of all matches as value
    output = {}
    c = {}
    i = 1
    count = len(q)
    if count > 100:
        count = 100
    for s in q[:100]:
        output, c = searchWeb(s, output, c)
        # msg = "\r"+str(i)+"/"+str(count)+"completed..."
        print('Web search task complete')
        sys.stdout.flush()
        i = i+1
    # print "\n"
    # f = open(sys.argv[2],"w")
    # for ele in sorted(c.iteritems(),key=operator.itemgetter(1),reverse=True):
    # 	f.write(str(ele[0])+" "+str(ele[1]*100.00))
    # 	f.write("\n")
    # f.close()
    print(output, c)
    print("\nDone!")


# if __name__ == "__main__":
# 	try:
# 		main()
# 	except:
# 		#writing the error to stdout for better error detection
# 		error = traceback.format_exc()
# 		print ("\nUh Oh!\n"+"Plagiarism-Checker encountered an error!:\n"+error)

str = 'n a DFA, for a particular input character, the machine goes to one state only. A transition function is defined on every state for every input symbol. Also in DFA null (or ε) move is not allowed, i.e., DFA cannot change state without any input character. '
main(str)
