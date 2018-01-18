import os
import sys
import zipfile
from xml.dom import minidom

# gets name of file
zipname = raw_input('what is the name of the KMZ?')
print '\n recomended range of 6500'
userrange = raw_input('what is the desired range?')

#change file name from KMZ to ZIP
path = 'C:\\Users\\rgarcia\\Documents\\py\\' # go back and change path value
os.rename(path + zipname + '.kmz', path + zipname + '.zip')


#extract KMZ to get KML
kmz = zipfile.ZipFile('C:\\Users\\rgarcia\\Documents\\py\\' + zipname + '.zip', 'r')
kmz.extractall('C:\\Users\\rgarcia\\Documents\\py\\')
kmz.close()

#cahnge KML to XML for parsing
os.rename(path + zipname+ '.kml', path + zipname + '.xml')

# parses XML for 
doc = minidom.parse('C:\\Users\\rgarcia\\Documents\\py\\' + zipname + '.xml')
item = doc.getElementsByTagName('range')
print item[0].firstChild.nodeValue
item[0].firstChild.replaceWholeText( userrange )
print item[0].firstChild.nodeValue

with open(zipname + '.xml','w') as f:
    f.write(doc.toxml())

# renames XML TO KML
os.rename(path + zipname +'.xml', path + zipname + '_fixed.kml')
