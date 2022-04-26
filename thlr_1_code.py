#[Q9]

def union(E,F):
	L=list(E)
	M = list(F)
	for i in range (len(M)):
		l = len(L)
		j = 0
		while j!=l and L[j]!=M[i]:
			j+=1
		if j == l:
			L.append(M[i])	 
	return set(L)

#[/Q9]

#[Q10]

def intersection(E, F):
	L = list(E)
	M = list(F)
	N=[]
	for i in range (len(M)):
		l = len(L)
		j = 0
		while j!=l and L[j]!=M[i]:
			j+=1
		if j != l:
			N.append(M[i])	 
	return set(L)

#[/Q10]

#[Q11]

def substraction(E,F):
	L=list(E)
	M = list(F)
	for i in range (len(M)):
		l = len(L)
		j = 0
		while j!=l and L[j]!=M[i]:
			j+=1
		if j != l:
			L.remove(M[i])	 
	return set(L)

#[/Q11]

#[Q12]

def diff(E,F):
	L=list(E)
	M = list(F)
	for i in range (len(M)):
		l = len(L)
		j = 0
		while j!=l and L[j]!=M[i]:
			j+=1
		if j != l:
			L.remove(M[i])
		else:
			L.append(M[i])	 
	return set(L)

#[/Q12]


#[Q13]

def sublist(L):
    if len(L) == 0:
        return [[]]
    liste = []
    for i in sublist(L[1:]):
        liste += [i, [L[0]]+i]
    return liste

#[/Q13]


#[Q14]

def power_set(E):
	M= sublist(list(E))
	for i in range (len (M)):
		M[i]=set(M[i])
	return M
	
#[/Q14]

