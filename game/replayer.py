"""
Replayer will load json file and replay the tatic on screen
"""
from . import recorder
import tkinter
import tkinter.filedialog
import json

def load_file():
	filename = select_file()
	print("Select file:",filename)
	with open(filename, "r", encoding='utf-8') as file:
		data = json.load(file)
	return data

def select_file():
	"""Create a Tk file dialog and cleanup when finished"""
	top = tkinter.Tk()
	top.withdraw()  # hide window
	filename = tkinter.filedialog.askopenfilename(parent=top)
	top.destroy()
	return filename

class Replayer:
	def __init__(self,recorder:recorder.Recorder,json_data:dict):
		self.recorder = recorder
		self.data = json_data
		# Load data into recorder after init
		for key,value in self.data.items():
			setattr(self.recorder,key,value)
