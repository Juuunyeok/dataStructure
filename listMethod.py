array = [1, 2, 3, 4, 5]
## 구현은 append, del, len 만 사용

def Myappend(a):
    array.append(a)

def Mypop():
    print(array[len(array)-1])
    del(array[len(array)-1])

Mypop()
print(array)