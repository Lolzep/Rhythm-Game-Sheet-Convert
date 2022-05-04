import json

import os
from os.path import join, dirname
from dotenv import load_dotenv

import tkinter as tk
from tkinter import filedialog, Text

#* .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
starting_directory = os.getenv("starting_directory")

#* Color definitions
bowiepurple = "#ddccfe"
bowiepink = "#ff35f4"
bowiegreen = "#d0ffdb"
bowieblush = "#ff7c80"
bowiewhite = "#fdfdff"

#* Determines what gamemode is selected from the json file
#! TODO: Lead this into another subclass based on gamemodes to do calculations
#* This also creates the intial window to select the json file
class Gamemode:

	# creates a window to select which files to add
	root = tk.Tk()

	def openjson(self, file): #* opens the json file that's selected from "addFile"

		with open (file, encoding="utf8") as f:
			sdata = json.load(f)
		for object in sdata:
			print(object["chartID"]) 
		# ...
		#! TODO: figure out gamemode by what's in json

	def addFile(self): #* create a file dialog window to select json files

		filename = filedialog.askopenfilename(initialdir=starting_directory, title="Select File", filetypes=(("JSON files", "*.json"), ("All Files", "*.*"))) #file browser to select)
		self.openjson(filename)

	def dialogwindow(self): #* Initialize the selection window for gamemodes

		# creates a "canvas" that changes style settings
		canvas = tk.Canvas(self.root, height=200, width=400, bg=bowiepurple)
		canvas.pack()

		frame = tk.Frame(self.root, bg=bowiewhite)
		frame.place(relwidth=1, relheight=0.8, relx=0, rely=0.25)

		# creates buttons (command=lambda allows an argument to be passed for a button press)
		openFile = tk.Button(self.root, text="Open File", padx=10,pady=5, fg="black", bg=bowiepurple, command=lambda: Gamemode.addFile(self))
		openFile.pack()

		# creates the window
		self.root.mainloop()

class calculate(Gamemode):

	def general(self):
		pass
		# TODO
		# Has calcuations that can be shared across all gamemodes

	def wacca(self):
		pass
		# TODO
	
	def iidx_sp(self):
		pass
		# TODO

	def iidx_sp(self):
		pass
		# TODO

	def iidx_dp(self):
		pass
		# TODO
	
	def sdvx(self):
		pass
		# TODO

class visualize(calculate):
	# Same format as before, but this will be used for visualizations
	# Thinking of each definition as it's own separate page on a dashboard...
	def general(self):
		pass
		# TODO
		# Has visualizations that can be shared across all gamemodes

	def wacca(self):
		pass
		# TODO
	
	def iidx_sp(self):
		pass
		# TODO

	def iidx_sp(self):
		pass
		# TODO

	def iidx_dp(self):
		pass
		# TODO
	
	def sdvx(self):
		pass
		# TODO	

#* Runs everything so far
def main():
	gm = Gamemode()
	gm1 = gm.dialogwindow()
	print(gm1)

if __name__ == "__main__":
	main()