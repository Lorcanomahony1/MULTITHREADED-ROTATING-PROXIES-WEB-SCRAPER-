import threading
import time
from threading import Thread



def timer(name, delay, repeat):
	print ("Timer: " + name + "Started")
	while repeat > 0:
		time.sleep(delay)
		print(name + ": " + str(time.ctime(time.time())))
		repeat -= 1
	print("Timer: " + name + "Complete")

def thesecondfunction():
	print("I'm the second function motherfucker")
	time.sleep(1)
	print("yep yep yep")

def Main(): 
	t1 = Thread(target=timer, args=("Timer1", 1, 5))
	t2 = Thread(target=thesecondfunction)
	t1.start()
	t2.start() 

	print("Main Complete")



if __name__ == '__main__': 
	Main()