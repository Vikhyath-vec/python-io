import numpy as np
from scipy.stats import bernoulli
count = 0
for i in range(50000):
    bern_data = bernoulli.rvs(size=50, p=0.02)
    idk = np.nonzero(bern_data == 1)
    defective = np.size(idk)
    if defective >= 2:
        count += 1

print(count/50000)
