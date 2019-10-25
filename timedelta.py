from datetime import *

def delta(func, *args):
    time1 = datetime.now()
    func_ret = func(*args)
    time2 = datetime.now()
    return f"Function {func.__name__} ran for {(time2 - time1).microseconds}μs, and returned: '{func_ret}'"