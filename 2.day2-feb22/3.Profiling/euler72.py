# from memory_profiler import profile
from math import ceil,sqrt
# %load_ext memory_profiler
# %load_ext line_profiler 

@profile
def gen_primes(n):
    
    l = range(2,n)
    primes = []
    for j in range(0,len(l)):
        p = True
        for d in primes:
            if(d > sqrt(l[j])):
                break
            if(l[j] % d == 0):
                p = False
                break;
        if(p):
            primes.append(l[j])

    return primes

# Total time: 0.006285 s
# File: euler72.py
# Function: gen_primes at line 6

# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#      6                                           @profile
#      7                                           def gen_primes(n):
#      8                                               
#      9         1          3.0      3.0      0.0      l = range(2,n)
#     10         1          1.0      1.0      0.0      primes = []
#     11       999        391.0      0.4      6.2      for j in range(0,len(l)):
#     12       998        359.0      0.4      5.7          p = True
#     13      2968       1056.0      0.4     16.8          for d in primes:
#     14      2967       1837.0      0.6     29.2              if(d > sqrt(l[j])):
#     15       167         85.0      0.5      1.4                  break
#     16      2800       1516.0      0.5     24.1              if(l[j] % d == 0):
#     17       830        314.0      0.4      5.0                  p = False
#     18       830        269.0      0.3      4.3                  break;
#     19       998        345.0      0.3      5.5          if(p):
#     20       168        109.0      0.6      1.7              primes.append(l[j])
#     21                                           
#     22         1          0.0      0.0      0.0      return primes

#########################################################################

@profile
def factorize(n,primes):
    factors = []
    init_n = n
    for p in primes:
        while(n%p == 0):
            n = n/p
            factors.append(p)
        if(p > sqrt(n)):
            break
    if(n > 1):
        factors.append(n)
    return factors

# Total time: 0.118035 s
# File: euler72.py
# Function: factorize at line 24

# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#     24                                           @profile
#     25                                           def factorize(n,primes):
#     26      9999       2460.0      0.2      2.1      factors = []
#     27      9999       2368.0      0.2      2.0      init_n = n
#     28     96347      22637.0      0.2     19.2      for p in primes:
#     29    118736      36717.0      0.3     31.1          while(n%p == 0):
#     30     22389       6170.0      0.3      5.2              n = n/p
#     31     22389       7128.0      0.3      6.0              factors.append(p)
#     32     96347      29954.0      0.3     25.4          if(p > sqrt(n)):
#     33      9999       2540.0      0.3      2.2              break
#     34      9999       2746.0      0.3      2.3      if(n > 1):
#     35      9596       2936.0      0.3      2.5          factors.append(n)
#     36      9999       2379.0      0.2      2.0      return factors

###################################################################
@profile    
def phi(n,primes):
    factors = factorize(n,primes)
    p = 1

    for i in range(2,n):
        flag = True
        for f in factors:
            if i%f == 0:
                flag = False
                break
        if flag:
            p+=1
    return p

# Total time: 0 s
# File: euler72.py
# Function: phi at line 85

# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#     85                                           @profile    
#     86                                           def phi(n,primes):
#     87                                               factors = factorize(n,primes)
#     88                                               p = 1
#     89                                           
#     90                                               for i in range(2,n):
#     91                                                   flag = True
#     92                                                   for f in factors:
#     93                                                       if i%f == 0:
#     94                                                           flag = False
#     95                                                           break
#     96                                                   if flag:
#     97                                                       p+=1
#     98                                               return p

#####################################################################

@profile
def fast_phi(n,primes):
    factors = factorize(n,primes)
    phi = factors[0]-1
    # for i in range(1,len(factors)):
    #     if(factors[i] == factors[i-1]):
    #         phi *= (factors[i]-1)*(factors[i])/(factors[i]-1)
    #     else:
    #         phi *= (factors[i]-1)
    return phi

primes = gen_primes(1000)
m = 10000
#m = 8
fraq = 0
for i in range(2,m+1):
    fraq += fast_phi(i,primes)
    
# Total time: 0.253891 s
# File: euler72.py
# Function: fast_phi at line 53

# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#     53                                           @profile
#     54                                           def fast_phi(n,primes):
#     55      9999     222529.0     22.3     87.6      factors = factorize(n,primes)
#     56      9999       2995.0      0.3      1.2      phi = factors[0]-1
#     57     31985      10372.0      0.3      4.1      for i in range(1,len(factors)):
#     58     21986       7481.0      0.3      2.9          if(factors[i] == factors[i-1]):
#     59      7685       3346.0      0.4      1.3              phi *= (factors[i]-1)*(factors[i])/(factors[i]-1)
#     60                                                   else:
#     61     14301       4743.0      0.3      1.9              phi *= (factors[i]-1)
#     62      9999       2425.0      0.2      1.0      return phi


print(fraq)