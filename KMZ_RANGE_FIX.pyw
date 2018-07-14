import os
import sys
import zipfile
from xml.dom import minidom
from Tkinter import Tk, Entry, Button, INSERT
from tkFileDialog import askopenfilename
import subprocess
import time

ftypes = [
    ('Google Earth', '*.kmz'),  
    ('All files', '*'), 
]

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename(initialdir='C:/Users/%s', filetypes=ftypes) # show an "Open" dialog box and return the path to the selected file
print(filename)
trunk_fn = filename.replace(' ', '')[:-4]


# gets name of file
root = Tk()
# Create single line text entry box
entry = Entry(root)
entry.pack()
time_save = time.strftime("_%M%S")
print time_save

# Specifying character position in entry
# - END: After last character of entry widget
# - ANCHOR: The beginning of the current selection
# - INSERT: Current text cursor position
# - "@x": Mouse coordinates

# Insert some default text
entry.insert(INSERT, '5000')

# Print the contents of entry widget to console
def print_content():
    userrange = entry.get()
    #print os.listdir(trunk_fn)
    #change file name from KMZ to ZIP
    os.rename(trunk_fn + '.kmz', trunk_fn + '.zip')
  
    #extract KMZ to get KML
    kmz = zipfile.ZipFile(trunk_fn + '.zip', 'r')
    kmz.extractall(os.path.dirname(filename))
    kmz.close()

    #cahnge KML to XML for parsing
    os.rename(trunk_fn + '.kml', trunk_fn + '.xml')

    # parses XML for 
    doc = minidom.parse(trunk_fn + '.xml')
    item = doc.getElementsByTagName('range')
    print item[0].firstChild.nodeValue
    item[0].firstChild.replaceWholeText( userrange )
    print item[0].firstChild.nodeValue

    with open(trunk_fn + '.xml','w') as f:
        f.write(doc.toxml())

    # renames XML TO KML
    os.rename(trunk_fn + '.xml', trunk_fn + time_save + '.kml')
    os.remove(trunk_fn + '.zip')
    os.startfile(trunk_fn + time_save +'.kml')
    
    root.destroy()
    sys.exit()

# Create a button that will print the contents of the entry
button = Button(root, text='Set Range', command=print_content)
button.pack()

root.mainloop()
