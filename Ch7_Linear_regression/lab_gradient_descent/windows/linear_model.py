import numpy as np


class LinearRegressionGD(object):
    def __init__(self, fit_intercept=True, copy_X=True,
                 eta0=0.001, epochs=1000, weight_decay=0.9):
        self.fit_intercept = fit_intercept
        self.copy_X = copy_X
        self._eta0 = eta0
        self._epochs = epochs

        self._cost_history = []

        self._coef = None
        self._intercept = None
        self._new_X = None
        self._w_history = None
        self._weight_decay = weight_decay

    def cost(self, h, y):
        return ((1.0 / (2 * y.size)) * (h - y) ** 2).sum()

    def hypothesis_function(self, X, theta):
        return X.dot(theta)

    def gradient(self, X, y, theta):
        prediction = X.dot(theta)
        m = len(y)
        deriv_J = (1/m)*((prediction - y).reshape(-1, 1) * X).sum(axis=0)
        return deriv_J

    def fit(self, X, y):
        # Write your code
        if self.fit_intercept:
            X = np.concatenate((np.ones(len(X)).reshape(-1, 1), X), axis=1)

        self._new_X = X
        theta = np.random.normal(1, size=len(X[0]))
        self._w_history = list()

        for epoch in range(self._epochs):
            # 아래 코드를 반드시 활용할 것
            gradient = self.gradient(self._new_X, y, theta).flatten()
            theta = theta - self._eta0 * gradient
            # Write your code

            if epoch % 100 == 0:
                self._w_history.append(theta)
                cost = self.cost(
                    self.hypothesis_function(self._new_X, theta), y)
                self._cost_history.append(cost)
            self._eta0 = self._eta0 * self._weight_decay

        # Write your code
        if self.fit_intercept:
            self._coef = theta[1:]
            self._intercept = theta[0]
        else:
            self._coef = theta

        return self

    def predict(self, X):
        if self.fit_intercept:
            X = np.concatenate((np.ones(len(X)).reshape(-1, 1), X), axis=1)

        if self.fit_intercept:
            y_hat = X.dot(np.concatenate((self._intercept, self._coef), axis=None))
        else:
            y_hat = X.dot(self.coef)
        return y_hat

    @property
    def coef(self):
        return self._coef

    @property
    def intercept(self):
        return self._intercept

    @property
    def weights_history(self):
        return np.array(self._w_history)

    @property
    def cost_history(self):
        return self._cost_history
