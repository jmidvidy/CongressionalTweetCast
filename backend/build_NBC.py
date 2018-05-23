# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 20:32:01 2018

@author: jmidv
"""


import csv
import os
import json

stop_list = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", 
             "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", 
             "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", 
             "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", 
             "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", 
             "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", 
             "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", 
             "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", 
             "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify",
             "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", 
             "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he",
             "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him",
             "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest",
             "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", 
             "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover",
             "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", 
             "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not",
             "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto",
             "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own",
             "part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed",
             "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere",
             "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", 
             "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", 
             "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", 
             "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", 
             "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too",
             "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", 
             "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when",
             "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", 
             "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", 
             "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours",
             "yourself", "yourselves", "the", "i", "oh", "did", '',"let"]

chars = set('!@\/,.()*^%[]{}#$12345;&-+=:6\'7890')



#delete all the existing models in the current directory
models = os.listdir("C:\\Users\\jmidv\\Documents\\Spring 2018\\EECS 338\\models")
for f in models:
    fp = "C:\\Users\\jmidv\\Documents\\Spring 2018\\EECS 338\\models\\" + f
    os.remove(fp)

print("\n")
print("------Removing old models!------")
print("------Creating new models!------")

#path elements for file access
fullPath = "C:\\Users\\jmidv\\Documents\\Spring 2018\\EECS 338\\backend\\tweets_repo"
fileNames = os.listdir("C:\\Users\\jmidv\\Documents\\Spring 2018\\backend\\EECS 338\\tweets_repo")

#counters for printers
i = 0
total = len(fileNames)

#main output
for line in fileNames:
    tweetList = []
    currTweetDict = {}
    filePath = fullPath + "\\" + line
    with open(filePath,"r") as filereader:           
        #sort the input file with the csv reader and the , delimiter
        fileListReader = csv.reader(filereader, delimiter=',')
        
        #place holder for dictionary to be created in loop
        for row in fileListReader:
            tweetList.append(row)

    #build model
    for row in tweetList:
        a = row[0].split(" ")
        for itera in a:
            elem = itera.lower()
            if elem in stop_list:
                continue
            elif any((c in chars) for c in elem):
                continue
            elif elem in currTweetDict:
                currTweetDict[elem] = 1 + currTweetDict[elem]
            else:
                currTweetDict[elem] = 1
                
    #clean dict
    clean_dict = {}
    total_score = 0
    for key in currTweetDict:
        total_score = total_score + currTweetDict[key]
    
    #only update ones with highest average score
    avg_score = float(total_score) / len(currTweetDict)
    for key in currTweetDict:
        if currTweetDict[key] > avg_score:
            clean_dict[key] = currTweetDict[key]
            
    
                            
    #write to .json file for later extraction
    full_line = "models\\" + line
    json.dump(clean_dict, open(full_line, "w"))
    i = i + 1

    #print confirmation after each iteration
    print("Created model " + str(i) + "/" + str(total) + " for " + str(line))

            

            
            
            
            
            
            
            
            
            
            

