from memory_profiler import profile
%load_ext memory_profiler
%load_ext line_profiler 

@profile
def fact(x): return (1 if x==0 else x * fact(x-1))

@profile
def is_curious(n):
    s = str(n)
    sum = 0;
    for c in s:
        sum += fact(int(c))
    if(sum == n):
        return True
    return False

@profile
def find_curious():
    for a in range(10,11):
        # pdb.set_trace() # add pdb here
        if(is_curious(a)):
            print(a)

find_curious() 

#one should run this code as following
#kernprof -l -v script.py