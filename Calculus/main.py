import sys
from DefiniteIntegral.definite_integral import summarize_multiple_partitions

"""
 * 
 *  Coded by Rickiarty @ GitHub 
 * 
"""

def example_math_func1(x):
    x = float(x)
    y = 3 * (x**2)
    return float(y)

from_x = float(sys.argv[1])
to_x = float(sys.argv[2])
div_num = int(sys.argv[3])

sum = summarize_multiple_partitions(example_math_func1, from_x, to_x, div_num)
print(str(sum))
