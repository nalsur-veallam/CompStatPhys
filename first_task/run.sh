#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --partition=RT
#SBATCH --job-name=example
#SBATCH --comment="lammps"

cd 1.4/
 srun ~/lmp_mpi -in  in.melt
cd ..

cd 0.1/
 srun ~/lmp_mpi -in  in.melt
cd ..

cd 1/
 srun ~/lmp_mpi -in  in.melt
cd ..

cd 2/
 srun ~/lmp_mpi -in  in.melt
cd ..

cd 2.5/
 srun ~/lmp_mpi -in  in.melt
cd ..

cd 3/
 srun ~/lmp_mpi -in  in.melt
cd ..

cd 3.5/
 srun ~/lmp_mpi -in  in.melt
cd ..

cd 4/
 srun ~/lmp_mpi -in  in.melt
cd ..

cd 4.5/
 srun ~/lmp_mpi -in  in.melt
cd ..

cd 5/
 srun ~/lmp_mpi -in  in.melt
cd ..

