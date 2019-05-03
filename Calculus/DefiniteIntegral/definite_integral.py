"""
 * 
 *  Coded by Rickiarty @ GitHub 
 * 
"""

def eval_single_interval(math_func, from_x, to_x):
    if from_x > to_x:
        t = from_x
        from_x = to_x
        to_x = t
    dx = to_x - from_x
    from_y = math_func(from_x)
    to_y = math_func(to_x)
    aver_y = (from_y + to_y) / 2.0
    return aver_y * dx

def summarize_multiple_integrals(math_func, from_x, to_x, div_num):
    coef = 1
    sum = 0.0
    if from_x > to_x:
        t = from_x
        from_x = to_x
        to_x = t
        coef = -1
    dx = (float(to_x) - float(from_x)) / div_num
    for i in range(div_num):
        sum += eval_single_interval(math_func, float(from_x) + i*dx, float(from_x) + ((i+1)*dx))
    return coef * sum
