#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    #filter and remove max element
    m = max(arr)
    liste = list(filter(lambda x: x != m, arr))
    #print new max element
    print(max(liste))
