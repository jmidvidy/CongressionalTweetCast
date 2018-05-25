# -*- coding: utf-8 -*-
"""
Created on Fri May 25 17:42:21 2018

@author: jmidv
"""
import json
import os
import csv

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




def classifyNone(cand):
    
    #build paths
    model_path = "C:\\Users\\jmidv\\Documents\\Spring 2018\\EECS 338\\backend\\models\\"
    test_path = "C:\\Users\\jmidv\\Documents\\Spring 2018\\EECS 338\\backend\\user_tweets\\" #tweets from inputted user
    end_path = ".json"
    
    #combine paths
    cand_path = model_path + cand + end_path
    
    #load json
    cand_dict = {}
    
    cand_dict = json.load(open(cand_path))
    
    #classify
    testNames = os.listdir(test_path)
    common_words = set()
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
                
        countCand = 0
        countNot = 0
        
        #filter most common words
        curr_dict = {}
        for elem in row_tweets[0]:
            s = elem.split(" ")
            for w in s:
                word = w.lower()
                if word in stop_list:
                    continue
                elif any((c in chars) for c in word):
                    continue
                elif word not in curr_dict:
                    curr_dict[word] = 1
                else:
                    curr_dict[word] = curr_dict[word] + 1
            
        top_ten = []
        for c in range(0,20):
             curr_max = max(curr_dict, key=curr_dict.get)
             top_ten.append(curr_max)
             del curr_dict[curr_max]
           
        tt_cand = {}
        tt_notCand = {}
        for tt in top_ten:
            if tt in cand_dict:
                countCand = countCand + 1
                if tt not in tt_cand:
                    tt_cand[tt] = 1
                else:
                    tt_cand[tt] = tt_cand[tt] + 1
            else:
                countNot = countNot + 1
                if tt not in tt_notCand:
                    tt_notCand[tt] = 1
                else:
                    tt_notCand[tt] = tt_cand[tt] + 1
            


    #extract hot words
    hot_words_cand = sorted(tt_cand, key=tt_cand.get, reverse=True)
    hot_words_not = sorted(tt_notCand, key=tt_notCand.get, reverse=True)
    
    #get top 10
    hw_cand = hot_words_cand[:10]
    hw_not = hot_words_not[:10]
            
    total_len = len(tt_cand) + len(tt_notCand)
    
    cand_weight = float(len(tt_cand)) / total_len
    not_weight = float(len(tt_notCand)) / total_len
    
    countCand = float(countCand*cand_weight)
    countNot = float(countNot*not_weight)
    res = []
    
    print("countCand: " + str(int(countCand)) + " | countNot " + str(int(countNot)))
    
    if countCand > countNot:
        res.append("cand")
        res.append(hw_cand)
    else:
        res.append("not-cand")
        res.append(hw_not)
        
    return(res)
    
#a = classifyNone("SenBlumenthal")
#print(a)




    
