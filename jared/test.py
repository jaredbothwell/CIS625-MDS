import pandas as pd
import numpy as np
from sklearn.manifold import MDS
from sklearn.decomposition import PCA
import time
import os
import sys
import phate

def main():
    #pm = pd.read_csv('pm_MDS_test.csv', index_col=0)
    #gp = pd.read_csv('gp_MDS_test.csv', index_col=0)
    #total = pd.read_csv('/bulk/jimenezb/Pandorina_morum5/mds/pm_gp_cr_test.csv', index_col=0)
    #total = pm.append(gp)

    try:
        jobs = int(sys.argv[1])
        lines = int(sys.argv[2])
        max_iter = int(sys.argv[3])
    except IndexError:
        print("Usage: " + os.path.basename(__file__) + " <arg1>")
        sys.exit(1)
    
    #total = pd.read_csv('cr_mini.csv', index_col=0)
    total = pd.read_csv('long.csv')
    total = total[:lines]

    print('starting mds')
    start = time.time()
    scaled = MDS(n_components = 2, n_jobs=jobs, max_iter=max_iter, n_init=16).fit_transform(total)
    end = time.time()
    coordinates = pd.DataFrame(scaled)
    coordinates.index= total.index
    coordinates.to_csv('test.csv')

    pstart = time.time()
    pca = PCA(n_components = 2).fit_transform(total)
    pend = time.time()
    print(f'pca: {pend-pstart}')

    coordinates = pd.DataFrame(pca)
    coordinates.index= total.index
    coordinates.to_csv('pca.csv')

    s = time.time()
    scaled_phate = phate.PHATE(n_components=2).fit_transform(total)
    e = time.time()
    print(f'phate: {e - s}')

    coordinates = pd.DataFrame(scaled_phate)
    coordinates.index= total.index
    coordinates.to_csv('phate.csv')

    

    ntasks = os.getenv('SLURM_NTASKS')
    print(f'Time: {end-start}, n_jobs: {jobs}, n_tasks: {ntasks}, lines: {lines}, iter: {max_iter}')


if __name__ == '__main__':
    main()