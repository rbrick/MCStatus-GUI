#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minequery_gui.py
#  
#  Copyright 2014 rbrick
#  

from minecraft_query import MinecraftQuery
from os import system
from Tkinter import *
import socket

  
root = Tk()
message = Label(root, text = "Server IP")
message.pack()

e = Entry(root)
e.pack()

message = Label(root, text = "Server Port")
message.pack()

e2 = Entry(root)
e2.pack()

po = Label(root,text = "Player Count: null")
po.pack() 
def ServerStatsPlayer():
  try:
   query = MinecraftQuery(str(e.get()), int(e2.get()))
   status = query.get_status()
   po.config(text = "Player Count: " + str(status['numplayers']))
  except socket.error as ee: 
   po.config(text = "Player Count: Cannot connect to server!")
b = Button(root, text = "Get Server Info", fg = "green", command = ServerStatsPlayer)
b.pack()




root.mainloop()
