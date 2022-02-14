def fact(n):
    # 引用: https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

least = int(input("aの最小値を入力: "))
if least < 2:
    import sys
    sys.exit("最小値は2以上を入力してください")
up = int(input("aの最大値を入力: "))
if least >= up:
    import sys
    sys.exit("最大値と最小値の差を1以上にしてください")


least = int(least)
up = int(up)

print()
print("min:", least)
print("max:", up)
print()


for i in range(least, up + 1):
    print(fact(i), fact(i)[-1][0])
    fl = fact(i)
    k = 1 # 仮置き

    for j in range(len(fl)):
        k *= (fl[j][0] ** (fl[j][1] + 1) - 1) / (fl[j][0] - 1)

    print(i,fl[-1][0], int(k))
