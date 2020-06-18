data=[("username1","phone_number1","email1"),("usernameX","phone_number1","emailX"),("usernameZ","phone_numberZ","emailZ"),("usernameY","phone_number1","email1")]
return_list=[]
index_covered=[]

for i in range(0,len(data)):
    k1=[]
    L=[]
    if i in index_covered:
        continue
    for j in range(i,len(data)):
        if len(L)==0:
            final=True
        else:
            final=any(element in data[j] for element in L)
        if final:
            k1.append(j)
            for p in data[j]:
                L.append(p)
        else:
            pass
    #print(k1)
    for h in k1:
        index_covered.append(h)
    return_list.append(k1)
print(return_list)
