# Aws Nassar 12027708

from threading import Thread, Condition
from time import sleep
from random import randint, random

mainCondition = Condition()
switchCondtion1 = Condition()
switchCondtion2 = Condition()
switchCondtion3 = Condition()
switchCondtion4 = Condition()
switchCondtion5 = Condition()

CAPACITY = 5
buffer1 = []
buffer2 = []
buffer3 = []
buffer4 = []
buffer5 = []

class OtherSwitch1(Thread):
    def run(self):
        global switchCondtion1
        global CAPACITY, buffer1
        global mutex1, items_consumed
        
        while True:
            switchCondtion1.acquire()
            while len(buffer1) == 0:
                switchCondtion1.wait()
            item = buffer1.pop(0)
            print("\nSwitch1 consumed", item)
            print(buffer1)
            switchCondtion1.release()
            sleep(1.5)

class OtherSwitch2(Thread):
    def run(self):
        global switchCondtion2
        global CAPACITY, buffer2
        global mutex2, items_consumed
        
        while True:
            switchCondtion2.acquire()
            while len(buffer2) == 0:
                switchCondtion2.wait()
            item = buffer2.pop(0)
            print("\nSwitch2 consumed", item)
            print(buffer2)
            switchCondtion2.release()
            sleep(1.5)

class OtherSwitch3(Thread):
    def run(self):
        global switchCondtion3
        global CAPACITY, buffer3
        global mutex3, items_consumed
        
        while True:
            switchCondtion3.acquire()
            while len(buffer3) == 0:
                switchCondtion3.wait()
            item = buffer3.pop(0)
            print("\nSwitch3 consumed", item)
            print(buffer3)
            switchCondtion3.release()
            sleep(1.5)

class OtherSwitch4(Thread):
    def run(self):
        global switchCondtion4
        global CAPACITY, buffer4
        global mutex4, items_consumed
        
        while True:
            switchCondtion4.acquire()
            while len(buffer4) == 0:
                switchCondtion4.wait()
            item = buffer4.pop(0)
            print("\nSwitch4 consumed", item)
            print(buffer4)
            switchCondtion4.release()         
            sleep(1.5)

class OtherSwitch5(Thread):
    def run(self):
        global switchCondtion5
        global CAPACITY, buffer5
        global mutex5, items_consumed
        
        while True:
            switchCondtion5.acquire()
            while len(buffer5) == 0:
                switchCondtion5.wait()
            item = buffer5.pop(0)
            print("\nSwitch5 consumed", item)
            print(buffer5)
            switchCondtion5.release()  
            sleep(1.5)

class MainSwitch(Thread):
    def run(self):
        
        global mainCondition, switchCondtion1, switchCondtion2, switchCondtion3, switchCondtion4, switchCondtion5
        global CAPACITY, buffer1, buffer2, buffer3, buffer4, buffer5 , in_index1 , in_index2 , in_index3 , in_index4 , in_index5
        global mutex1, mutex2, mutex3, mutex4, mutex5, items_produced
        while True:
            mainCondition.acquire()
            ri = randint(1, 5)
            if ri == 1:
                while len(buffer1) == CAPACITY:
                    mainCondition.wait()
                r = random()
                buffer1.append(r)
                print(f"\nMainSwitch produces {r} on buffer1")
                print(buffer1)
                mainCondition.release()
                notifyAllConditons()
                sleep(1)
                
            elif ri == 2:
                while len(buffer2) == CAPACITY:
                    mainCondition.wait()
                r = random()
                buffer2.append(r)
                print(f"\nMainSwitch produces {r} on buffer2")
                print(buffer2)
                mainCondition.release()
                notifyAllConditons()
                sleep(1)
                
            elif ri == 3:
                while len(buffer3) == CAPACITY:
                    mainCondition.wait()
                r = random()
                buffer3.append(r)
                print(f"\nMainSwitch produces {r} on buffer3")
                print(buffer3)
                mainCondition.release()
                notifyAllConditons()
                sleep(1)
                
            elif ri == 4:
                while len(buffer4) == CAPACITY:
                    mainCondition.wait()
                r = random()
                buffer4.append(r)
                print(f"\nMainSwitch produces {r} on buffer4")
                print(buffer4)
                mainCondition.release()
                notifyAllConditons()
                sleep(1)
                
            elif ri == 5:
                while len(buffer5) == CAPACITY:
                    mainCondition.wait()
                r = random()
                buffer5.append(r)
                print(f"\nMainSwitch produces {r} on buffer5")
                print(buffer5)
                mainCondition.release()
                notifyAllConditons()
                sleep(1)
            
            
def notifyAllConditons():
    with switchCondtion1:
        switchCondtion1.notify()
    with switchCondtion2:
        switchCondtion2.notify()
    with switchCondtion3:
        switchCondtion3.notify()
    with switchCondtion4:
        switchCondtion4.notify()
    with switchCondtion5:
        switchCondtion5.notify()
            

'''
 Run Starts from here
'''
    
mainswitch = MainSwitch()
switch1 = OtherSwitch1()
switch2 = OtherSwitch2()
switch3 = OtherSwitch3()
switch4 = OtherSwitch4()
switch5 = OtherSwitch5()

mainswitch.start()
switch1.start()
switch2.start()
switch3.start()
switch4.start()
switch5.start()

