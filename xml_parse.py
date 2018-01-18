from xml.dom import minidom
doc = minidom.parse('C:\\Users\\rgarcia\\Documents\\py\\hdd.xml')
item = doc.getElementsByTagName('scale')
print item[0].firstChild.nodeValue
item[0].firstChild.replaceWholeText('replaced text')
print item[0].firstChild.nodeValue

with open('hdd.xml','w') as f:
    f.write(doc.toxml())

#for s in item: #if you want to loop try this
 #   s.firstChild.replaceWholeText('TEXT, TEXT1 , etc...')