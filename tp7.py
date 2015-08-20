def main1(l):
    i = 0
    while i < len(l):
        j = i + 1
        while j < len(l):
            if l[i] == l[j]:
                l.pop(j)
            j = j+1
        i = i + 1
    print(l)
            
lista1=[3,6,2,3,1,3]
print(main1(lista1))

def main2(l):
    i = 0
    while i < len(l):
        while l[i] == l[i+1]:
            l.pop(i+1)
            if i+1==len(l):
                break
        i= i+1
    print(l)
            
lista2=[1,1,3,3,3,3,5,5,5,5,7,7,7]
print(main2(lista2))

def main3(m,n):
    t = m+n
    i = 0
    for i in range(0,len(t)):
        d = t[i]
        a = i-1
        while (a >= 0 and t[a] > d):
            t[a+1] = t[a]
            a = a-1
        t[a+1] = d 
    return t
lista3=[1,4,8]
lista4=[2,3,7]
print(main3(lista3,lista4))

def main4(m,n):
    t = 0
    i = 0
    while i<len(m):
        a = m[i]*n[i]
        t = t + a
        i = i+1
    return t

    
vector1=[1,3,4,3,4]
vector2=[2,1,5,2,1]
print(main4(vector1,vector2))
    
  