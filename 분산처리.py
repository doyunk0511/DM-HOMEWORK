count=int(input())
result=[]
for x in range(count):
    num,sq=map(int,input().split())
    result.append((num**sq)%10)
    
print('')

for _ in range(count):
    print(result[_])