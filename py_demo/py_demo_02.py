#水仙花数：水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number），
# 水仙花数是指一个 n 位数（n≥3 ），它的每个位上的数字的 n 次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。

#水仙花数
#for i in range(100,1000):
 #   s=str(i)
  #  if int(s[0])**3+int(s[1])**+int(s[2])**3==1:
   #     print(s,"是水仙花数")




#如果一个数恰好等于它的因子之和，则称该数为“完全数” 。各个小于它的约数（真约数,列出某数的约数，去掉该数本身，剩下的就是它的真约数）
#的和等于它本身的自然数叫做完全数（Perfect number），又称完美数或完备数。
#完美数
for i in range(1,1000):
    s=0
    for k in range(1,1):
        if i%k==0:
            s==s+k
    if i==s:
        print(i)

#Fibonacci数列
def fibonacci1(n):
    if n==0 or n==1:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)
print [fibonacci1(i) for i in range(10)]


def fibonacci3(n):
    a, b =0, 1
    for i in range(1, n+1):
        a, b = b, a+b
    return b
print[fibonacci3(i) for i in range(10)]