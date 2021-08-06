import numpy as np
import numpy as array
def ang_to_vec(ang):
    rad= np.degrees(ang)
    cosine=np.cos(rad)
    sine=np.sin(rad)
    print np.stack((cosine, sine),axis=-1)



def vec_to_ang(vec):
    A=np.array(vec)
    x=[row[0] for row in A]
    y=[row[1] for row in A]
    k= np.arctan2(y,x)
    print np.rad2deg(k)

