# Made by Juknum, following already existing code.py made by Dokucraft Team, all credits to them
#
# Copyright (c) 2020 Faithful Team Dungeon & DokucraftSaga
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import json
import math

texturesPath = '../UE4Project/Content/Decor/Prefabs/'

count_missing = 0
count_present = 0
total = 0

with open('prefabs_textures.json') as json_file:
	textures = json.load(json_file)
	for file,filenames in textures.items():
		for filename in filenames:
			total += 1
			if os.path.isfile(texturesPath + file + '\\' + filename):
				count_present += 1
				print('Present: ' + file + '/' + filename)
			if not os.path.isfile(texturesPath + file + '\\' + filename):
				count_missing += 1
				print('Missing: ' + file + '/' + filename)

	print('----------------------------------------')
	print('  Total textures: ' + str(total))
	print('       - Missing: ' + str(count_missing))
	print('       - Present: ' + str(count_present) + ' (' + str(math.floor((total - count_missing) * 100 / total)) + '%)')
	print('----------------------------------------')