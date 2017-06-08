import random
import copy
import time
import datetime
import numpy as np

#Быстрая сортировка
def QuickSort(A, left, right):
    global Cqs, Mqs
    indexLow  = left + 1 # Нижний и текущий индексы
    indexHigh = right - 1
    pivotPoint = left # Верхний индекс
    pivotVal = A[left]
    i = left + 1
    while i <= right: # Пока есть область не просмотренных элементов.
        Cqs += 1
        if A[i] < pivotVal:
            pivotPoint += 1 # Если элемент меньше оси
            if i > pivotPoint: # убирает перестановки эл-та с самим собой
                Mqs += 1
                A[i], A[pivotPoint] = A[pivotPoint],A[i]# гоним его в начало интервала
                indexLow = indexLow + 1 # сужаем область слева
        i += 1
        #print(A, left, pivotPoint)
    A[left],  A[pivotPoint] = A[pivotPoint], A[left]
    Mqs += 1
    return pivotPoint

#Сортировка пузырьком
def BubbleSort(A):
    global Cbs, Mbs
    n = len(A)
    m = n-1
    while m > 0:
        for i in range(m):
            if (A[i] > A[i+1]):
                Mbs += 1
                x = A[i]
                A[i] = A[i+1]
                A[i+1] = x
            m = m - 1
            Cbs += 1

#Сортировка вставками
def InsertionSort(array):
    global Cis, Mis
    for i in range(1, len(array)):
        while (i > 0) and (array[i] < array[i - 1]):
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
            Mis += 1
            Cis += 1
        Cis += 1

#Сортировка деревом
class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

    def set_value(self, val):
        self.key = val

class Tree:
    def __init__(self):
        self.root = None

    def add_key(self, val):
        global Ct, Mt
        if self.root == None:
            self.root = Node(val, None, None)
            return
        current = self.root
        while current:
            if val <= current.key:
                Ct += 1
                if current.left == None:
                    Mt += 1
                    current.left = Node(val, None, None)
                    break
                current = current.left
            elif val > current.key:
                Ct += 1
                if current.right == None:
                    Mt += 1
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
            if node != None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                print(node.key , end=" ")
                node = node.right
        print('\n')

    def inorder(self):
        self.inorder_()

#Поиск по дереву
    def search_(self, val):
        global Ms
        if self.root == None:
            self.root = Node(val, None, None)
            return
        current = self.root
        while current:
            if val <= current.key:
                Ms += 1
                if  current.key == val:
                    #print(current.key)
                    print('Искомое значение найдено')
                    break
                elif (current.left == None) and (current.key != val):
                    print('Искомое значение не найдено')
                current = current.left
            elif val > current.key:
                Ms += 1
                if current.key == val:
                    #print(current.key)
                    print('Искомое значение найдено')
                    break
                elif (current.right == None) and (current.key != val):
                    print('Искомое значение не найдено')
                current = current.right

    def search(self, val):
        self.search_(val)

def SortTree(array):
    if __name__ == "__main__":
        t = Tree()
        for i in array:
            if i == "0":
                break
            t.insert(i)
        #t.inorder()

def STree(array, val):
    if __name__ == "__main__":
        t = Tree()
        for i in array:
            if i == "0":
                break
            t.insert((i))
        t.search(val)

#Поиск минимума и максимума линейным поиском
def MinMax(array):
    Min = array[0]
    Max = array[0]
    Mm = 0
    i = 1
    for i in range(len(array)):
        if array[i] < Min:
            Min = array[i]
        Mm += 1
        if array[i] > Max:
            Max = array[i]
        Mm += 1
    print('Минимальное значение = ' + str(Min))
    print('Максимальное значение = ' + str(Max))
    print('Число операций сравнения = ' + str(Mm))

#Бинарный поиск
def BinarySearch(li, x):
    i = 0
    j = len(li) - 1
    m = int(j / 2)
    Mbin = 0
    while (li[m] != x) and (i < j):
        if x > li[m]:
            i = m + 1
        else:
            j = m - 1
        m = int((i + j) / 2)
        Mbin += 1
    if i > j:
        print('Искомое значение не найдено\n')
    else:
        print('Искомое значение найдено под номером ' + str(m + 1))
    print('Кол-во операций сравнения ' + str(Mbin))

#Подсчет времени
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()
    def __exit__(self, type, value, traceback):
        print('Elapsed time: {:.3f} sec'.format(time.time() - self._startTime))

#Заполнение массива
def Fillingin (n):
    A = [[0] * 1 for i in range(n)]
    for x in range(n):
        A[x] = random.randrange(0, 100)
    print(A)
    return A

#..........................................................
print("Выберите метод создания массива")
print("1 - чтение из файла\n")
print("2 - ввод с клавиатуры\n")
print("3 - генерация случайного массива\n")
metod = int(input())

Mqs = 0
Cqs = 0
Mbs = 0
Cbs = 0
Mis = 0
Cis = 0
Mt = 0
Ct = 0
Ms = 0

if metod == 1:
    f = open('file.scv', 'r')
    lines = f.readlines() # Читает все строки из файла в список
    f.close()
    # Преобразовать все значения из строк в числа с плавающей точкой
    arr = [int(line) for line in lines]
    n = len(arr)

    arr1 = copy.copy(arr)
    arr2 = copy.copy(arr)
    arr3 = copy.copy(arr)
    arr4 = copy.copy(arr)
    arr5 = copy.copy(arr)

    # Быстрая сортировка и подсчет времени
    print('Быстрая сортировка и подсчет времени')
    with Profiler() as p:
        arr1 = QuickSort(arr1, 0, len(arr1) - 1)
    print(arr1)
    print('Число операций сравнения = ' + str(Cqs))
    print('Число операций перемещения = ' + str(Mqs))

    # Сортировка пузырьком
    print('Сортировка пузырьком')
    with Profiler() as p:
        BubbleSort(arr2)
    print(arr2)
    print('Число операций сравнения = ' + str(Cbs))
    print('Число операций перемещения = ' + str(Mbs))

    # Сортировка вставками
    print('Сортировка вставками')
    with Profiler() as p:
        InsertionSort(arr3)
    print(arr3)
    print('Число операций сравнения = ' + str(Cis))
    print('Число операций перемещения = ' + str(Mis))

    # Сортировка деревом
    print('Сортировка деревом')
    with Profiler() as p:
        arr4 = SortTree(arr4)
    print(arr4)
    print('Число операций сравнения = ' + str(Ct))
    print('Число операций перемещения = ' + str(Mt))

    # Линейный поиск минимума и максимума
    print('Линейный поиск минимума и максимума')
    with Profiler() as p:
        MinMax(arr5)

    # Бинарный поиск значения
    print('Бинарный поиск значения')
    k = int(input())
    with Profiler() as p:
        BinarySearch(arr3, k)

    # Поиск бинарным деревом
    print('Поиск бинарным деревом')
    key = random.randint(0, 100)
    print(key)
    Time = time.time()
    p = STree(arr5, key)
    Time = time.time() - Time
    print('Elapsed time: {:.3f} sec'.format(Time))
    print('Число операций сравнения = ' + str(Ms))

elif metod == 2:
    arr = [[0] * 1 for i in range(10)]
    for x in range(10):
        arr[x] = int(input())
    print(arr)

    arr1 = copy.copy(arr)
    arr2 = copy.copy(arr)
    arr3 = copy.copy(arr)
    arr4 = copy.copy(arr)
    arr5 = copy.copy(arr)

    # Быстрая сортировка и подсчет времени
    print('Быстрая сортировка и подсчет времени')
    with Profiler() as p:
        arr1 = QuickSort(arr1, 0, len(arr1) - 1)
    print(arr1)
    print('Число операций сравнения = ' + str(Cqs))
    print('Число операций перемещения = ' + str(Mqs))

    # Сортировка пузырьком
    print('Сортировка пузырьком')
    with Profiler() as p:
        BubbleSort(arr2)
    print(arr2)
    print('Число операций сравнения = ' + str(Cbs))
    print('Число операций перемещения = ' + str(Mbs))

    # Сортировка вставками
    print('Сортировка вставками')
    with Profiler() as p:
        InsertionSort(arr3)
    print(arr3)
    print('Число операций сравнения = ' + str(Cis))
    print('Число операций перемещения = ' + str(Mis))

    # Сортировка деревом
    print('Сортировка деревом')
    with Profiler() as p:
        arr4 = SortTree(arr4)
    print(arr4)
    print('Число операций сравнения = ' + str(Ct))
    print('Число операций перемещения = ' + str(Mt))

    # Линейный поиск минимума и максимума
    print('Линейный поиск минимума и максимума')
    with Profiler() as p:
        MinMax(arr5)

    # Бинарный поиск значения
    print('Бинарный поиск значения')
    k = int(input())
    with Profiler() as p:
        BinarySearch(arr3, k)

    # Поиск бинарным деревом
    print('Поиск бинарным деревом')
    key = random.randint(0, 100)
    print(key)
    Time = time.time()
    p = STree(arr5, key)
    Time = time.time() - Time
    print('Elapsed time: {:.3f} sec'.format(Time))
    print('Число операций сравнения = ' + str(Ms))

elif metod == 3:
    print('Введите кол-во элементов\n')
    N = int(input())
    arr = []
    arr = Fillingin(N)

    arr1 = copy.copy(arr)
    arr2 = copy.copy(arr)
    arr3 = copy.copy(arr)
    arr4 = copy.copy(arr)
    arr5 = copy.copy(arr)

    # Быстрая сортировка и подсчет времени
    print('Быстрая сортировка и подсчет времени')
    with Profiler() as p:
        arr1 = QuickSort(arr1, 0, len(arr1) - 1)
    #print(arr1)
    print('Число операций сравнения = ' + str(Cqs))
    print('Число операций перемещения = ' + str(Mqs))

    # Сортировка пузырьком
    print('Сортировка пузырьком')
    with Profiler() as p:
        BubbleSort(arr2)
    #print(arr2)
    print('Число операций сравнения = ' + str(Cbs))
    print('Число операций перемещения = ' + str(Mbs))

    # Сортировка вставками
    print('Сортировка вставками')
    with Profiler() as p:
        InsertionSort(arr3)
    #print(arr3)
    print('Число операций сравнения = ' + str(Cis))
    print('Число операций перемещения = ' + str(Mis))

    # Сортировка деревом
    print('Сортировка деревом')
    with Profiler() as p:
        arr4 = SortTree(arr4)
    #print(arr4)
    print('Число операций сравнения = ' + str(Ct))
    print('Число операций перемещения = ' + str(Mt))

    # Линейный поиск минимума и максимума
    print('Линейный поиск минимума и максимума')
    with Profiler() as p:
        MinMax(arr5)

    # Бинарный поиск значения
    print('Бинарный поиск значения')
    k = int(input())
    with Profiler() as p:
        BinarySearch(arr3, k)

    # Поиск бинарным деревом
    print('Поиск бинарным деревом')
    key = random.randint(0, 100)
    print(key)
    Time = time.time()
    p = STree(arr5, key)
    Time = time.time() - Time
    print('Число операций сравнения = ' + str(Ms))
    print('Elapsed time: {:.3f} sec'.format(Time))
else:
    print("Неверный ввод")