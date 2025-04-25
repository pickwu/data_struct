"""
借助python已有的列表,实现一个栈数据结构
"""
class Stack:
    def __init__(self):
        # 初始化栈
        self.stack = []
    def push(self,element):
        # 压栈
        self.stack.append(element)
    def pop(self):
        # 出栈
        return self.stack.pop()
    def seek(self):
        # 查看栈内元素
        return self.stack
    def size(self):
        # 查看栈内元素的数量
        return len(self.stack)
    def is_empty(self):
        # 是否为空栈
        return self.stack == []

if __name__=="__main__":
    print("初始化一个栈，并推入元素：0，1，2")
    stack_a = Stack()
    stack_a.push(0);stack_a.push(1);stack_a.push(2)
    print(f"查看栈的全部元素为：{stack_a.seek()}，栈内元素的数量：{stack_a.size()}")
    print(f"连续两次出栈，出栈顺序：{stack_a.pop()}，{stack_a.pop()}")
    print(f"查看栈的全部元素为：{stack_a.seek()}，栈内元素的数量：{stack_a.size()}")
    print(f"是否为空栈:{stack_a.is_empty()}")





