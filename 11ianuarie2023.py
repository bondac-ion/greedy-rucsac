vol,v,p,cv,ob=250,[120,40,40,100,150],[150,60,80,120,180],[],[]
n=len(v)
print(n)
for i in range(n):
    x=p[i]/v[i]
    cv.append(x)
    ob.append(0)
for i in range(len(cv)-1):
    for k in range(n-1):
        if(cv[k]<cv[k+1]):
            cv[k],cv[k+1]=cv[k+1],cv[k]
            v[k],v[k+1]=v[k+1],v[k]
            p[k],p[k+1]=p[k+1],p[k]
    n-=1
vt,ct,i=0,0,0
while((vt<vol)and(i<=5)):
    if(vt+v[i]<=vol):
        ob[i]=1
        ct+=p[i]
        vt+=v[i]
    else:
        ob[i]=(vol-vt)/v[i]
        vt=vol
        ct+=(p[i]*ob[i])
    i+=1
vt,obtemp=0,[]
lvin,lpin,lvout,lpout=[],[],[],[]
for i in range(len(v)):
    if(ob[i]==1):
        lvin.append(v[i])
        lpin.append(p[i])
        vt+=v[i]
    else:
        lvout.append(v[i])
        lpout.append(p[i])
        obtemp.append(0)
ct,n,vtemp=0,0,0
while(n<len(lvin)):
    for i in range(len(obtemp)):
        obtemp[i]=0
    q=vol-vt+lvin[n]
    i,vtemp=0,0
    while((vtemp<=q)and(i<len(lvout))):
        if(vtemp+lvout[i]<=q):
            obtemp[i]=1
            ct+=lpout[i]
            vtemp+=lvout[i]
        else:
            obtemp[i]=(q-vtemp)/lvout[i]
            vtemp=q
            ct+=(lpout[i]*ob[i])
        i+=1
    y=0
    for i in range(len(obtemp)):
        if(obtemp[i]==1):
            y+=lpout[i]
    if(y>lpin[n]):
        lvin.append(lvout[i])
        lpin.append(lpin[i])
        lvin.pop(n)
        lpin.pop(n)
    n+=1
print("Rezultat Greedy:")
t=0
for i in lpin:
    t+=i
print(t,lvin)
ct=0
def solpos(a,b,c,d,e):
    global vol,p,v
    if(v[0]*a+v[1]*b+v[2]*c+v[3]*d+v[4]*e<=vol):
        return True
    else:
        return False
def prelsol(a,b,c,d,e):
    global ct,p
    pt=p[0]*a+p[1]*b+p[2]*c+p[3]*d+p[4]*e
    if(pt>ct):
        ct=pt
        return pt
    else:
        return 0
m,l=0,[]
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    if(solpos(a,b,c,d,e)):
                        w=int(prelsol(a,b,c,d,e))
                        if(w>m):
                            m=w
                            l=[]
                            l.append(a)
                            l.append(b)
                            l.append(c)
                            l.append(d)
                            l.append(e)
print("Rezultat Trierii:")
for i in range(len(l)):
    t=l[i]*v[i]
    l.append(t)
print(m,l[5:])