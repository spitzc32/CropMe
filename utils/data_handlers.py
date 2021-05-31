from __future__ import division
import numpy as np
import math
import sys


def shuffle_data(x_data, y_data, seed=None):
    """
    Random shuffle of the samples in X and y
    @params:
    	x_data: np.ndarray
    		X dependent data from derived val
    	y_data: np.ndarray
    		y independent data from derived val
    	seed: int
    		seed number for randomizing shuffling
    """
    if seed:
        np.random.seed(seed)
    idx = np.arange(X.shape[0])
    np.random.shuffle(idx)
    return X[idx], y[idx]


def train_test_split(x_data, y_data, test_size=0.5, shuffle=True, seed=None):
    """
    Split data into train and test sets for both input & output
    @params:
        x_data: np.ndarray
            input data
        y_data: np.ndarray
            output data
        test_size: int
            test size for algo
        shuffle: boolean
            shuffle data
        seed: integer
            for random seed

    """
    if shuffle:
        x_data, y_data = shuffle_data(x_data, y_data, seed)

    split_i = len(y_data) - int(len(y_data) // (1 / test_size))
    X_train, X_test = x_data[:split_i], x_data[split_i:]
    y_train, y_test = y_data[:split_i], y_data[split_i:]

    return X_train, X_test, y_train, y_test


def normalize(matrix, n_samples):
	"""
	rescales values into a range of [0,1]
	@formula:
		x_hat = (x - x_min) / (x_max - x_min)
	@params:
		matrix: np.ndarray
			matrix to convert
	"""
	np.hstack((np.ones((n_samples, 1)), (matrix - np.mean(matrix, 0) / np.std(matrix))))
