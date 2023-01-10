"""La un mecanic se aduc un numar n de masini, 
care pot ocupa o anumita suprafata de parcare (aria).
Masina cu diferita arie necesita timp diferit de reparatie, dupa cum este specificat in vectori.
Sa se determine timpul minim pentru reparatia a n masini."""
timpul=[15,20,25,30]#timpul necesar pentru reparatia unui tip de masini
ar=[6,8,12,16]#aria masinii

def sol_pos(a,b,c,d):    
	if (ar[0]*a+ar[1]*b+ar[2]*c+ar[3]*d<=aria) and (a+b+c+d==n):       
		return True    
	else:       
		return False

def sol(a,b,c,d):    
	SumMin=-1    
	Sum=timpul[0]*a+timpul[1]*b+timpul[2]*c+timpul[3]*d    
	if Sum>SumMin:        
		SumMin=Sum   
	if SumMin==-1:       
		SumMin=Sum    
	return print(SumMin)

n=int(input('Dati un numar de masini:'))
aria=int(input('Dati aria totala a parcarii:'))
for a in range (0,n):    
	for b in range (0,n):       
		for c in range (0,n):            
			for d in range (0,n):                
				if (sol_pos(a,b,c,d)):                        
					sol(a,b,c,d)