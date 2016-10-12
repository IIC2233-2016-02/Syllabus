''' Daemon Thread '''

import time
import random
from threading import Thread


def myfunc(i):
    sleeping_time = random.randint(1,5)
    print ("sleeping {0} sec from thread {1}".format(sleeping_time, i))
    time.sleep(sleeping_time)
    print ("finished sleeping from thread {0}".format(i))



if __name__ == '__main__':

	for i in range(10):
	    t = Thread(target=myfunc, args=(i,))
	    t.setDaemon(True)
	    t.start()
	   
	print(
	"\n"
	"Esta linea se imprime y luego de ella el programa termina"
	"de ejecutarse, justo ahi nuestros threads son brutalmente asesinados"
	"y mueren tragicamente sin alcanzar de terminar su trabajo, dormir, "
	"(Best trabajo ever). Un minuto de silencio por ellos."
	)
