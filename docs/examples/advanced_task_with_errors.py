import sys
sys.path.append('..')
from statuscast import Cast
from time import sleep

# Advanced

task1 = Cast('Cleaning dust')
sleep(2)
task1.info('There seems to be more dust here')
sleep(2)
task1.error('Vacuum bag starts to get full')
sleep(2)
task1.complete()

# Advanced, keep all messages

task2 = Cast('Cleaning Closet', erase_exceptions=['all'])
sleep(2)
task2.info('There seems to be more dust here')
sleep(2)
task2.error('Vacuum bag starts to get full')
sleep(2)
task2.complete()

# Advanced, keep only info

task3 = Cast('Washing car', erase_exceptions=['info'])
sleep(2)
task3.info('Used another soap dispenser')
sleep(2)
task3.error('There are some scratches')
sleep(2)
task3.complete()

# Advanced, Errors

task4 = Cast('Cutting grass')
sleep(2)
task4.info('soon out of fuel')
sleep(2)
try:
    raise Exception('Out of fuel')
except Exception as e:
    task4.fail(str(e))
# Never called
sleep(2)
task4.complete()

