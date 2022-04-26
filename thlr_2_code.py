from thlr_regex import *

#[Q7]

def regex_to_string(regex):
     if (len(regex.children) == 2):
         return "(" + regex_to_string(regex.children[0]) + regex.root + regex_to_string(regex.children[1]) + ")"
     elif (len(regex.children) == 1):
         return "("+ regex_to_string(regex.children[0]) + ")" + regex.root
     else:
         return regex.root
         
 #[/Q7]