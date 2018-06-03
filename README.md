# Congressional Tweetcast

This is the source code for the final submission for EECS 338: "Practicum in Intelligent Information Systems", Spring 2018 at Northwestern University in Evanston IL.

Congressional TweetCast was a quarter long (10-weeks) project that fulfilled the full stack "Software Development" requirement for the Computer Science Major.

This is a tool for political and electoral research. How it works is simple: users enter in a twitter handle and select a specific congressional election.

This website will then deploy sophisticated algorithms to analyze the inputted twitter user's tweets, and tell you - the user - which candidate the inputted twitter handle will vote for in the specified election.

Our algorithms are built off tweepy, machine learning in python (more specifically text analysis through a Naive Bayes Classifier), as well as your standard web tools like HTML, JavaScript, and jQuery.

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

index.html is the main HTML file for the website.  When the website is launched locally or by any remote server, this file is what the browser will access.  It contains all of the contents of the website (landing page, divs, sections, and class/id tags) as well as important text that is displayed on screen.  If you want to see how the website is structured, just take a look at this file and you will get the jist of it.

## Backend
