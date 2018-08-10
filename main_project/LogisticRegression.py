import numpy as np


class LogisticRegressionScratch(object):
    def __init__(self, lr=0.1, num_iter=3000, fit_intercept=True, verbose=False):
        self.lr = lr
        self.num_iter = num_iter
        self.fit_intercept = fit_intercept
        self.verbose = verbose
#X is input features   vectors likr venue,toss,etc
    def __add_intercept(self, X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis=1)

    def __sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
#h is estimated output and y is correct  output
    def cost_function(self, h, y):
        return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()

    def fit(self, X, y):
        if self.fit_intercept:
            X = self.__add_intercept(X)
        # weights initialization
        self.weight = np.zeros(X.shape[1])

        for i in range(self.num_iter):
            z = np.dot(X, self.weight)
            h = self.__sigmoid(z)
            gradient = np.dot(X.T, (h - y)) / y.size
            self.weight -= self.lr * gradient

            z = np.dot(X, self.weight)
            h = self.__sigmoid(z)
            loss = self.cost_function(h, y)

            if (self.verbose == True and i % 3000 == 0):
              print(f'loss: {loss} \t')
              print()

    def predict_prob(self, X):
        if self.fit_intercept:
            X = self.__add_intercept(X)

        return self.__sigmoid(np.dot(X, self.weight))

    def predict(self, X):
        return self.predict_prob(X).round()