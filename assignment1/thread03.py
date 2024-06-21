# extending the Thread class
from time import sleep, ctime
from threading import Thread

#a custom thread class
class CustomThread(Thread):
    #override the run function
    def run(self):
        #block for a moment
        sleep(1)
        #display a message
        print(f'{ctime()} This is comming from another thread...')

#create a thread
thread = CustomThread()

#run the thread
thread.start()

#wait for the thread to finish
print(f'{ctime()} Waiting for the thread...')
thread.join()
