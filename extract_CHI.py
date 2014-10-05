#!/usr/bin/python
#import easy to use xml parser called minidom:
from xml.dom.minidom import parseString
#all these imports are standard on most modern python implementations
 
#open the xml file for reading:
file = open('acm198.xml','r')
#convert to string:
data = file.read()
#close file because we dont need it anymore:
file.close()
#parse the xml you got from the file
dom = parseString(data)

itemlist1 = dom.getElementsByTagName('keywords')
itemlist2 = dom.getElementsByTagName('article_id')
itemlist3 = dom.getElementsByTagName('abstract')
itemlist4 = dom.getElementsByTagName('title')
itemlist5 = dom.getElementsByTagName('authors')
itemlist6 = dom.getElementsByTagName('year') 
i = 1;

for s in range(len(itemlist2)) :
	
	xmlTag1 = dom.getElementsByTagName('keywords')[s].toxml()
	xmlTag2 = dom.getElementsByTagName('article_id')[s].toxml()
	xmlTag3 = dom.getElementsByTagName('abstract')[s].toxml()
	xmlTag4 = dom.getElementsByTagName('title')[s].toxml()
	xmlTag5 = dom.getElementsByTagName('publication')[s].toxml()
	xmlTag6 = dom.getElementsByTagName('year')[s].toxml()
	
	xmlData1=xmlTag1.replace('<keywords>','').replace('</keywords>','')
	xmlData2=xmlTag2.replace('<article_id>','').replace('</article_id>','')
	xmlData3=xmlTag3.replace('<abstract>','').replace('</abstract>','')
	xmlData4=xmlTag4.replace('<title>','').replace('</title>','')
	xmlData5=xmlTag5.replace('<publication>','').replace('</publication>','')
	xmlData6=xmlTag6.replace('<year>','').replace('</year>','')
	

	if xmlData1 == "<keywords/>":
		newKeys = "Null"
	else:
		newKeys = xmlData1

	if xmlData3 == "<abstract/>":
		newAbs = "Null"
	else:
		newAbs = xmlData3

	if xmlData4 == "<title/>":
		newTitle = "Null"
	else:
		newTitle = xmlData4

	if xmlData5 == "<publication/>":
		newAuth = "Null"
	else:
		newAuth = xmlData5

	if xmlData6 == "<year/>":
		newYear = "Null"
	else:
		newYear = xmlData6

	if (xmlData5 == "Conference on Human Factors in Computing Systems"):
		print str(i)+ "	"+ xmlData2 + ",	" + newTitle +",	"+ newAuth+",	"+ newYear+",	"+ newAbs+",	"+ xmlData1
		i = i + 1

	
