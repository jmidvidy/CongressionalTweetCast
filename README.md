# Congressional Tweetcast

This is the source code for the final submission for EECS 338: "Practicum in Intelligent Information Systems", Spring 2018 at Northwestern University in Evanston IL.

Congressional TweetCast was a quarter long (10-weeks) project that fulfilled the full stack "Software Development" requirement for the Computer Science Major.

This is a tool for political and electoral research. How it works is simple: users enter in a twitter handle and select a specific congressional election.

This website will then deploy sophisticated algorithms to analyze the inputted twitter user's tweets, and tell you - the user - which candidate the inputted twitter handle will vote for in the specified election.

Our algorithms are built off tweepy, machine learning in python (more specifically text analysis through a Naive Bayes Classifier), as well as your standard web tools like HTML, JavaScript, and jQuery.

Permanent Online Link: (Coming Soon)

## Contents

Within this folder are two main directories:
1. website
2. backend

As you would expect, the code for the client-side front-end is stored in "website", and the code for the server-side back-end is stored in "backend."

## Website

The "website" directory holds all of the relevant code for the front-end (client-side) portion of the project.

Here is a detailed catalog of each file:

- css/
- js/
- index.html

##### css

css is a directory that holds all of the relevant styling for the front-end.  The website is built off the free ["Lux" Boostrap](https://bootswatch.com/lux/).  This directory contains all the styling for every part of the website.

##### js/

js is also a directory.  This directory holds the relevant JavaScript that makes the website interactive and more dynamic.  Inside this directory is the standard jQuery library of functions, as well as the main js document "waypoints.js"  All animations and website flow come from this code.

#### index.html

index.html is the main HTML file for the website.  When the website is launched locally or by any remote server, this file is what the browser will access.  It contains all of the contents of the website (landing page, divs, sections, and class/id tags) as well as important text that is displayed on screen.  If you want to see how the website is strucuted, just take a look at this file and you will get the jist of it.

## Backend

The "backend" directory stores all of the relevant code for the back-end (server-side) of our project.

In short, when a twitter-handle and election is selected from the front-end, these inputs are beamed to the back-end using an AJAX call.  The back-end then does a few basic procedures, and then returns (1) a classification, and (2) a list of 10-hot words that most significantly contributed to the classification.

When inputted is passed to the back-end via Ajax, the following happens:
1. Check to see if the inputted twitter-handle is valid (that the user exists and is a public user).
   - If the inputted-user is invalid, the back-end returns an error to the front-end, which then in turn, displays the error.
   - Otherwise, the back-end proceeds to the next step.
2. Use [tweepy](http://www.tweepy.org/) to pull the last 300 tweets from the given user.
3. Create a model of the user's tweets.
4. Use the model to perform a Naive Bayes Classification of the user's tweets given the inputted election as the source of NBC's sentiment analyzer
5. Return the more likely candidate.

So that's how the project works.  Here is a detailed catalog of the files in this directory:

- models\
- user_tweets\
- ajax_caller.py
- build_NBC.py
- model_test.py
- none_classify.py
- pull_tweets.py
- username_checker.py

##### models/

This folder contains all of the models for each election.  When a specific election is inputted for classification, the NBC pulls the relevant models from this folder.

##### user_tweets/
When an inputted user's tweets are pulled, those tweets are then stored in this folder for Classification.

##### ajax_caller.py

This python file launches the local server to run this project locally.  You will need python3 and Flask installed to perform this.
##### build_NBC.py
This python file envokes the main classifier.  When called, it will classify the given inputs.
##### model_test.py
This python file constructs new models.  It can be used to update the store of models.  It is not called by front-end input.
##### none_classify.py
This python file classifies an election when one candidate does not have a twitter-handle.  Rather than comparing scores between each candidate, it just says whether the inputted twitter handle will or will not vote for the candidate in the specified election that does have a twitter handle.
##### pull_tweets.py
This python file uses tweepy to pull the relevant tweets from Twitter.
##### username_checker.py
This python file uses tweepy to perform error checking on the input from the front-end.

## Running Locally
  
1. Have python3 installed.  (do $py -m --V) from the command line to check this.
2. Have Flask installed.  (do $py -m pip install Flask). If already installed (typically is), this command will tell you.
3. Open a command prompt/terminal, and cd into the project directory, and then cd into the backend.
   - Then do, $py ajax_caller.py
   - This will create  a local host with Flask than can serve Ajax requests.  I have it set to port 8000.
4. Then, open a second command prompt/terminal, and cd into the project directory, and the cd into the website directory.
   - Then do, $py -m http.server 8001
   - This will create a local host on port 8001.  Since the website has an "index.html" file, it will automatically load the website.  Note: you cannot create this server on 8000 as that is already being used to serve the flask (doing this will make the project not work.)
5.  Finally, go to your browser (preferably Google Chrome) and do $localhost:8001 which will open the website.

If you have any problem with the website, the two command prompts will print out errors when they are triggered (watch out for Tweepy rate limits!).
