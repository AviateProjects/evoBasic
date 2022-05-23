g=open("/home/pi/projects/evoBasic/log.txt","a")
seed=0
act=0
seed=float(input("Select Seed:"))
def appen(n,a,b):
    n=str(n)
    n=n[a:b]
    n=int(n)
    return n;
def rand():
    a=act
    a=a+3/7
    f=pow(seed,2)%a
    f=appen(f,2,6)
    return f;
num=rand()
genrN=0
genrN=int(input("Input number of generations: "))
def ranVar(d):
    a=rand()
    addDo=False
    if a>5000:
        addDo=True
    if addDo:
        d+=rand()
    else:
        d-=rand()
    return d;
def genr():
    numA=ranVar(num)
    numB=ranVar(num)
    numC=ranVar(num)
    lst=[0,0,0]
    lst[0]=numA
    lst[1]=numB
    lst[2]=numC
    lst.sort(reverse=True)
    numS=lst[0]
    return numS;
i=0
g.write('\n'+"STARED NEW LOG"+'\n')
while i<genrN:
    act=+197/211
    num=(genr())
    print("Gen: "+str(i)+" Storngest Species: "+str(num))
    g.write("Gen: "+str(i)+" Storngest Species: "+str(num)+'\n')
    i+=1
g.close