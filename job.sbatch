#!/bin/bash
#SBATCH -p smfletch
#SBATCH --job-name=demo
#SBATCH --time=00:05:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=keaniw@stanford.edu

set -e
module purge
module load python/3.10.13

# optional: per-job venv to keep things clean
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt --quiet


python app.py
