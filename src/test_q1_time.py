import sys
import os
import cProfile
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from q1_time import q1_time

def profile_q1_time():
    file_path = "../../farmers-protest-tweets-2021-2-4.json"
    profiler = cProfile.Profile()
    profiler.enable()
    result = q1_time(file_path)
    profiler.disable()
    profiler.print_stats()

if __name__ == "__main__":
    profile_q1_time()
