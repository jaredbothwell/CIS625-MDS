#!/bin/sh
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=01:00:00
#SBATCH --gres=gpu:1

# module load fosscuda
module load Python/3.9.5-GCCcore-10.3.0

source  /homes/jaredcbothwell/virtualenvs/cuda/bin/activate
export PYTHONDONTWRITEBYTECODE=1

python /homes/jaredcbothwell/CIS625-MDS/jared/cuda.py