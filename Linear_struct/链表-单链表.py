
# 先定义节点，包含两属性：data和next
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Single_linked_list:
    def __init__(self):
        # 初始链表为空
        self.head = None
    def is_empty(self):
        # 是否为空
        return self.head==None
    def add(self,data):
        # 从头部添加数据
        node = Node(data)
        node.next = self.head
        self.head = node
    def append(self,data):
        # 从尾部添加数据
        node = Node(data)
        cur = self.head
        while(cur.next!=None):
            cur = cur.next
        cur.next = node
    def len(self):
        # 链表长度
        cur = self.head
        count = 0
        while(cur!=None):
            count += 1
            cur = cur.next
        return count
    def traverse(self):
        # 遍历链表
        result = []
        cur = self.head
        while(cur!=None):
            result.append(cur.data)
            cur = cur.next
        return result
    def insert(self,index,data):
        # 插入元素
        if index <= 0:
            # 当索引<=0，处理方法是一样的
            self.add(data)
        elif index >= self.len():
            self.append(data)
        else:
            cur = self.head
            cur_next = cur.next
            for i in range(1,index): # 通过以上限制了index范围[1,len)
                cur = cur.next
                cur_next = cur.next
            node = Node(data)
            cur.next = node
            node.next = cur_next
    def remove(self,index):
        # 删除指定索引位置的元素
        if index >= 0 and index < self.len():
            cur = self.head
            cur_next = cur.next
            if index == 0:
                self.head = cur_next
            else:
                for i in range(1,index):
                    cur = cur.next
                    cur_next = cur.next
                cur.next = cur_next.next
        else:
            print(f"索引{index}可能小于0或者超出链表长度限制");return


if __name__=="__main__":
    print("初始化一个单链表")
    sList = Single_linked_list()
    print(f"是否为空链表:{sList.is_empty()}")
    for i in range(1,7,2):
        print(f"依次从头添加元素{i}")
        sList.add(i)
    print(f"链表元素为：{sList.traverse()}")
    for i in range(7,10):
        print(f"依次从尾添加元素{i}")
        sList.append(i)
    print(f"链表元素为：{sList.traverse()}")
    for i in [-1,2,9,0]:
        print(f"依次从索引{i}插入元素{i}")
        sList.insert(i,i)
        print(f"链表元素为：{sList.traverse()}")
    for i in [-1,2,9,0]:
        print(f"依次从索引{i}删除元素")
        sList.remove(i)
        print(f"链表元素为：{sList.traverse()}")



