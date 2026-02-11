import sys
import pandas as pd

# sys.argv allows us to pass arguments (like a date) from the command line
# [0] is the script name, [1] is the first actual argument
day = sys.argv[1]

print(f'Job finished successfully for day = {day}')