"""
Recorder will recorde all stages and acts on the playbook
"""
import json

class Recorder:

	def __init__(self):
		self.name = ""
		# Init recorder properties
		self.stages = 0
		self.all_stages = []
		self.court = ""

	def save_record(self, savepath:str):
		# update the stages
		self.stages = len(self.all_stages)
		# get all properties in recorder class
		data = self.__dict__
		with open(savepath, "w", encoding="utf-8") as json_file:
			json.dump(data, json_file)

