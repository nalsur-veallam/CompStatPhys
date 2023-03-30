#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --partition=RT
#SBATCH --job-name=example
#SBATCH --comment="lammps"

cd t30
 srun ~/lmp_mpi -in  in.melt
cd ..

cd t50
 srun ~/lmp_mpi -in  in.melt
cd ..

cd t10
 srun ~/lmp_mpi -in  in.melt
cd ..

