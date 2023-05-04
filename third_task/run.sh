#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --partition=RT
#SBATCH --job-name=example
#SBATCH --comment="lammps"


srun ~/lmp_mpi -in  in.equilibrate
srun ~/lmp_mpi -in in.diffusion.msd
srun ~/lmp_mpi -in in.diffusion.gk
srun ~/lmp_mpi -in in.viscosity


