class diff():
    def __init__(self):
        pass
    def difference(self,L,k):
        L1=[]
        for i in range(len(L)):
            for j in range(i,len(L)):
                if L[j]-L[i] == 2 or L[j]-L[i] == -2:
                    L1.append((L[i],L[j]))
        print(L1)
s=diff()
s.difference([1,-6,-8,-4,2,4],2)
  
