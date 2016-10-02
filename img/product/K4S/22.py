#-*- coding: UTF-8 -*-
import os
filenames = os.listdir(os.getcwd())


for num in range(0,len(filenames)):
    name = filenames[num]
    if name[2] == '.':
        continue

    if name[1] == '-':
        newName= name[0]+'.jpg'
    else:
        newName= name[0]+name[1] +'.jpg'
    os.rename(name,newName)
