''' Задание 1. Матрицы
 Вы стажируетесь в лаборатории искусственного интеллекта, в ней вам
 поручили разработать класс Matrix для обработки и анализа данных. Ваш класс
 должен предоставлять функциональность для выполнения основных операций
 с матрицами, таких как сложение, вычитание, умножение и транспонирование.
 Это будет полезно для обработки и структурирования больших объёмов
 данных, которые используются в обучении нейронных сетей.
 Задача
 1. Создайте класс Matrix для работы с матрицами.
 Реализуйте методы:
 ○ сложения,
 ○ вычитания,
 ○ умножения,
 ○ транспонирования матрицы.
 2. Создайте несколько экземпляров класса Matrix и протестируйте
 реализованные операции.'''

from random import randint

class MyMatrix():
    def __init__(self, rows, cols, data_matrix=None):
        self.rows = rows
        self.cols = cols
        self.data_matrix = data_matrix if data_matrix is not None else [[0] * cols for _ in range(rows)]


    def  creat_matrix(self, data_matrix):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data_matrix[i][j] = randint(0, 10)
        return data_matrix

    def add(self, other):
        """Метод сложения матриц"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одинакового размера для сложения. ")
        result = MyMatrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data_matrix[i][j] = self.data_matrix[i][j] + other.data_matrix[i][j]
        return result

    def subtract(self, other):
        """Метод вычитания матриц"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одинакового размера для вычитания. ")
        result = MyMatrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data_matrix[i][j] = self.data_matrix[i][j] - other.data_matrix[i][j]
        return result

    def multiply(self, other):
        """Метод умножения матриц"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одинакового размера для умножения. ")
        result = MyMatrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data_matrix[i][j] = self.data_matrix[i][j] * other.data_matrix[i][j]
        return result

    def transpose(self):
        """Метод для транспонирования матрицы"""
        result = MyMatrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data_matrix[i][j] = self.data_matrix[j][i]

        #result = [list(i) for i in zip(*self.data_matrix)]
        return result

    def __str__(self):
        """Форматирование строк матрицы"""
        result = "\n".join(["\t".join(map(str, rows)) for rows in self.data_matrix])
        return result




matrix1 = MyMatrix(2, 2)
matrix2 = MyMatrix(2, 2)
print(matrix1.creat_matrix(matrix1.data_matrix))
print(matrix2.creat_matrix(matrix2.data_matrix))
print(f' << Сложение матриц >> \n {matrix1.add(matrix2)}')
print(f' << Вычитание матриц >> \n {matrix1.subtract(matrix2)}')
print(f' << Умножение матриц >> \n {matrix1.multiply(matrix2)}')
print(f'исходная матрица \n {matrix1} \n транспонированная матрица \n {matrix1.transpose()}')