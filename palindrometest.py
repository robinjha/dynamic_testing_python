'''
Created on Dec 19, 2014

@author: robin
'''
import unittest
import ast
import sys
from palindrome import is_palindrome
from palindrome import is_palindrome_rec

class PalindromeTest(unittest.TestCase):
    longMessage = True
    
'''
this function reads the file and converts it into a map
param : filename to be read
'''
def setUp(filename):
    print('In setUp()')
    global testsmap 
    testsmap = {}
    with open(filename,'r') as f:
        _ = next(f)
        for line in f:
            splitLine = line.split(',')
            list = []
            list.append(splitLine[1])
            list.append(splitLine[2])
            testsmap[splitLine[0]] = list
            
    print testsmap
    print('Setup complete')
            
'''
creates a test function that compares its inputs.
params - function description
params - val to be passed to the function being tested
params - expected val of the function output
params - function to be tested
'''
def make_test_function(description, val, expected, func):
    def test(self):
        if func == "is_palindrome":
            actual = is_palindrome(val)
        else:
            actual = is_palindrome_rec(val)
        self.assertEqual(actual, expected, description)
    return test


'''
Data pairs in the map is translated into distinctly named test methods.
New test cases are generated for each of the data items

'''
def main(f):
    setUp(f)
    functions = ["is_palindrome","is_palindrome_rec"]
    for f in functions:
        for name, params in testsmap.iteritems():
            print(params[0], params[1])
            test_func = make_test_function(name, params[0], ast.literal_eval(params[1]), f)
            klassname = f+'_Test_{0}'.format(name)
            globals()[klassname] = type(klassname,
                                   (PalindromeTest,),
                                   {'test_gen_{0}'.format(name): test_func})
         
'''
takes in the file with the test cases as input and runs them
'''   
if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        sys.exit("ERROR Filename must be supplied for these tests as a parameter")
    filename = sys.argv[1]
    main(filename)
    del sys.argv[1:]
    unittest.main()
    