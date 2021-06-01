#question-1 (sum of all element of list)
def sumList(x):
    return sum(x)
lst=list(map(int,input().split()))
print(sumList(lst))
#input-[2,3,5]   output- 10


#question2-maximum dict return
d1={}
n= int(input())
for i in range(n):
    keys=input()
    value=input()
    d1[keys]=value
d2={}
for i in range(n):
    keys=input()
    value=int(input())
    d2[keys]=value
lst=list(max(zip(d2.keys(),d2.values())))
print({lst[0]:lst[1]})


#q-3--->find consecutive ones
def cons(lst):
    c = 0
    res = 0
    for i in lst:
        if i == 0:
            c = 0
        else:
            c += 1
            res = max(res, c)
    return res
lst=list(map(int,input().split()))
print(cons(lst))
