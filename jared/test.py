import pandas as pd
import numpy as np
from sklearn.manifold import MDS
from mdscuda import mds_fit, minkowski_pairs, MDS as cudaMDS
import time
import os
import sys

def main():
    try:
        jobs = int(sys.argv[1])
        lines = int(sys.argv[2])
        max_iter = int(sys.argv[3])
    except IndexError:
        print("Usage: " + os.path.basename(__file__) + " <jobs> <lines> <max_iter>")
        sys.exit(1)
    
    total = pd.read_csv('../mds_forstudents/pm_gp_cr_test.csv', index_col=0)
    total = total[:lines]

    print('starting mds')
    start = time.time()
    scaled = MDS(n_components = 2, n_jobs=jobs, max_iter=max_iter, n_init=16).fit_transform(total)
    end = time.time()
    coordinates = pd.DataFrame(scaled)
    coordinates.index= total.index
    coordinates.to_csv('sklearn.csv')

    ntasks = os.getenv('SLURM_NTASKS')
    print(f'Time: {end-start}, n_jobs: {jobs}, n_tasks: {ntasks}, lines: {lines}, iter: {max_iter}')


if __name__ == '__main__':
    main()