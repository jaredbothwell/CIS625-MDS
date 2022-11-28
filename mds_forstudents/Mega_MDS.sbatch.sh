#!/bin/sh
#SBATCH --ntasks=4
#SBATCH --mem-per-cpu=50G
#SBATCH --time=96:00:00
#SBATCH --job-name=Mega_MDS
#SBATCH --mail-user=jimenezb@ksu.edu
#SBATCH --mail-type=END,FAIL

module load Python/3.6.4-foss-2018a
source  /homes/jimenezb/virtualenvs_sbatch/mds_env_test2/bin/activate
export PYTHONDONTWRITEBYTECODE=1

python /bulk/jimenezb/Pandorina_morum5/mds/MDS_pm_gp.py
