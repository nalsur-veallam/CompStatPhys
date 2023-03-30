import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import jensenshannon
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import scipy.stats as sps

probs = [0.5562605, 0.48582, 0.3925573, 0.27437, 0.1355487749]
    
x = [0.1, 0.12, 0.15, 0.2, 0.3]
    
fig = plt.figure(figsize=(10,7))     
    
plt.plot(x, np.log(probs),'o-', c='green') 
plt.xlabel('maxdist')  
plt.ylabel('Log(Probability)') 
plt.grid()
plt.show()
fig.savefig("probs.pdf")
