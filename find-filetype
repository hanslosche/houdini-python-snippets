import os
import sys
from collections import OrderedDict


txtDir = '/Users/hlos/visuals'

dicto = OrderedDict()

for path,subdir, files in os.walk(txtDir):
    for file in files:
        if file.endswith('.mp4'):
            txtName = file.split(".")
            txtName = txtName[0]

            filePath = os.path.join(path, file)

            dicto[txtName] = filePath

print('\n'.join(dicto))
