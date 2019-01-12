###########################################################
'''
parse the tbody tag outerHtml in mysong of music.163.com to
songListBody.html (default name) file, and run this script
to get all song name and author name (default is "songname - 
author.mp3") of your list in fileName.txt (default name) 
file.
'''
################### configuration #########################
###########################################################
expression = '"FILENAME"'
inFile = 'songListBody.html'
outFile = 'fileName.txt'
###########################################################

from bs4 import BeautifulSoup

inFile = open(inFile, 'r', encoding='UTF-8')
outFile = open(outFile, 'w', encoding='UTF-8')

songList = BeautifulSoup(inFile, features='html.parser')
songList = songList.select('tr')

nameTD = [single.select('td:nth-of-type(2)')[0] for single in songList]
nameStr = [single.select('.ttc span.txt a b')[0]['title'] for single in nameTD]

authorTD = [single.select('td:nth-of-type(4)')[0] for single in songList]
authorStr = [single.select('span')[0]['title'] for single in authorTD]

if len(nameStr) != len(authorStr):
    print('the amount of name and author are not same')
    print('there must be some place error!')
    exit(-1)

for (singleName, singleAuthor) in zip(nameStr, authorStr):
    filename = singleName + " - " + singleAuthor + ".mp3"
    writeline = expression.replace("FILENAME", filename) + "\n"
    outFile.write(writeline)

inFile.close()
outFile.close()