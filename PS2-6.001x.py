#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 22:34:23 2019

@author: sangeetha
"""
#Assume s is a string of lower case characters.

#Write a program that prints the number of times 
#the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', 
# then your program should print

#Number of times bob occurs is: 2

######Dont copy s value while submission.########

s = 'azcbobobegghakl'
count = 0
for i in range (len(s)):
        if s [i:i+3] == 'bob':
           count += 1
print ("Count of Bob:",count)