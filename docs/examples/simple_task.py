import sys
sys.path.append('..')
from statuscast import Cast
from time import sleep

# Simple

task1 = Cast('Cleaning dust')
sleep(2)
task1.complete()

# Simple, keep all messages

task2 = Cast('Cleaning Closet', erase_exceptions=['all'])
sleep(2)
task2.complete()
