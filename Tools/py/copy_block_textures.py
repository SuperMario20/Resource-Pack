# Copyright (c) 2020 DokucraftSaga
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
import shutil

texturesPath = '../Block Textures/'
outputDir = '../Dungeons/Content/data/resourcepacks/'

os.makedirs(outputDir, exist_ok=True)

for packDir in [f.path for f in os.scandir(outputDir) if f.is_dir()]:
  os.makedirs(packDir + '/images/blocks', exist_ok=True)
  for filePath in [f.path for f in os.scandir(packDir + '/images/blocks') if f.is_file() and f.name.endswith('.png')]:
    print('Deleting ' + filePath + '...')
    os.remove(filePath)

with open('block_textures.json') as json_file:
  textures = json.load(json_file)
  for filename,copies in textures.items():
    if os.path.isfile(texturesPath + filename):
      print('Copying ' + texturesPath + filename + '...')
      for copy in copies:
        os.makedirs(os.path.dirname(outputDir + copy), exist_ok=True)
        shutil.copyfile(texturesPath + filename, outputDir + copy)