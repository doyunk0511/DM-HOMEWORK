
N=int(input())
samples=[]
for _ in range(N):
    s,e=map(int,input().split())
    samples.append([s,e])
samples.sort(lambda x: x[1])
print(samples)

C=samples[0][1]
count=1
for j in samples:
    if C < j[0]:
        count+=1
        C=j[1]

print(count)

#미해결
seats,length=map(int,input().split())
line=list(input())

count=0
for i in range(length,seats-length):
    g=line[i]
    for j in range(-length,length+1):
        if g != line[i+j] and line[j]!='N':
            count+=1
            line[i]='N'
            line[j]='N'
            continue

print(count)