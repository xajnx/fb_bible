#!/usr/bin/env python3

import json
import os
import pause
import facebook

#set variables
home = os.environ['HOME']
work = home + '/scripts/python/fb_bible/'
bible_dir = work + 'KJVJson/'
bible_log = work + 'last.log'

with open(home + '/scripts/python/apikeys', 'r') as f:
    keys = eval(f.read())

token = keys['personal']

graph = facebook.GraphAPI(access_token=token)

''' The KJV books of the Bible can be found here: https://github.com/brendancol/king-json-bible'''

bible = ['Genesis', 'Exodus', 'Lev', 'Num', 'Deut', 'Joshua', 'Judges',
         'Ruth', '1Sam', '2Sam', '1Kings', '2Kings', '1Chron', '2Chron',
         'Ezra', 'Nehemiah', 'Esther', 'Job', 'Psalms', 'Proverbs', 'Eccl',
         'Song', 'Isaiah', 'Jeremiah', 'Lament', 'Ezekiel', 'Daniel', 'Hosea',
         'Joel', 'Amos','Obadiah','Jonah','Micah','Nahum','Habakkuk','Zeph',
         'Haggai','Zech','Malachi','Matthew', 'Mark','Luke', 'John', 'Acts',
         'Romans', '1Cor', '2Cor', 'Gal', 'Eph', 'Philip', 'Hebrews','James',
         '1Peter', '2Peter', '1John', '2John', '3John', 'Jude', 'Rev']

def fb_bible():
    if os.path.exists(bible_log) == False:
        for book in bible:
            get = bible_dir + book + '.json'
            with open(get, 'r') as f:
                data = json.load(f)

            num_verse = range(len(data['verses'])-1)
            for n in num_verse:
                verse = data['verses'][n]['verse']
                chap = data['verses'][n]['chapter']
                text = data['verses'][n]['text']
                verse_str = text + ' - ' + book + str(chap) + ':' + str(verse)
                log_str = {'book': book, 'start': n}
                graph.put_object(parent_object='me', connection_name='feed', message=verse_str)

                with open(bible_log, 'w+') as log:
                    log.write(json.dumps(log_str))
                pause.hours(1)

    elif os.path.exists(bible_log) == True:
        with open(bible_log, 'r') as log:
            data = eval(log.read())
        book = data['book']
        start = data['start']
        get = bible_dir + book + '.json'
        with open(get, 'r') as f:
            data = json.load(f)

        num_verse = len(data['verses']) - 1
        for n in range(start, num_verse):
            verse = data['verses'][n]['verse']
            chap = data['verses'][n]['chapter']
            text = data['verses'][n]['text']
            verse_str = text + ' - ' + book + str(chap) + ':' + str(verse)
            log_str = {'book':book, 'start': n}
            graph.put_object(parent_object='me', connection_name='feed', message=verse_str)

            with open(bible_log, 'w+') as log:
                log.write(json.dumps(log_str))
            pause.hours(1)


if __name__ == '__main__':

    fb_bible()


























