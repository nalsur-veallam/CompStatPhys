#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --partition=RT
#SBATCH --job-name=example
#SBATCH --comment="lammps"

cd mc2
 srun ~/lmp_mpi -in  in.melt
cd ..

cd mc3
 srun ~/lmp_mpi -in  in.melt
cd ..


cd mc4
 srun ~/lmp_mpi -in  in.melt
cd ..


cd mc5
 srun ~/lmp_mpi -in  in.melt
cd ..


