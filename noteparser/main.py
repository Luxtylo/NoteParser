#!/usr/bin/env python3

"""

NoteParser - A simple Python script to parse my Note Markup Language
Copyright (C) 2013  George Bryant

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

# Imports

# Definitions - allow me to change syntax later
italicTag = "*"
boldTag = "**"
underlineTag = "_"
strikethroughTag = "--"

bulletTag = "* " 		# At start of line
blockTag = "> " 	# At start of line
quoteTags = ["\"\"\"", "\'\'\'", "```"]

equationTags = ["[", "]"]
exponentTags = ["^(", ")"]
exponentSingleTag = "^"
baseTags = ["_(", ")"]
baseSingleTag = "_"

symbolDict = {
	"pi": "\03C0"
}

print(symbolDict["pi"])