#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 22:44:53 2019

@author: sangeetha
"""

#Assume s is a string of lower case characters.

#Write a program that prints the longest substring of s 
#in which the letters occur in alphabetical order.
#For example, if s = 'azcbobobegghakl', then your program should print

#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. 
#For example, if s = 'abcbcd', then your program should print

#Longest substring in alphabetical order is: abc

######Dont copy s value while submission.########

#The current string of increasing letters and the currently longest string
#Both strings are initialized with the first letter
#Then we iterate over the input string s 
#If the current character c fulfills the requirement c >= current[-1], 
#we add it to the current solution.
#We possibly store the current string as longest
#If c does not fulfill the ordering requirement, we start with a 
#new solution current = c.
#Finally, we print the longest string

s = 'bcdabycdeaeff'
longest = s[0]
current = s[0]
for c in s[1:]:
    if c >= current[-1]:
        current += c
        if len(current) > len(longest):
            longest = current
    else:
        current = c
print ("Longest substring in alphabetical order is:", longest)