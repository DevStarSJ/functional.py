import math
from itertools import chain, combinations

import functional as F

def sigmoid(z):
    return 1 / (1 + math.e ** -z)

def softmax2D(M, t = 1.0):
    E = F.map(M, lambda row: [math.exp(x/t) for x in row])
    total = F.sum(F.map(E, lambda row: F.sum(row)))
    return F.map(E, lambda row: [x/total for x in row])

def softmax(M, t = 1.0):
    E = [math.exp(x/t) for x in M]
    total = F.sum(E)
    return [x/total for x in E]

def argmax(M):
    max_num = -1
    max_index = -1
    for i, v in enumerate(M):
        if v > max_num:
            max_num, max_index = v, i
    return max_index

# 약수
def divisors(origin):
    factors = [1, origin]

    current, other_side = 2, origin
    while current < other_side:
        if origin % current == 0:
            other_side = origin // current
            factors += [current, other_side]
        current += 1
    return sorted(list(set(factors)))

def sum(arg):
    if not F.is_sequence(arg): return None
    return F.reduce(arg, lambda a, b: a+b, 0)

# 삼각수 : 1 ~ n까지의 자연수 합 : 삼각형을 만들기 위해 사용된 물건의 총 수
def triangular_number(n):
    return n * (n + 1) // 2

# 콜라츠 추측 : 입력된 수가 몇번의 과정을 거쳐 1로 되는
def collatz_conjecture(n):
    acc = n
    count = 0

    while acc > 1:
        acc = acc // 2 if acc % 2 == 0 else 3 * acc + 1
        count += 1
    return count

def factorial(n):
    return 0 if n < 2 else \
           2 if n == 2 else \
           n * factorial(n-1)

# 친화수 : d = '약수 중 자기자신을 뺀 수' 라고 했을때 d(a) = b , d(b) = a 임을 만족하는 쌍
def is_amicable(a):
    b = sum(divisors(a)) - a
    if a == b:
        return False
    c = sum(divisors(b)) - b
    return a == c

# 완전수 : 진약수의 합이 자기자신과 같은 수
def is_complete(a):
    b = sum(divisors(a)) - a
    return a == b

# 초과수: 진약수의 합이 자신보다 큰 수
def is_abundant_number(a):
    b = sum(divisors(a)) - a
    return a < b

def is_prime(num):
    if num == 2 or num == 3: return True
    if num % 2 == 0 or num % 3 == 0: return False

    for i in range(3,int(math.sqrt(num))+1,2):
        if num % i == 0: return False
    return True

# 모든 요소를 1번씩 사용하면서 가능한 모든 조합들
def combination(iterable):
    if len(iterable) == 1:
        return [iterable]

    result = []
    for a in iterable:
        subs = [b for b in iterable if b != a]
        for b in combination(subs):
            result.append([a] + b)

    return result

# 입력된 집합으로 생성가능한 모든 부분집합들
def powerset(iterable):
    xs = list(iterable)
    return list(chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1)))

# 부분집합 중 주어진 갯수에 해당되는 것들
def powerset_check_length(iterable, min_num, max_num):
    return [list(x) for x in powerset(iterable) if min_num <= len(x) <= max_num]

