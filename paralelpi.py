from mpi4py import MPI
import time

start = time.time()
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
hasil = 0.0
pi = 0.0
x = 0.0
comm.Barrier()
for i in range(1, size):
	x = i*i*(1.0/100000000000000)
	hasil += 1.0/(1.0+x*x)
val = comm.reduce(hasil, op=MPI.SUM, root=0)
if rank == 0:	
	pi = 4*val*(1.0/10000000)
	end = time.time()
	print "Pi with %d steps is %f in %f secs" %(size, pi, end-start)
