"""
Clive (Virtual Assistant) made by Victor Ocampo
version: 2.0.09

Stared on 2017.6 (month, estimation)

Note: If you run it from here it will not
work, it will only work if you run it "from"
the "brain" (clivebrain.py, line 25).
"""


import secrets                          #our App_id's, etc stored in this programm (fyi it only contains variables (and comments)) 
import wikipedia                        #wikipedia free online encyclopedia api
import wolframalpha                     #wolramalpha computational knoledge engine api
from wordnik import *                   #Wordnick dictionary API for PYTHON
from time import sleep                  #sleep (suspends the application for the given time)
import os                               #os module lets you run terminal commands inside clive (example: os.system('echo hello world'))
import config                           #This is used (in Clive2) to store a module wide variable
import webbrowser                       #can do stuff with a webbrowser (in python) in this project we use it to open urls (its usually used for that)
from random import *                    #random module for python
from cliveclientstuff import *          #CLIVECLIENTSTUFF!!!!!!!!!!!!!!(tm)
from clivemouth import *                #The mouth of clive
from clivebuiltinquestions import *     #The "Built in questions"
from clivebrain import *                #All clives info n' stuuff comez from here

while True:
    Main()

