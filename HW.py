#HW FizzBuzz
x=0
while x < 100:
    x+=1
    if x%3==0 :
       print('Fizz')
    elif x%5==0:
        print('Buzz')
    elif x%3==0 & x%5==0:
        print('FizzBuzz')
    else:
        print(x)


#HW Change in Dict

dict={x:x**3 for x in range(50)}
print("Dict_1\n", dict, "\n")
dict_2={}
for i in dict.keys():
	o={dict[i]:i}
	dict_2.update(o)
dict=dict_2
print("Dict_2", dict_2)



#HW New list from list
m=[1,4,1,5,3,2,1,2,3,3,4,5,7,6,6,4,8,9,2,3,9]
l=[]
for i in m:
    if i not in l:
        l.append(i)
print(l)


#HW Decorator
import time
import math


def mes_time(func):
    def wrap1(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Fucntion {func.__name__} took {end-start} for execution')   #Функции потребовалось времени для завершения

    return wrap1


@mes_time
def fact(num):
    time.sleep(4)
    print(math.factorial(num))


fact(100)