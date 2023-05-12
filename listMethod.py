array = [1, 2, 3, 4, 5]
## 구현은 append, del, len 만 사용

def Myappend(a):
    array.append(a)

def Mypop():
    print(array[len(array)-1])
    del(array[len(array)-1])

def Myreverse():
    str = array[::-1]
    print(str)

def Myindex(findData):
    for i in range(0, len(array)):
        if array[i] == findData:
            print("인덱스 번호: "+ str(i))
        
def Myinsert(index, data):
    array.append(None)

    for i in range(len(array)-1, index, -1):
        array[i] = array[i-1]

    array[index] = data 

def Myremove(delData):
    for i in range(0, len(array)):
        if array[i] == delData:
            del(array[i])
