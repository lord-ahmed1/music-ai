labels_dir="data/labels/"
import re

def turn_clock_to_time(clock):
    processed=re.findall('[0-9]+',clock)
    return sum([int(stringTime)*((60)**(len(processed)-1-index) ) for index,stringTime in enumerate(processed)])
     

def timeline_lyrics_splitter(path):
    first=open(path,'r')
    timeline=[]
    words=[]
    for i in first:
        splited=re.findall('[0-9]+:[0-9]+',i)
        if splited!=[]:
            start=splited[0]
            end=splited[1]
            start=turn_clock_to_time(start)
            end=turn_clock_to_time(end)
            print(start,'here')

            timeline.append([start,end])
        elif  i!='\n':
                words.append(i.strip())
            
    return [timeline,words[1:]]
timeline,words=timeline_lyrics_splitter(labels_dir+"Islamalmighty.vtt")
print(timeline)
print(words)