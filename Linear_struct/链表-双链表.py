
# 定义双向链表的节点
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class Bi_LinkList: # 定义双向链表
    # 定义空链表
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None
    def add(self,data):
        # 从头加节点
        node = Node(data)
        if self.is_empty(): # [5,3,1]
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    def append(self,data):
        # 从尾部加节点
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while(cur.next!=None):
                cur = cur.next
            cur.next = node
            node.prev = cur
    def get_len(self):
        if self.is_empty():
            return 0
        else:
            cur = self.head
            count = 1
            while(cur.next!=None):
                cur = cur.next
                count += 1
            return count
    def insert(self,index,data):
        if index <= 0:
            self.add(data)
        elif index >= self.get_len():
            self.append(data)
        else:
            node = Node(data)
            cur = self.head
            for i in range(1,index):
                cur = cur.next
            # 后节点prev指向node；node的next指向后节点
            node.next = cur.next
            node.prev = cur
            # 以下两行不能颠倒，哎
            cur.next.prev = node
            cur.next = node
    def remove(self,index):
        if index >=0 and index < self.get_len():
            cur = self.head
            if index == 0:
                cur.next.prev = None
                self.head = cur.next
            elif index == self.get_len()-1:
                while(cur.next!=None):
                    cur = cur.next
                cur.prev.next = None
            else:
                for i in range(index):
                    cur = cur.next
                prev_node = cur.prev
                next_node = cur.next
                prev_node.next = next_node
                next_node.prev = prev_node
        else:
            print("索引错误")
    def traverse(self):
        result = []
        cur = self.head
        if self.is_empty():
            return result
        else:
            result.append(cur.data)
            while(cur.next!=None):
                cur = cur.next
                result.append(cur.data)
            return result


if __name__=="__main__":
    blist = Bi_LinkList()
    print(f"定义一个双向链表\n是否为空链表:{blist.is_empty()}\n链表长度为：{blist.len()}")
    for i in range(1, 7, 2):
        print(f"依次从头添加元素{i}") # [5,3,1]
        blist.add(i)
    print(f"链表元素为：{blist.traverse()}")
    for i in range(7, 10):
        print(f"依次从尾添加元素{i}")
        blist.append(i)
    print(f"链表元素为：{blist.traverse()}") # [-1,5,3,1,7,8,9]
    for i in range(-1,9,2):
        print(f"依次从索引{i}插入元素{i}")
        blist.insert(i,i)
        print(f"链表元素为：{blist.traverse()}")
    for i in range(-2,3):
        print(f"依次从索引{i}删除元素")
        blist.remove(i)
        print(f"链表元素为：{blist.traverse()}")

