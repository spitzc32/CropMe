import numpy as np


def euclidean_distance(p1,p2):
	"""
	returns euclidean distance between matrices	
	@params:
		p1, p2: np.ndarray
			matrices to perform operation to.
	"""
	return np.sqrt(np.sum((p1-p2)**2, axis=1))


def entropy(p):
		"""
		Will be our measurement for uncertainty in our construction 
		of descision tree
		@params:
			p: float

		"""
		if p == 0:
			return 0
		elif p == 1:
			return 0
		else:
			return -(p * np.log2(p) + (1 - p) * np.log2(1 - p))


def information_gain(left_child, right_child):
		"""
		measurement of how much info we gained when splitting a node
		using our entropy method.
		@def:
			takes in a list of classes from left and right child to return
			the information gain of our curr split
		@params:
			left_child: np.ndarray
				curr left child arr
			right_child: np.ndarray
				curr left child arr
		"""
		parent = left_child + right_child
		p_par = parent.count(1) / len(parent) if len(parent) > 0 else 0
		p_left = left_child.count(1) / len(left_child) if len(left_child) \
		> 0 else 0
		p_right = right_child.count(1) / len(right_child) if len(right_child) \
		> 0 else 0

		infogain_p = self.entropy(p_par)
		infogain_l = self.entropy(p_left)
		infogain_r = self.entropy(p_right)

		return infogain_p - len(left_child) / len(parent) * infogain_l - \
		len(right_child) / len(parent) * infogain_r
