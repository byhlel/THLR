from thlr_automata import *

#[Q3]

def get_accessible_states(automaton, origin):
  inc = set()
  for lettre in automaton.alphabet:
    for suivant in automaton.get_successors(origin, letter):
      inc.add(suivant)
  vis = set() 
  while len(inc) > 0:
    while len(inc) > 0:
      vis.add(inc.pop())
    for i in vis:
      for lettre in automaton.alphabet:
        for suivant in automaton.get_successors(i, lettre):
          if not suivant in vis:
            inc.add(suivant)
  vis.add(origin)
  return vis

#[/Q3]

#[Q4]

def is_accessible(automaton, state):
  for premier in automaton.initial_states:
    if etat in get_accessible_states(automaton, premier):
      return True
  return False

#[/Q4]

#[Q5]

def is_co_accessible(automaton, state):
  for states in automaton.final_states:
    if states in get_accessible_states(automaton, state):
      return True
  
  return False

#[/Q5]

#[Q6]

def is_useful(automaton, state):
  return is_accessible(automaton, state) and is_co_accessible(automaton, state)

#[/Q6]

#[Q7]

def prune(automaton): 
  origin = automaton.all_states
  for etat in origin:
    if not is_useful(etat):
      automaton.remove_state(etat)
      
#[/Q7]