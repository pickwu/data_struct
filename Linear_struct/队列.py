"""
使用python的列表，构建队列
"""
class Queue:
    def __init__(self):
        self.queue = []
    def push(self,element):
        # 进队
        self.queue.append(element)
    def pop(self):
        # 出队
        return self.queue.pop(0)
    def size(self):
        # 查看队列长度
        return len(self.queue)
    def is_empty(self):
        return self.queue == []
    def seek(self):
        # 查看队列元素
        return self.queue

if __name__=="__main__":
    print("初始化一个队列A")
    queue_A = Queue()
    print(f"初始化队列元素为：{queue_A.seek()}")
    print("入队操作")
    for i in range(3):
        queue_A.push(i)
        print(f"出队元素为：{i}")
    print(f"查看队列元素为：{queue_A.seek()}")
    print("出队操作")
    for i in range(3):
        print(f"出队元素为：{queue_A.pop()}")
    print(f"是否为空队列:{queue_A.is_empty()}")

