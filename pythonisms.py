import functools
import time

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

# output: 3
#         2
#         1
#         Liftoff!


#generator example
sum(i for i in range(10) )
#output 45


Year = (1999, 2003, 2011, 2017)
Month = ("Mar", "Jun", "Jan", "Dec")
Day = (11,21,13,5)
print zip(Year,Month,Day)

# output [(1999, 'Mar', 11), (2003, 'Jun', 21), (2011, 'Jan', 13), (2017, 'Dec', 5)]



x,y = 11, 34
print(x)
print(y)

x,y = y,x
print(x)
print(y)


#list comprehension used to filter
[i for i in range(10) if i % 2 == 0]
#output [0, 2, 4, 6, 8]