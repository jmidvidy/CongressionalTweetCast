# -*- coding: utf-8 -*-
"""
Created on Mon May 14 19:26:12 2018

@author: jmidv
"""

import csv
import os
import json
import none_classify


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


def classify(e, t_h):
#    #two inputs: Later come from input
#    twitter_handle = "realDonaldTrump"
#    dem_cand = "SenatorHassan"
#    rep_cand = "ChuckGrassley"
    
    
    #have to get candidate from election
    
    twitter_handle = t_h
    
    print(twitter_handle)
    
    el = e.split("-") #split along -
    dem_cand = el[0]
    rep_cand = el[1]
    
 
    #if a candidate in this election doesn't have a twitter, run binary handle
    if dem_cand == "none":
        ret = none_classify.classifyNone(rep_cand)
        return ret
    if rep_cand == "none":
        ret = none_classify.classifyNone(dem_cand)
        return ret
    
    
    #build paths
    model_path = ".\\models\\"
    test_path = ".\\user_tweets\\" #tweets from inputted user
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
           
        tt_r = {}
        tt_d = {}
        for tt in top_ten:
            if tt in rep_dict and rep_dict[tt] > 20:
                countRep = countRep + 10
                countDem = countDem - 5
                if tt not in tt_r:
                    tt_r[tt] = 1
                else:
                    tt_r[tt] = tt_r[tt] + 1
            if tt in dem_dict and dem_dict[tt] > 20:
                countDem = countDem + 10
                countRep = countRep - 5
                if tt not in tt_d:
                    tt_d[tt] = 1
                else:
                    tt_d[tt] = tt_d[tt] + 1
    
    
        #extract hot words
        hot_words_rep = sorted(tt_r, key=tt_r.get, reverse=True)
        hot_words_dem = sorted(tt_d, key=tt_d.get, reverse=True)
        
        #get top 10
        hw_rep = hot_words_rep[:10]
        hw_dem = hot_words_dem[:10]
                
        total_len = len(rep_dict) + len(dem_dict)
        
        rep_weight = float(len(rep_dict)) / total_len
        dem_weight = float(len(dem_dict)) / total_len
        
        countRep = float(countRep*rep_weight)
        countDem = float(countDem*dem_weight)
                
        
        res = []
        print("countRep: " + str(int(countRep)) + " | countDem " + str(int(countDem)))
        if countRep > countDem:
            res.append("rep")
            res.append(hw_rep)
        else:
            res.append("dem")
            res.append(hw_dem)
            
        return(res)
     
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
    






