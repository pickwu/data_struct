import time

def sum_1(n):
    # 计算从1加到n
    sumn = 0                # 执行语句：1
    start = time.time()     # 执行语句：1
    for i in range(1,n+1):  # 执行语句：n
        sumn += i           # 执行语句：1
    end = time.time()       # 执行语句：1
    return sumn,end-start   # 执行语句：1。共执行1+1+n*1+1+1 = n+4 。随着n增大，4忽略到不计，时间复杂度O(n)

def sum_2(n):
    # 计算从1加到n
    start = time.time()     # 执行语句：1
    sumn = (n * (n+1)) / 2  # 执行语句：1
    end = time.time()       # 执行语句：1
    return sumn,end-start   # 执行语句：1.

def count_time(sum_1):
    # 计算n从1000，100000，10000000的时间变化
    for i in range(3):
        init = 1000 * (100**i)
        avg = 0
        for j in range(5):
            # 计算5次的平均值
            avg += sum_1(init)[1]
        print(f"当n={init},{sum_1.__name__}平均耗时：{avg/5 * 1000 * 1000:.8f} us")


if __name__=="__main__":
    count_time(sum_1)
    count_time(sum_2)
    # 可以看到sum_1，随着训练次数增加，耗时也增加；而sum_2，不会随n增加而增加
    # 使用时间衡量算法效率，是不够客观的。因为程序运行时间跟机器，编程语言等因素都有关。
    # 为了更好的衡量算法效率，提出大O表示法。重要是起主导
    # 常见的数量级：1，log(n)，n,nlog(n),n^2,n^3,2^n
    # 算法，空间和时间的均衡
