if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students = students + [[name,score]]
    mi=min([j for s,j in students])
    students = list(filter(lambda x: x[1] != mi, students))
    mi=min([j for s,j in students])
    students = list(filter(lambda x: x[1] == mi, students))
    names = [name for name,point in students]
    names.sort()
    for i in names:
        print(i)
