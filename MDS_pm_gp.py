import pandas as pd
import numpy as np
from sklearn.manifold import MDS

#pm = pd.read_csv('pm_MDS_test.csv', index_col=0)
#gp = pd.read_csv('gp_MDS_test.csv', index_col=0)
total = pd.read_csv('/bulk/jimenezb/Pandorina_morum5/mds/pm_gp_cr_test.csv', index_col=0)

#total = pm.append(gp)

scaled = MDS(n_components = 2).fit_transform(total)

coordinates = pd.DataFrame(scaled)
coordinates.index= total.index


coordinates.to_csv('/bulk/jimenezb/Pandorina_morum5/mds/three_spec_mds.csv')

