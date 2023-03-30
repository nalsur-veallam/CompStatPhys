import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import jensenshannon
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import scipy.stats as sps

mc = [98.4238, 197.399, 290.095, 485.541]
md = [4.75964, 9.41078, 14.2053, 23.8143]
    
times = [10000, 20000, 30000, 50000]
    
fig, axs = plt.subplots(nrows= 1 , ncols= 2, figsize=(16,8))
axs[0].plot(times, mc,'o-', c='green')
axs[0].set_xlabel('Trajectory length')  
axs[0].set_ylabel('Run time') 
axs[0].set_title("MC")
axs[0].grid()


axs[1].plot(times, md,'o-', c='red') 
axs[1].set_xlabel('Trajectory length')  
axs[1].set_ylabel('Run time') 
axs[1].set_title("MD")
axs[1].grid()
    
plt.show()
fig.savefig("md.pdf")
