from sklearn.base import BaseEstimator
import numpy as np
from scipy.optimize import fmin_l_bfgs_b

def loss(w, x, y):
    y_pred = x.dot(w).reshape((-1, 1))
    y_pred = np.array(y_pred, order="F")
    return np.mean(np.exp(0.1 * (y - y_pred)) - 0.1 * (y - y_pred) - 1)

def grad(w, x, y):
    y_pred = x.dot(w).reshape((-1, 1))
    y_pred = np.array(y_pred, order="F")
    gradient = 0.1 * (1 - np.exp(0.1 * (y - y_pred))) * x
    return np.mean(gradient, axis=0)

class Regressor(BaseEstimator):
    def __init__(self):
        self.x = None
        self.y = None
        self.loss = lambda w : loss(w, self.x, self.y)
        self.grad = lambda w : grad(w, self.x, self.y)
        self.w = [-1.1402e-01,-1.1753e-01,2.1598e-01,-1.7790e-01,-6.6611e-02,2.9560e-01
,2.7882e-01,-7.2882e-02,-2.6504e-02,2.9603e-01,3.5308e-02,3.3317e-02
,-7.8806e-02,-2.5856e-02,6.8541e-02,2.8024e-02,-1.2070e-02,4.5463e-02
,-8.9096e-04,-7.1983e-02,-9.0145e-03,-7.6402e-02,1.7180e-03,-3.2217e-02
,-3.5026e-02,-2.0708e-02,-2.2459e-02,-2.1028e-02,-3.0833e-02,-5.0043e-02
,-1.3473e-03,6.4909e-03,-7.8813e-02,-5.3015e-02,4.2651e-02,-8.7530e-03
,3.1952e-02,1.4258e-01,-5.5490e-02,1.4348e-01,1.4270e-01,-1.7811e-02
,-3.3676e-02,1.0132e-01,2.2109e-01,4.2911e-01,3.8355e-01,1.2695e-01
,1.0637e-01,-3.7792e-02,8.7411e-02,9.5872e-03,-1.1133e-01,-1.2180e-01
,6.6977e-02,-3.1065e-02,-1.7028e-01,6.2446e-02,-7.8310e-03,-3.4437e-03
,-2.9490e-02,-6.5672e-02,-2.0095e-02,2.1368e-02,-2.6679e-02,1.0465e-03
,1.3674e-02,-9.5771e-03,4.6047e-02,1.5365e-03,1.7693e-02,3.6143e-02
,6.1764e-03,3.0260e-03,-3.6152e-02,4.8932e-02,1.3455e-02,5.0999e-03
,2.3278e-02,5.1613e-02,-5.2128e-02,-5.2502e-02,4.9274e-02,-5.0854e-02
,1.5511e-02,4.8274e-02,-2.1759e-02,-1.7729e-01,-5.2741e-03,9.0862e-02
,7.8168e-02,-1.4612e-01,-8.6977e-02,2.2669e-01,-7.6791e-02,1.2425e-01
,-2.0287e-01,9.3506e-02,1.1964e-01,-2.2605e-01,-1.8673e-01,1.2133e-01
,-8.5483e-02,-1.4071e-01,-1.6639e-02,-1.6485e-02,4.4237e-02,6.2677e-02
,-7.9010e-03,-3.1252e-02,-2.1752e-02,-1.3324e-02,9.2529e-03,5.4149e-02
,1.0836e-02,2.5092e-02,9.7174e-03,2.1433e-02,2.8535e-02,2.9662e-02
,2.3746e-02,1.4071e-02,4.7961e-02,4.8723e-02,2.8316e-03,-2.2834e-02
,4.0014e-02,6.5662e-02,-4.3776e-02,-5.0408e-02,-5.1523e-02,-9.6991e-02
,2.3882e-02,-1.4177e-01,-1.0647e-01,1.0525e-02,-7.5560e-02,-5.7925e-02
,-3.2426e-01,-2.2728e-01,4.8467e-02,7.8170e-01]

    def fit(self, X, y):
        labels = y.reshape((-1,1))
        temp = X.copy()
        self.x = np.array(temp, order="F")
        self.y = np.array(labels, order="F")
        #self.w = np.ones((X.shape[1], 1), order="F") / 100
        self.w, _, _ = fmin_l_bfgs_b(func=self.loss, x0=self.w, fprime=self.grad)

    def predict(self, X):
        predicted = X.dot(self.w)
        return np.maximum(0, predicted.astype(int))