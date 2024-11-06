import numpy as np
class KalmanFilter:
    def __init__(self, F, B, H, Q, R, x0, P0):
        self.F = F  # Модель перехода состояния
        self.B = B  # Матрица управления
        self.H = H  # Модель наблюдения
        self.Q = Q  # Ковариация процесса
        self.R = R  # Ковариация измерений
        self.x = x0  # Начальное состояние
        self.P = P0  # Начальная ковариационная матрица

    def predict(self, u):
        # Прогноз состояния и ковариации состояния
        self.x = np.dot(self.F, self.x) + np.dot(self.B, u)
        self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q
        return self.x

    def update(self, z):
        # Вычисление коэффициента Калмана
        S = np.dot(np.dot(self.H, self.P), self.H.T) + self.R
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        # Обновление оценки состояния и ковариационной матрицы
        y = z - np.dot(self.H, self.x)
        self.x = self.x + np.dot(K, y)
        I = np.eye(self.P.shape[0])
        self.P = np.dot(np.dot(I - np.dot(K, self.H), self.P), (I - np.dot(K, self.H)).T) + np.dot(np.dot(K, self.R), K.T)
        return self.x