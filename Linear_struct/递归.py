# 递归Recursion

# 不使用循环，怎么求列表元素和
import turtle as t
def getsum(listx):
    if len(listx) == 1:
        return listx[0]
    else:
        sum = listx[0] + getsum(listx[1:])
    return sum

print(getsum([1,2]))

def hlt(n):
    # 有A、B、C三个柱子，A有n个从小到大的圆盘，怎么将A的圆盘通过B移动到C
    if n == 1:
        print("将圆盘从A移动到C")
    elif n == 2:
        print("将圆盘从A移动到B\n")
        print("将圆盘从A移动到C\n")
        print("将圆盘从B移动到C\n")
    else:
        print("将圆盘从A移动到C")
        hlt(n-1)

def tree(branch_len):
    if branch_len > 5:
        t.forward(branch_len) # 画树干
        t.right(20) # 右倾斜20度
        tree(branch_len-15) 
