# -*- coding: utf-8 -*-
"""
Created on Mon May 14 19:26:12 2018

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

#two inputs: Later come from input
dem_cand = "KamalaHarris"
rep_cand = "RandPaul"

#build paths
model_path = "C:\\Users\\jmidv\\Documents\\Spring 2018\\EECS 338\\models\\"
test_path = "C:\\Users\\jmidv\\Documents\\Spring 2018\\EECS 338\\tests\\"
end_path = ".json"

#combine paths
rep_path = model_path + rep_cand + end_path
dem_path = model_path + dem_cand + end_path


#load json
dem_dict = {}
rep_dict = {}

rep_dict = json.load(open(rep_path))
dem_dict = json.load(open(dem_path))

#classify
testNames = os.listdir(test_path)
commonDem_words = set()
commonRep_words= set()
for row in testNames:
    
    row_tweets = [] #containts tweets
    row_path = test_path + row
    #read tweets
    with open(row_path,"r") as filereader:           
        #sort the input file with the csv reader and the , delimiter
        fileListReader = csv.reader(filereader, delimiter=',')
        #place holder for dictionary to be created in loop
        for elem in fileListReader:
            row_tweets.append(elem)
            
    countRep = 0
    countDem = 0
    
    #filter most common words
    curr_dict = {}
    for elem in row_tweets:
        s = elem[0].split(" ")
        for w in s:
            word = w.lower()
            if word in stop_list:
                continue
            elif any((c in chars) for c in word):
                continue
            elif word not in curr_dict:
                curr_dict[word] = 0
            else:
                curr_dict[word] = curr_dict[word] + 1
        
    top_ten = []
    for c in range(0,20):
         curr_max = max(curr_dict, key=curr_dict.get)
         top_ten.append(curr_max)
         del curr_dict[curr_max]
            
    for tt in top_ten:
        if tt in rep_dict and rep_dict[tt] > 20:
            countRep = countRep + 10
            countDem = countDem - 5
        if tt in dem_dict and dem_dict[tt] > 20:
            countDem = countDem + 10
            countRep = countRep - 5

            
    total_len = len(rep_dict) + len(dem_dict)
    
    rep_weight = float(len(rep_dict)) / total_len
    dem_weight = float(len(dem_dict)) / total_len
    
    countRep = float(countRep*rep_weight)
    countDem = float(countDem*dem_weight)
            
    print("countRep: " + str(int(countRep)) + " | countDem " + str(int(countDem)))
    if countRep > countDem:
        print(str(row) + " is a REPUBLICAN!!!!!!!")
    else:
        print(str(row) + " is a DEMOCRAT!!!!!!!")
     
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
    






