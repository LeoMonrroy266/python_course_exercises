import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()


process = rank
start = np.zeros(1)
end = np.zeros(1)
start[0] = comm.rank

comm.Reduce(start, end, op=MPI.SUM, root=0)

if comm.rank == 0:
    print( "Sum of the ranks is:", end[0])
