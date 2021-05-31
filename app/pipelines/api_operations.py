import requests


def request(url,param,json={}, req_type):
	"""
	Function to perform API calls needed for our Data pipeline

	Parameters
	----------
		url : string
			base url needed for api call
		param : dictionary
			values for api call needed for base extension
		json : dictionary, default={}
			for POST request needed for data insertion
		req_type: string
			Type of request
	"""
	if req_type == 'GET':
		return requests.get(url, param).json()
	elif req_type == 'POST':
		return requests.post(url,data=param, json=json).text

	return

