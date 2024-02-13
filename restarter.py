import time
import subprocess
import os


os.chdir(os.path.dirname(os.path.realpath(__file__)))

from threading import Thread
def watch_thread():
    try:
        global file_watcher
        while True:
            if(file_watcher.is_alive()==False):
                file_watcher = Thread(target=watch_file, args=())
                file_watcher.start()
                print("started file_watcher")
            time.sleep(5)
    except:
        watch_thread()
        

def watch_file():
    while True:
        subprocess.call("python3 main.py", shell=True)
        print("process disturbed")
        time.sleep(5)
        

global file_watcher
print("working")
file_watcher = Thread(target=watch_file, args=())
file_watcher.start()
watch_thread()
