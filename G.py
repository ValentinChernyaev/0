__author__ = 'student'
def prostoeli(x):
    delitel=2
    while delitel<=int(x**0.5):
        if x%delitel == 0:
            return False
        delitel+=1
    return True
def sum(x):
    summa=0
    while x!=0:
        summa+=x%10
        x=x//10
    return summa
s=list(map(int,input().split()))
for j in range(s[0],s[1]+1):
    if prostoeli(j) and sum(j)==s[2]:
        print(j, end= ' ')