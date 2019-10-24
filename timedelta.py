from datetime import *

def delta(function, *args):
    time1 = datetime.now()
    func_ret = function(*args)
    time2 = datetime.now()
    return f"Function {function.__name__} ran for {(time2 - time1).microseconds}μs, and returned: '{func_ret}'"