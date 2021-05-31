import numpy as np
from .utils import euclidean_distance


class LinearRegression():
	"""
	Definition
	----------
		To simplify, in Linear regression, we find the correlation 
		of a given X value then use it to predict our outcome.

	Formula
	-------
		we will be using gradient descent algorithm to optimize our
		random weights at first. We can refer to it in this class
		as our fit method. Then up till the weights are updated to 
		its optimal value, we can now predict the output we are 
		expecting.

	Parameters
	----------
		x_data: np.ndarray
			our dependent data that we will fit to predict y

		y_data: np.ndarray
			our independent data that we will base our predicted data
			from.

		learning_rate: float, default=0.03
			rate where we expect our model to learn from

		n_iter: int, default=1500
			number of iterations most commonly recommended to constantly
			train our x_data

	"""
	def __init__(self, x_data, y_data, learning_rate=0.03,  n_iter=1500):
		self.learning_rate = learning_rate
		self.n_iter = n_iter
		self.n_samples = len(y)
		self.n_features = mp.size(X, 1)
		self.x_data = euclidean_distance(x_data, n_samples)
		self.y_data = [:, np.newaxis]
		self.weights = np.zeros((self.n_features + 1, 1))
		self.coef_ = None
		self.intercept_ = None

	def fit(self):
		"""
		optimization function to decrease our cost(error). Using 
		gradient descent and store its respective weights inside 
		self.weights

		Definition
		----------
			gradient descent is an optimization function most commonly
			used to decrease error from a newly generated random weight.

		Returns
		-------
			Object (self) since we are updating the instance of the obj 
			class

		"""
		for i in range(self.n_iter):
			self.weights = self.weights - (self.learning_rate / self.n_samples) \
				* self.x_data.T @ (self.x_data @ self.weights - self.y_data)

		self.intercept_ = self.weights[0]
		self.coef_ = self.weights[1:]

		return self

	def cost(self, X=None, y=None):
		"""
		Using Sum of Squared Errors (SSE)  to compute the accuracy 
		for our prediction to the actual value

		Parameters
		----------
			X: np.ndarray
				our x_data that we will pred and test the predicted
				accuraccy

			y: np.ndarray
				our y_data where we will base the accuracy of our 
				predicted data
		"""
		if X is None:
			X = self.x_data
		else:
			n_samples = np.size(X, 0)
			X = np.hstack((np.ones((n_samples, 1)), (X - np.mean(X,0)) / np.std(X,0)))

		if y is None:
			y = self.y_data
		else:
			y = y[:, np.newaxis]

		y_pred = X @ self.weights

		# SSE formula
		cost = 1 - (((y - y_pred) ** 2 ).sum() / ((y- y.mean())** 2).sum())

		return cost

	def predict(self, X):
		"""
		Using regression formula to predict each y value in arr. 

		Parameters
		----------
			X : np.ndarray
				new X test data that we will predict after doing 
				an optimization of our weights that we trained.

		"""
		n_samples = np.size(X, 0)
		y = np.hstack((np.ones((n_samples, 1)), (X-np.mean(X, 0)) \
                            / np.std(X, 0))) @ self.weights
        return y

    def get_weight(self):
    	return self.weights

class KNeighborsRegression():
	"""
	To simplify, KNeighborsRegression is a algorithm similar to the 
	kNN algorithm used in classification. The only difference is that
	predicting something in regression returns numerical predictions
	rather than classifying it to a certain class set up by classification.

	Defenition
	----------
		K Nearest neighbors is all about clumping nearest points together
		gathered from a list of distances. We can think of it as a KDTree
		where we calculate their distances using euclidean distance and 
		classify them according to their closeness to each other in a number
		of k. But in this instance, we will just predict them without 
		classifying their closeness.

	Parameters
	----------
		k : int, default 1
			specifies how many neighbors to take account when predicting

		x_data: np.ndarray
			array containing all training data for our model.

		n_row : int
			Number of observations
	"""
	def __init__(self, k=1, x_data):
		self.k = k
		self.x_data = x_data
		self.n_row = data.shape[0]

	def _distance(self, new_pt):
		"""
		Calculate the euclidean distance between a new point and
		all pointsin self.data

		Parameters
		----------
			new_pt : np.ndarray
				An array containing new_points

		"""
		new_pt = np.resize(new_point, (self.n_row, new_pt.shape[0]))
		dist = euclidean_distance(self.data[:,0:-1], new_pt)

		return dist

	def predict(self, new_pts):
		y_pred = np.zeros(new_pts.shape[0])
		
		for i, pt in enumerate(new_pts.shape[0])
			dist = self._distance(pt)
			lbl = self.data[:,-1][np.argpartition(dist, self.k)[self.k]]

			y_pred[i] = np.bincount(lbl.neighbors).argmax()

		return y_pred 
