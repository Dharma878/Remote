# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:46:08 2021

@author: DELL
"""
def flames1(Boy,Girl):
    Girl_m = Girl
    Boy_m = Boy
    Boy = Boy.lower()
    Girl = Girl.lower()
    mat = 0
    Boy = Boy.replace(" ", "")
    Girl = Girl.replace(" ", "")
    for char in range(len(Boy)):
        for cg in range(len(Girl)):
            if Girl[cg] == Boy[char]:
                mat += 1
                Girl = Girl[0:cg:]+Girl[cg+1::]
                #           print(Girl,mat)
                break
    fl=len(Boy)-mat+len(Girl)
    Fl = "flames"
#print(Fl)
    for i in range(5):
        #    print(i)
        s=fl%len(Fl)
        #    print(s)
        if s == 0:
            s = len(Fl)
        Fl = Fl[s::]+Fl[0:s-1:]
    if Fl == 'f':
        return("You are friends!!!!!")
    if Fl == 'l':
        return("{} and {} are born for each other!!!!!".format(Boy_m,Girl_m))
    if Fl == 'a':
        return("{} and {} are affectionate !!!!!".format(Boy_m,Girl_m))
    if Fl == 'm':
        return("{} and {} will tie knot soon!!!!!".format(Boy_m,Girl_m))
    if Fl == 'e':
        return("{} ,Please stay away from {} !!!!!".format(Boy_m,Girl_m))
    if Fl == 's':
        return("{}, Please say 'Hi' to your sister {} ".format(Boy_m,Girl_m))
          