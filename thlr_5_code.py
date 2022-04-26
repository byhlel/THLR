from thlr_automata import *


#[Q2]

def is_complete(nfa):
  inc= nfa.all_states
  for i in inc:
    for j in nfa.alphabet:
      if len(nfa.get_successors(i,j))==0:
        return False
  return True

#[\Q2]

#[Q3]

def is_deterministic(nfa):
  inc = nfa.all_states
  for i in inc:
    for j in nfa.alphabet:
      if len(nfa.get_successors(i,j))>1:
        return False
  return True

#[\Q3]

#[Q4]

def get_reachable_states(nfa,origins,letter):
  l=[]
  for i in origins:
    liste = nfa.get_successors(i,letter)
    for j in liste:
      l.append(j)
  return set(l)
 
#[\Q4]

#[Q5]

def accepts_from(nfa,current_states,word):
  if word=="":
    for i in current_states:
      if i in nfa.final_states:
        return True
    return False
  else:
    l=get_reachable_states(nfa,current_states,word[0])
    return accepts_from(nfa,l,word[1:])

#[\Q5]

#[Q6]

def accepts(nfa,word):
  return accepts_from(nfa,nfa.initial_states,word)

#[\Q6]

#[Q7]

def determinize(nfa):
  vis = []
  tal=[]
  tis=[]
  tfl= []
  te=[]
  tis.append(set(nfa.initial_states))
  tas.append(set(nfa.initial_states))
  inc = tis
  poubelle = nfa.add_state()
  nfa.remove_state(poubelle)
  lpoub =[]
  lpoub.append(poubelle)
  spoub= set(lpoub)
  tas.append(spoub)
  for i in nfa.alphabet:
    te.append((spoub, i, spoub))
  while len(inc)!=0:
    posi = inc[0]
    for lettre in nfa.alphabet:
      ifs= False
      liste = get_reachable_states(nfa,posi,lettre)
      for j in nfa.final_states:
        if j in liste:
          ifs= True
      if len(liste)==0:
        thisedges.append((posi,lettre,spoub))
      else:
        n= set(liste)
        if n not in tas:
          tas.append(n)
          if ifs:
            tfs.append(node)
        te.append((posi,lettre,n))
        if n not in inc:
          if n not in vis:
            incoming.append(n)
    vis.append(posi)
    inc.pop(0)
  l= symbolic_nfa_builder(tas,tis,tfs,nfa.alphabet,te)
  return l
  
#[\Q7]