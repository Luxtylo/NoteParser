"""

NoteParser - A simple Python script to parse my Note Markup Language
Copyright (C) 2013  George Bryant

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

import os
import html

if os.name == "posix":
	slashChar = "/"
elif os.name == "nt":
	slashChar = "\\"
else:
	print("OS may be unsupported")
	slashChar = "/"

class files():
	def __init__(self, inputName, outputName):
		cwd = os.getcwd() + slashChar
		notesDir = cwd + "notes" + slashChar

		self.inputFileName = str(inputName)
		self.outputFileName = str(outputName)

		self.inputFile = open(notesDir + self.inputFileName, "r")
		self.outputFile = open(notesDir + self.outputFileName, "w+")

		self.outputFile.write(html.header % inputName)

	def read(self):
		return self.inputFile

	def write(self, text):
		self.outputFile.write(str(text))

	def writeLine(self, line):
		self.outputFile.write("\n\t\t" + str(line))

	def close(self):
		self.inputFile.close()

		self.writeLine(html.footer)
		self.outputFile.close()

io = files("styleGuide.note", "test.note")