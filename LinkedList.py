class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # 연결리스트 순회
    def traverse(head):
        cur = head
        while cur.next != None:
            print(cur.data)
            cur = cur.next
        print(cur.data)

    # insert 구현
    def insert(head, index, data):
        insertData = Node(data)
        cur = head

        for i in range(0, index-1):
            cur = cur.next
        insertData.next = cur.next
        cur.next = insertData

    # delete 구현
    def delete(head, index):
        cur = head

        for i in range(0, index-1):
            cur = cur.next
        cur.next = cur.next.next
    




    