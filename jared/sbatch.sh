#!/bin/sh
#SBATCH --ntasks=16
#SBATCH --mem-per-cpu=1G
#SBATCH --time=00:30:00
#SBATCH --constraint=warlocks

# module load Python/3.10.4-GCCcore-11.3.0
module load Python/3.9.5-GCCcore-10.3.0
# module load Python/3.6.4-foss-2018a
source  /homes/jaredcbothwell/virtualenvs/venv/bin/activate
export PYTHONDONTWRITEBYTECODE=1

python /homes/jaredcbothwell/CIS625-MDS/test.py $1 $2 $3
