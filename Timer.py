from datetime import datetime
from time import sleep

t1 = datetime.now()
sleep(3)
t2 = datetime.now()

delta = t2-t1
print(delta.seconds)