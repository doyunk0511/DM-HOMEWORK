# 문제1 : 다음 두 집합 A와 B가 있다. A와 B의 합집합을 출력하라
'''
A={1,2,3,4,5}
B={4,5,6,7,8}

C=A.union(B)
print(C)
'''
# 문제2 : 다음 두 집합 A와 B가 있다. A와 B의 교집합을 출력하라
'''
A={10,20,30,40,50}
B={30,40,50,60,70}

C=A.intersection(B)
print(C)
'''
# 문제3 : 다음 두 집합 A와 B가 있다. A에는 있지만 B에는 없는 원소만 출력하라
'''
A={1,2,3,4,5}
B={3,4,5,6,7}

C=A.difference(B)
print(C)
'''
# 문제4 : 숫자 5개를 입력받고 중복되는 숫자를 제거하여 집합을 출력하라
'''
A=list(map(int,input().split()))

result=set(A)

print(result)
'''
# 문제5 : 이름을 입력받고 해당 이름이 집합 안에 있는지를 출력하라
'''
names={'James','Alice','Greg','Ben'}

name=input()
if name in names:
    print('있습니다')
else:
    print('없습니다')
'''
# 문제6 : 두반에 공통으로 속해있는 학생들을 출력하라
'''
class1={'민수','철수','영희','지수'}
class2={'영희','지수','준호','민수'}

print(class1.intersection(class2))
'''
# 문제7 : 두반 모두에 속하지 않은 학생들을 출력하라
'''
class1={'민수','철수','영희','지수'}
class2={'영희','지수','준호','민수'}

only_class=class1.union(class2) - class1.intersection(class2)
print(only_class)
'''
# 문제8 : 집합의 크기를 출력하라
'''
numbers={3,7,10,15,20,25,30}
print(len(numbers))
'''
# 문제9 : 0을 입력받을때까지 입력을 받고 그 이후 중복 수 없이 집합을 출력하라
'''
numbers={0}
numbers.clear()
while True:
    number=int(input())
    if number == 0:
        break
    else:
        numbers.add(number)

print(numbers)
'''
# 문제7 : 두 플레이어가 공통으로 가지고있는 아이템, 플레이어 1만 가지고있는 아이템, 
# 한명의 플레이어만 가지고있는 아이템을 각각 출력하라 (for문 사용 금지)

player1={'검','방패','물약','활','갑옷'}
player2={'물약','활','마법봉','반지','갑옷'}

print(f'공통 아이템: {player1.intersection(player2)}')
print(f'플레이어1만: {player1.difference(player2)}')
print(f'한 명만 가지고 있음: {player1.union(player2) - player1.intersection(player2)}')
