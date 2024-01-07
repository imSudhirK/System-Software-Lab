import numpy as np

N = 100

euler = 360.0 * (np.random.uniform(size=(N, 3)) - 0.5)
quaternion = np.random.uniform(size=(N, 4))

np.savetxt("euler.out", euler, delimiter="," )
np.savetxt("quaternion.out", quaternion, delimiter="," )

er = np.loadtxt("euler.out", delimiter=",")
qr = np.loadtxt("quaternion.out", delimiter=",")

assert (euler == er).all()
assert (quaternion == qr).all()
