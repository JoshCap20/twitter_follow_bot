# twitter_follow_bot
A follow bot for twitter using API account and access keys.

INTRODUCTION
------------
This bot uses a Python package 'tweepy' to connect with Twitter's APIs. While this bot could be ran extremely fast by removing all sleep commands from the 'time' package, these are in place to slow down the program in order to avoid being banned from Twitter by making a large amount of follow requests to its API. Please proceed with caution changing these settings as this is what I have found to be most effective, especially when ran continously on a cloud server.

REQUIREMENTS
------------
All requirements for this package are included in the file 'requirements.txt' in this directory.

USAGE
-------------
This file is a normal python file. With the installed packages from required, it should run as a python file with the command:

Download this repository to your computer.
`git clone https://github.com/JoshCap20/twitter_follow_bot.git`  
Navigate to the folder containing the file with  
`cd twitter_follow_bot`   
Run the file with Python.  
`python followbot.py`  

That's it. Make sure to configure the program to your own API keys first.


CONFIGURATION
-------------

[coming soon]

TROUBLESHOOTING
---------------

Make sure your API key includes read and write permissions. Just read permissions will result in an error since the bot will be unable to follow users.

