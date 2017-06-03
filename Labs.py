

import random
import copy
import time
import datetime
import numpy as np

#быстрая сортировка
def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = [elem for elem in A if elem < q]

        M = [q] * A.count(q)
        R = [elem for elem in A if elem > q]
        return QuickSort(L) + M + QuickSort(R)
# сортировка простого обмена
def mymin(mylist):
    for k in range(len(mylist) - 1):
        m = k
        i = k + 1
        while i < len(mylist):
            if mylist[i] < mylist[m]:
                m = i
            i += 1
        t = mylist[k]
        mylist[k] = mylist[m]
        mylist[m] = t

# подсчет времени
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))

#заполнение массива
def Fillingin (n):
    A = [[0] * 2 for i in range(n)]

    for x in range(n):
        A[x][0] = int(time.mktime(time.strptime(str(random.randrange(1980, 2017)) + " 0" + str(random.randrange(1, 9)), '%Y %m')))
        A[x][1] = random.randrange(0, 100)
    print(A)
    return A

#Сортировка вставками
def insertion_sort(array):
    for i in range(1, len(array)):
        while i > 0 and array[i] < array[i - 1]:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1

#Сортировка деревом
class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right
        # print('.')

    def set_value(self, val):
        self.key = val

class Tree:
    def __init__(self):
        self.root = None

    def add_key(self, val):
        if self.root == None:
            self.root = Node(val, None, None)
            return
        current = self.root
        while current:
            if val < current.key:
                if current.left == None:
                    current.left = Node(val, None, None)
                    break
                current = current.left
            elif val > current.key:
                if current.right == None:
                    current.right = Node(val, None, None)
                    break
                current = current.right
            else:
                break

    def insert(self, val):
        self.add_key(val)

    def inorder_(self):
        if self.root == None:
            return None
        stack = []
        node = self.root
        while node or stack:
            # print(stack)
            if node != None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                print(node.key , end=" ")
                node = node.right

    def inorder(self):
        self.inorder_()

    def find_(self, val):
        if self.root == None:
            self.root = Node(val, None, None)
            return
        current = self.root
        while current:
            if val <= current.key:
                if  current.key == val:
                    print(current.key)
                    break
                elif current.left == None and current.key != val:
                    print("No Value")
                current = current.left
            elif val > current.key:
                if current.key == val:
                    print(current.key)
                    break
                elif current.right == None and current.key != val:
                    print("No Value")
                current = current.right

    def find(self, val):
        self.find_(val)

def SortTree(array):
    if __name__ == "__main__":
        t = Tree()
        for i in array:
            if i == "0":
                break
            t.insert((i))
        t.inorder()

def FTree(array, val):
    if __name__ == "__main__":
        t = Tree()
        for i in array:
            if i == "0":
                break
            t.insert((i))
        #t.inorder()
        tac = time.time()
        t.find((val))
        tic = time.time()
    return tic-tac



#поиск минимума и максимума линейным поиском
def min1(array):
    sortArr = []
    for y in range(len(array)):
        if (int(array[y][0]) >= 832963409 and int(array[y][0]) <= 1180032209):
            sortArr.append(array[y][1])
    min2 = sortArr[0]
    for arg in sortArr[1:]:
        if arg < min2:
            min1 = arg
    print('Минимальное значение = ' + str(min2))

    max2 = []
    for arg in sortArr[1:]:
        if arg > min2:
            max2 = arg
    print('Максимальное значение = ' + str(max2))

#Бинарный поиск значения
def interpolationSearch(a, key):
    print('Бинарный поиск')
    sortArr = []
    for y in range(len(a)):
        if (int(a[y][0]) >= 832963409 and int(a[y][0]) <= 1180032209):
            sortArr.append(a[y][1])


    left = 0  # левая граница поиска (будем считать, что элементы массива нумеруются с нуля)
    right = len(sortArr) - 1  # правая граница поиска

    while sortArr[left] < key and key < sortArr[right]:
        mid = left + (key - sortArr[left]) * (right - left) / (sortArr[right] - sortArr[left])
        mid = int(mid)
        if sortArr[mid] < key:
            left = mid + 1
        else:
            if sortArr[mid] > key:
                right = mid - 1
            else:
                print('Индекс = ' + str(mid))
                return mid
    if sortArr[left] == key:
        print('Индекс = ' + str(left))
        return left
    else:
        if sortArr[right] == key:
            print("Индекс = " + str(right))
            return right
        else:
            print('При бинарным поиске значение не найдено')
            return -1




print('Как вы хотите работать с массивом: ВРУЧНУЮ или СЛУЧАЙНО \n Напишите ВРУЧНУЮ или СЛУЧАЙНО')
temp = input()
temp = temp.upper()

massiveToWrite = []

if (temp == 'ВРУЧНУЮ'):
    print('Создание массива вручную ')
    massiveToWrite = [[0] * 2 for i in range(10)]
    for x in range(10):
        massiveToWrite[x][0] = int(time.mktime(time.strptime(str(random.randrange(1980, 2017)) + " 0" + str(random.randrange(1, 9)), '%Y %m')))
        massiveToWrite[x][1] = int(input())
    print(massiveToWrite)

    testarrayWrite1 = copy.copy(massiveToWrite)
    testarrayWrite2 = copy.copy(massiveToWrite)
    testarrayWrite3 = copy.copy(massiveToWrite)
    testarrayWrite4 = copy.copy(massiveToWrite)

    # Быстрая сортировка и подсчет времени
    print("Быстрая сортировка и подсчет времени")
    with Profiler() as p:
        testarrayWrite1 = QuickSort(testarrayWrite1)
    print(testarrayWrite1)

    # сортировка простого обмена
    print("сортировка простого обмена")
    with Profiler() as p:
        mymin(testarrayWrite2)
    print(testarrayWrite2)

    # сортировка вставками
    print("сортировка вставками")
    with Profiler() as p:
        insertion_sort(testarrayWrite3)
    print(testarrayWrite3)

    # Сортировка деревом
    print("Сортировка деревом")
    with Profiler() as p:
        testarrayWrite4 = SortTree(testarrayWrite4)

    # Поиск минимума и максимумв в заданных случаях линейным поиском
    ArrayMinAndMaxWrite = []
    with Profiler() as p:
        ArrayMinAndMaxWrite = min1(testarrayWrite3)

    print("Какое значение вы хотите отыскать в массиве?")
    number11 = int(input())

    # Бинарный поиск значения
    interpolationSearch(testarrayWrite3, number11)

    # поиск бинарным деревом
    csvArr17 = [random.randint(0, 100) for i in range(10)]
    key = csvArr17[random.randint(0, 10)]
    print(key)
    tf = FTree(csvArr17, key)
    print('Time = ' + str(tf))




else:
    print('Создание массива из 10000 тысяч элементов')
    array10k = []
    array10k = Fillingin(10000)

    testarray10k1 = copy.copy(array10k)
    testarray10k2 = copy.copy(array10k)
    testarray10k3 = copy.copy(array10k)
    testarray10k4 = copy.copy(array10k)

    # Быстрая сортировка и подсчет времени
    print("Быстрая сортировка и подсчет времени")
    with Profiler() as p:
        testarray10k1 = QuickSort(testarray10k1)
    print(testarray10k1)

   # сортировка простого обмена
    print("сортировка простого обмена")
    with Profiler() as p:
        mymin(testarray10k2)
    print(testarray10k2)

    # сортировка вставками
    print("сортировка вставками")
    with Profiler() as p:
        insertion_sort(testarray10k3)
    print(testarray10k3)

    #Сортировка деревом
    print("Сортировка деревом")
    with Profiler() as p:
        testarray10k4 = SortTree(testarray10k4)



    #Поиск минимума и максимумв в заданных случаях линейным поиском
    ArrayMinAndMax1 = []
    with Profiler() as p:
        ArrayMinAndMax1 = min1(testarray10k3)

    #Бинарный поиск значения
    with Profiler() as p:
        interpolationSearch(testarray10k3 , 3)

    #поиск бинарным деревом
    csvArr = [random.randint(0, 100000000) for i in range(400000)]
    key =csvArr[random.randint(0, 10)]
    print(key)
    tf = FTree(csvArr, key)
    print('Time = ' + str(tf))

    print('\n')#==========================

    #Сортировка массива из 30000 тысяч элементов
    print('Создание и сортировка массива из 30000 элементов')

    array30k = []
    array30k = Fillingin(30000)

    testarray30k1 = copy.copy(array30k)
    testarray30k2 = copy.copy(array30k)
    testarray30k3 = copy.copy(array30k)
    testarray30k4 = copy.copy(array30k)

    # Быстрая сортировка и подсчет времени
    print("Быстрая сортировка и подсчет времени")
    with Profiler() as p:
        testarray30k1 = QuickSort(testarray30k1)
    print(testarray30k1)

    # сортировка простого обмена
    print("сортировка простого обмена")
    with Profiler() as p:
        mymin(testarray30k2)
    print(testarray30k2)

    # сортировка вставками
    print("сортировка вставками")
    with Profiler() as p:
        insertion_sort(testarray30k3)
    print(testarray30k3)

    # Сортировка деревом
    print("Сортировка деревом")
    with Profiler() as p:
        testarray30k4 = SortTree(testarray30k4)

    # Поиск минимума и максимумв в заданных случаях линейным поиском
    ArrayMinAndMax2 = []
    with Profiler() as p:
        ArrayMinAndMax2 = min1(testarray30k3)


    # Бинарный поиск значения
    with Profiler() as p:
        interpolationSearch(testarray30k3, 5)

    # поиск бинарным деревом
    csvArr1 = [random.randint(0, 100000000) for i in range(400000)]
    key = csvArr1[random.randint(0, 10)]
    print(key)
    tf = FTree(csvArr1, key)
    print('Time = ' + str(tf))


    print('\n')#=========================

    #Создание и сортировка массива из 50000 элементов

    print('Создание массива из 50000 элементов')

    array50k = []
    array50k = Fillingin(50000)

    testarray50k1 = copy.copy(array50k)
    testarray50k2 = copy.copy(array50k)
    testarray50k3 = copy.copy(array50k)
    testarray50k4 = copy.copy(array50k)

    # Быстрая сортировка и подсчет времени
    print("Быстрая сортировка и подсчет времени")
    with Profiler() as p:
        testarray50k1 = QuickSort(testarray50k1)
    print(testarray50k1)

    # сортировка простого обмена
    print("сортировка простого обмена")
    with Profiler() as p:
        mymin(testarray50k2)
    print(testarray50k2)

    # сортировка вставками
    print("сортировка вставками")
    with Profiler() as p:
        insertion_sort(testarray50k3)
    print(testarray50k3)

    # Сортировка деревом
    print("Сортировка деревом")
    with Profiler() as p:
        testarray50k4 = SortTree(testarray50k4)

    # Поиск минимума и максимумв в заданных случаях линейным поиском
    ArrayMinAndMax3 = []
    with Profiler() as p:
        ArrayMinAndMax3 = min1(testarray50k3)

    print("Бинарный поиск")

    # Бинарный поиск значения
    interpolationSearch(testarray50k3, 4)

    # поиск бинарным деревом
    csvArr12 = [random.randint(0, 100000000) for i in range(400000)]
    key = csvArr12[random.randint(0, 10)]
    print(key)
    tf = FTree(csvArr12, key)
    print('Time = ' + str(tf))


    print("\n")

    # Создание и сортировка массива из 70000 элементов

    print('Создание массива из 70000 элементов')

    array70k = []
    array70k = Fillingin(70000)

    testarray70k1 = copy.copy(array70k)
    testarray70k2 = copy.copy(array70k)
    testarray70k3 = copy.copy(array70k)
    testarray70k4 = copy.copy(array70k)

    # Быстрая сортировка и подсчет времени
    print("Быстрая сортировка и подсчет времени")
    with Profiler() as p:
        testarray70k1 = QuickSort(testarray70k1)
    print(testarray70k1)

    # сортировка простого обмена
    print("сортировка простого обмена")
    with Profiler() as p:
        mymin(testarray70k2)
    print(testarray70k2)

    # сортировка вставками
    print("сортировка вставками")
    with Profiler() as p:
        insertion_sort(testarray70k3)
    print(testarray70k3)

    # Сортировка деревом
    print("Сортировка деревом")
    with Profiler() as p:
        testarray70k4 = SortTree(testarray70k4)

    # Поиск минимума и максимумв в заданных случаях линейным поиском
    ArrayMinAndMax5 = []
    with Profiler() as p:
        ArrayMinAndMax5 = min1(testarray70k3)

    print("Бинарный поиск")

    # Бинарный поиск значения
    interpolationSearch(testarray70k3, 3)

    # поиск бинарным деревом
    csvArr13 = [random.randint(0, 100000000) for i in range(400000)]
    key = csvArr13[random.randint(0, 10)]
    print(key)
    tf = FTree(csvArr13, key)
    print('Time = ' + str(tf))

    # Сортировка массива из 90000 тысяч элементов
    print('Создание и сортировка массива из 90000 элементов')

    array90k = []
    array90k = Fillingin(90000)

    testarray90k1 = copy.copy(array90k)
    testarray90k2 = copy.copy(array90k)
    testarray90k3 = copy.copy(array90k)
    testarray90k4 = copy.copy(array90k)

    # Быстрая сортировка и подсчет времени
    print("Быстрая сортировка и подсчет времени")
    with Profiler() as p:
        testarray90k1 = QuickSort(testarray90k1)
    print(testarray90k1)

    # сортировка простого обмена
    print("сортировка простого обмена")
    with Profiler() as p:
        mymin(testarray90k2)
    print(testarray90k2)

    # сортировка вставками
    print("сортировка вставками")
    with Profiler() as p:
        insertion_sort(testarray90k3)
    print(testarray90k3)

    # Сортировка деревом
    print("Сортировка деревом")
    with Profiler() as p:
        testarray90k4 = SortTree(testarray90k4)

    # Поиск минимума и максимумв в заданных случаях линейным поиском
    ArrayMinAndMax6 = []
    with Profiler() as p:
        ArrayMinAndMax6 = min1(testarray90k3)

    print("Бинарный поиск")

    # Бинарный поиск значения
    interpolationSearch(testarray90k3, 5)


    #поиск ключа по дереву
    csvArr14 = [random.randint(0, 100000000) for i in range(400000)]
    key = csvArr14[random.randint(0, 10)]
    print(key)
    tf = FTree(csvArr14, key)
    print('Time = ' + str(tf))



