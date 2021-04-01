def minutes(time):
    return int(time[:2])*60+int(time[3:5])
def notes(note):
    out = []
    i = 0
    for n in list(note):
        if n == "#":
           out[i-1]+=n
        else:
            out.append(n)
            i+=1
    return out

def changecode(music_): 
    music_ = music_.replace('C#', 'c')
    music_ = music_.replace('D#', 'd')
    music_ = music_.replace('F#', 'f')
    music_ = music_.replace('G#', 'g')
    music_ = music_.replace('A#', 'a')    
    return music_ 

def solution(m, musicinfos):
    music = []
    for info in musicinfos:
        temp = info.split(',')
        music.append((temp[2], changecode(temp[3]), minutes(temp[1])-minutes(temp[0])))
    music.sort(key = lambda x: x[-1], reverse = True)
    
    m = changecode(m)

    for idx, info in enumerate(music):
        title, mel, time = info
        if len(mel) > time:
            mel = mel[:time]
        else:
            mel = mel*(time//len(mel))+mel[:len(mel)]

        if m in mel:
            return title
    
    return "(None)"

m = "ABC"
minfo = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, minfo))
