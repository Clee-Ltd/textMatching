from assets import fuzz
from assets import process

class matching:
	def __init__(self):
		return None

	def simple_ratio(self, s1: str, s2:str):
		ret_ = fuzz.ratio(s1, s2)
		return ret_

	def partial_ratio(self, s1:str, s2:str):
		ret_ = fuzz.partial_ratio(s1, s2)
		return ret_

	def short_ratio(self, s1:str, s2:str):
		ret_ = fuzz.token_sort_ratio(s1, s2)
		return ret_

	def partial_short_ratio(self, s1:str, s2:str):
		ret_ = fuzz.partial_token_sort_ratio(s1, s2)
		return ret_

	def token_ratio(self, s1:str, s2:str):
		ret_ = fuzz.token_set_ratio(s1, s2)
		return ret_

	def partial_token_ratio(self, s1:str, s2:str):
		ret_ = fuzz.partial_token_set_ratio(s1, s2)
		return ret_