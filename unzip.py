import os
import sys
import zipfile

#os.rename('C:\\Users\\rgarcia\\Documents\\py\\test.kmz', 'C:\\Users\\rgarcia\\Documents\\py\\output.zip')
a = raw_input('name?')
kmz = zipfile.ZipFile('C:\\Users\\rgarcia\\Documents\\py\\' + a + '.zip', 'r')
kmz.extractall('C:\\Users\\rgarcia\\Documents\\py\\')
kmz.close()