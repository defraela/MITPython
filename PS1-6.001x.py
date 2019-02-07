#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 21:51:45 2019

@author: sangeetha
"""
# Counting Vowels

#Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', program should print:
# Number of vowels: 5

######Dont copy s value while submission.########

s = 'azcbobobegghakl'
count = 0
for x in s:
        if x == 'a':
           count += 1
        if x == 'e':
           count += 1
        if x == 'i':
           count += 1
        if x == 'o':
           count += 1
        if x == 'u':
           count += 1
print ("Count of Vowels:",count)