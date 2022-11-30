import pandas as pd
import numpy as np
from mdscuda import MDS, minkowski_pairs
import time

N_SAMPLES = 100
total = pd.read_csv('../mds_forstudents/pm_gp_cr_test.csv', index_col=0)
total = total[:N_SAMPLES]
print(f'length: {len(total)} -----------------------------------------')
print('read data')

# method 1: use an sklearn-style class
start = time.time()
distance = minkowski_pairs(total, sqform = False)  # this returns a matrix of pairwise distances in longform
print('calculated distances')
mds = MDS(n_dims = 2, verbosity = 0)  # defines sklearn-style class
x = mds.fit(distance, calc_r2=True)  # fits and returns embedding
end = time.time()

coordinates = pd.DataFrame(x)
coordinates.index= total.index
coordinates.to_csv('cuda.csv')
print(f'Time: {end-start}, rows: {len(total)}')


