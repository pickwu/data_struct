"""
使用python的列表，构建双端队列double-ended queue
"""
class Deque:
    def __init__(self):
        self.deque = []
    def push_front(self,element):
        # 从首端推入
        self.deque = [element] + self.deque
    def pop_front(self):
        # 从首端推出
        self.deque.pop(0)
    def push_rear(self,element):
        # 从尾端推入
        self.deque = self.deque + [element]
    def pop_rear(self):
        # 从尾端推出
        self.deque.pop()
    def is_empty(self):
        # 是否为空
        return self.deque == []
    def size(self):
        # 双端队列尺寸
        return len(self.deque)
    def seek(self):
        return self.deque

if __name__=="__main__":
    print("新建一个双端队列")
    deque_A = Deque()
    print("依次从前端front插入")
    for i in range(3,7):
        deque_A.push_front(i)
        print(f"依次从前端front插入{i}")
    print(f"查看元素{deque_A.seek()}")
    for i in range(3):
        deque_A.push_rear(i)
        print(f"依次从尾端rear插入{i}")
    print(f"查看元素{deque_A.seek()}")
    n = 3
    for i in range(n):
        deque_A.pop_front()
    print(f"从前端front推出{n}次，查看元素{deque_A.seek()}")
    n = 2
    for i in range(n):
        deque_A.pop_rear()
    print(f"从尾端rear推出{n}次，查看元素{deque_A.seek()}")
    print(f"双端队列是否为空：{deque_A.is_empty()}")