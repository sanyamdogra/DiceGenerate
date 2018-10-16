# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 15:44:59 2018

@author: Sanyam Dogra
"""
import random
x=2
while x==2:
    
    print("Press 1 for Roll and 0 to exit")
    x=int(input())
    if x==1:
        print("ROLLING THE DICE!")
        print (random.randint(0,6))
        x=2
    elif x==0:
        
		
		
		
import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))
done=False
while not done:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True
			
	pygame.display.flip()				