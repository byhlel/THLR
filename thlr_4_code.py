from thlr_regex import *
from thlr_automata import *

#[Q2]

def convert_regex(enfa, origin, destination, regex):
  if len(regex.children) == 0:
    enfa.add_letter(regex.root)
    enfa.add_edge(origin, regex.root, destination)
    return (origin, destination)
  elif regex.root == '+':
    o,d = convert_regex(enfa, enfa.add_state(), enfa.add_state(), regex.children[0])
    enfa.add_edge(origin, '', o)
    enfa.add_edge(d, '', destination)
    o,d = convert_regex(enfa, enfa.add_state(), enfa.add_state(), regex.children[1])
    enfa.add_edge(origin, '', o)
    enfa.add_edge(d, '', destination)
    return (origin, destination)
  elif regex.root == '.':
    o, d1 = convert_regex(enfa, origin, enfa.add_state(), regex.children[0])
    o1, d = convert_regex(enfa, enfa.add_state(), destination, regex.children[1])
    enfa.add_edge(d1,'',o1)
    return (origin, destination)
  elif regex.root == '*':
    enfa.add_edge(origin, '', destination)
    o,d = convert_regex(enfa, enfa.add_state(), enfa.add_state(), regex.children[0])
    enfa.add_edge(origin,'',o)
    enfa.add_edge(d,'',destination)
    enfa.add_edge(d,'',o)
    return (origin, destination)

#[/Q2]
  
#[Q3]

def to_enfa(regex):
  enfa = ENFA([0,1], [0], [1], [], [])
  convert_regex(enfa, 0, 1, regex)
  return enfa

#[/Q3]

#[Q4]

def get_epsilon_closure(enfa, origin):
  set_ = set()
  set_.add(origin)
  ok = set()
  ok.add(origin)
  while(len(inc) > 0):
    now = inc.pop()
    for s in enfa.get_successors(now, ''):
      visited = False
      for y in vis:
        if(y == s):
          visited = True
          break
      if(not visited):
        set_.add(s)
      ok.add(s)
  return ok
  
#[/Q4]