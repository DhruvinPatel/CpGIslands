import math




f=open('testing.txt','r')

t_sequence=[]
for line in f:

	lin=line.strip()
	for l in lin:
		t_sequence.append(l)
f=open('training.txt','r')
sequence=[]
for line in f:

	lin=line.strip()
	for l in lin:
		sequence.append(l)		
	
seq_len=len(sequence)
range_from=[]
range_to=[]


f=open('cpg_island_training.txt','r')
for line in f:
	lin=line.strip()
	spl=lin.split(' ')
	range_from.append(int(spl[0])-1)
	range_to.append(int(spl[1])-1)
#print(range_from)
#print(range_to)	
def str2int(s,i):
	plus=False
	j=0
	while (j<len(range_from)):
		if(i in range(range_from[j],range_to[j]+1)):
			plus=True
			break
		j=j+1	
	if(plus==True):
		if(s=='A'):
			return 0
		if(s=='G'):
			return 1
		if(s=='C'):
			return 2
		if(s=='T'):
			return 3
	if(plus==False):
		if(s=='A'):
			return 4
		if(s=='G'):
			return 5
		if(s=='C'):
			return 6
		if(s=='T'):
			return 7
def cpg (i):
	if((i==0) or (i==1) or(i==2) or(i==3)):
		return True
	else :
		return False	
#print(str2int(sequence[584],584))		

trans_count=[]
for i in range(0,8):
	trans_count.append([0,0,0,0,0,0,0,0])
trans_prob=[]
for i in range(0,8):
	trans_prob.append([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
#print(len(trans_count))	
start_count=[0,0,0,0,0,0,0,0]
start_prob=[float('-inf'),float('-inf'),float('-inf'),float('-inf'),0.0,0.0,0.0,0.0]
i=0
non_cpg=0.0
freq=[0,0,0,0,0,0,0,0]
for i in range(0,len(sequence)):
	if(i==len(sequence)-1):
		ch1=sequence[i]
		code1=str2int(ch1,i)
		if((code1==4) or (code1==5) or (code1==6) or (code1==7)  ):
			start_count[code1]+=1
			non_cpg+=1
	else:	
		ch1=sequence[i]
		ch2=sequence[i+1]
		code1=str2int(ch1,i)
		code2=str2int(ch2,i+1)
		trans_count[code1][code2]+=1
		freq[code1]+=1
		if((code1==4) or (code1==5) or (code1==6) or (code1==7)  ):
			start_count[code1]+=1
			non_cpg+=1

for i in range (0,8):
	for j in range(0,8):
		p=	float(trans_count[i][j])/float(freq[i]) 
		if(p==0):
			trans_prob[i][j]=float('-inf')
		else:	
			trans_prob[i][j]=math.log(p)
for i in range(4,8):
	s1=float(start_count[i])
	

	start_prob[i]=math.log(float(s1)/float(non_cpg))
	print start_prob[i]

emmision=[[0,float('-inf'),float('-inf'),float('-inf')],[float('-inf'),0,float('-inf'),float('-inf')],[float('-inf'),float('-inf'),0,float('-inf')],[float('-inf'),float('-inf'),float('-inf'),0],[0,float('-inf'),float('-inf'),float('-inf')],[float('-inf'),0,float('-inf'),float('-inf')],[float('-inf'),float('-inf'),0,float('-inf')],[float('-inf'),float('-inf'),float('-inf'),0]]	

def code(s):
  if(s=='A'):
  	return 0
  if(s=='G'):
  	return 1
  if(s=='C'):
  	return 2
  if(s=='T'):
  	return 3

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
    
    for y in states:
        V[0][y] = start_p[y] + emit_p[y][code(obs[0])]
        path[y] = [y]
    
    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for y in states:
            (prob, state) = max((V[t-1][y0] +trans_p[y0][y] +emit_p[y][code(obs[t])], y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]

        # Don't need to remember the old paths
        path = newpath
    n = 0           # if only one element is observed max is sought in the initialization values
    if len(obs) != 1:
        n = t
    
    (prob, state) = max((V[n][y], y) for y in states)
    return (prob, path[state]) 

(p,path)=viterbi(t_sequence,range(0,8),start_prob,trans_prob,emmision)


ln=len(path)
start=[]
end=[]
prev=False
for i in range(0,ln):
	cp=cpg(path[i])
	if(cp):

		if(prev==False):
			start.append(i+1)
		prev=True	
	else:
		if(prev==True):
			end.append(i)
		prev=False
f=open('output.txt','w')
print(start)
print(end)
for i in range(0,len(start)):
	f.write(str(start[i])+" "+str(end[i])+'\n')







