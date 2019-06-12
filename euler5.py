


def multiply_fast(x,y):
    return x*y
def multiply_slow(x,y):
    return sum([x for _ in range(y)])

def run_both(x,y):
    return [multiply_fast(x,y),multiply_slow(x,y)]


from line_profiler import LineProfiler
profile = LineProfiler()
profile.add_function(multiply_fast)
profile.add_function(multiply_slow)

profile.enable_by_count()

for i in range(10000):
    run_both(i, i)
