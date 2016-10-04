def computeTransition(Pattern,Alphabet,delta) :
	m=len(Pattern)
	n=len(Alphabet)
	for q in range(m):
		for a in range(n):
			k=min(m+1,q+2)
			print("hi")
			pa=Pattern[:q]+Alphabet[a]
			while not (Pattern[:k].endswith(pa)) and k>0:
				k-=1
			delta[(Alphabet[a],q)]=k
			

def finiteAutomatonMatcher (Text,delta,m) :
	n=len(Text)
	q=0
	for i in range (1,n):
		q=delta[(q,Text[i])]
		if q==m :
			print("pattern occurs with shift ",i-m)

with open ("AESOP-TALES.txt", "r") as myfile:
	data=myfile.read()
	
import re
data=re.sub(' +',' ',data)
A=set(data);
Alphabet=list(A);
Pattern=("http");
delta ={}
computeTransition(Pattern,Alphabet,delta)
m=len(Pattern)
finiteAutomatonMatcher(data,delta,m)


