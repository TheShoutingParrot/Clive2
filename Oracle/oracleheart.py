"""
Oracle (Virtual Assistant) made by Victor Ocampo
version: 1.0.04

Stared on 2017.6 (estimation)

Note: If you run it from here it will not
work, it will only work if you run it "from"
the "brain" (oraclebrain.py, line 25).
REMEMBER to change the credentials (api keys, etc) in the secrets file
"""


import secrets                          #our App_id's, etc stored in this programm (fyi it only contains variables (and comments)) 
import wikipedia                        #wikipedia free online encyclopedia api
import wolframalpha                     #wolramalpha computational knoledge engine api
from wordnik import *                   #Wordnick dictionary API for PYTHON
import time                               #manipulate time with python
import os                               #os module lets you run terminal commands inside clive (example: os.system('echo hello world'))
import config                           #This is used (in Clive2) to store a module wide variable
import webbrowser                       #can do stuff with a webbrowser (in python) in this project we use it to open urls (its usually used for that)
import musicplayer_youtube as music     #youtube music player for clive (Text-based)
from random import *                    #random module for python
from oracleclientstuff import *         #CLIVECLIENTSTUFF!!!!!!!!!!!!!!(tm)
from oraclemouth import *               #The mouth of clive
from oraclebuiltinquestions import *    #The "Built in questions"
from oraclebrain import *               #All clives info n' stuuff comez from here

while True:
    Main()

