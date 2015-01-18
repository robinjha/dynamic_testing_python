#!/usr/bin/python

'''
Created on Dec 19, 2014

@author: robin
'''

'''
recursive implementation
param - String/word
return true if palindrome, false otherwise
'''
def is_palindrome_rec(word): 
    if len(word) == 0 or len(word) == 1: 
        return True
    elif word[0] != word[len(word)-1]:
        return False
    else: 
        return is_palindrome_rec(word[1:len(word)-1])
    

# non-recursive solution using the slice notation
def is_palindrome(num):
    if num[::-1] == num:
        return True
    else:
        return False
    
    
#print(is_palindrome_rec("abba abba"));
#print(is_palindrome("abba abba"));
