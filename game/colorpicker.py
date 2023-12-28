"""
Color Picker
"""
import tkinter as tk
from tkinter import colorchooser

def OpenColorPicker() -> tuple:
	root = tk.Tk()
	app = ColorPicker(root)
	root.mainloop()
	selected_color = ColorPicker.selected_color
	return selected_color

class ColorPicker:
	# class parms
	selected_color = (255,0,0)

	def __init__(self, master):
		self.master = master
		self.master.geometry("300x100")  # 窗口大小
		self.master.title("Color Picker")
		# Color Button
		self.color_button = tk.Button(self.master, text="Pick a Color", command = self.pick_color)
		self.color_button.pack(side=tk.LEFT, pady=20,padx=10)
		# Close Button
		self.decide_button = tk.Button(self.master, text="Decide", command=self.decide_action)
		self.decide_button.pack(side=tk.LEFT, pady=20)
		# Label
		self.color_label = tk.Label(self.master, text="Color:")
		self.color_label.pack(side=tk.RIGHT, padx= 10)

	def decide_action(self):
		self.master.destroy()

	def hex_to_rgb(self,hex_color):
		hex_color_str = hex_color.lstrip('#')
		return tuple(int(hex_color_str[i:i+2], 16) for i in (0,2,4))

	def pick_color(self):
		color_code, hex_color = colorchooser.askcolor(title="Pick a Color")
		if hex_color:
			rgb_color = self.hex_to_rgb(hex_color)
			self.color_label.config(text=f"Color:{rgb_color}")
			self.color_label.config(fg=hex_color)
			self.master.configure(bg=hex_color)
			# Update Color
			ColorPicker.selected_color = rgb_color
