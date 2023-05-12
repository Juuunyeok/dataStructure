# 홀수 짝수의 개수
def oddEvenCount(list):
    oddCount = 0
    evenCount = 0

    for i in list:
        if i % 2 == 0:
            evenCount +=1
        else:
            oddCount +=1
    print("짝수 개수: {}".format(evenCount))
    print("홀수 개수: {}".format(oddCount))

# 중복 여부 판단
def duplicationCheck(list):
    for i in range(0, len(list)):
        for j in (i+1, len(list)):
            if list[i] == list[j]:
                return "Yes"
    return "NO"

# 최대 최소 찾기
def maxMinCheck(list):
    max = list[0]
    min = list[0]

    for i in range(1, len(list)):
        if max < list[i]:
            max = list[i]
        elif min > list[i]:
            min = list[i]
    print("최댓값: {} \n최솟값: {}".format(max, min))

arr = [1,2, 3, 4, 7, 8]
maxMinCheck(arr)