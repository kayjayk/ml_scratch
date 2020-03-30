import numpy as np
class LinearRegression(object):
    def __init__(self, fit_intercept=True, copy_X=True):
        self.fit_intercept = fit_intercept
        self.copy_X = copy_X

        self._coef = None
        self._intercept = None
        self._new_X = None

    def fit(self, X, y):
        if self.fit_intercept:
            X = np.concatenate((np.ones(len(X)).reshape(-1, 1), X), axis=1)

        w_hat = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
        # print(w_hat)

        if self.fit_intercept:
            self._coef = w_hat[1:]
            self._intercept = w_hat[0:1]
        else:
            self._coef = w_hat

        return self

    def predict(self, X):
        if self.fit_intercept:
            X = np.concatenate((np.ones(len(X)).reshape(-1, 1), X), axis=1)
            pass

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

