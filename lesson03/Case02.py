import random as r

n = r.randint(1, 10)

if n % 2 == 0:
    print('%d 偶數' % n)
else:
    print('%d 奇數' % n)
# 類三元運算子的寫法
print('%d %s' % (n, "偶數" if n % 2 == 0 else "奇數"))