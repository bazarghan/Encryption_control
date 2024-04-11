import numpy as np
import matplotlib.pyplot as plt
import time
from ss import StateSpace as ss,MED
from ss__server import EncyrptedStateSpace as ess
from paillier import Encyrptoin

start_time = time.time()

def sim(input,G1,G2):
    output = []
    y = 0
    for r in input:
        error = r - y
        y = G2.out(G1.out(error))
        output.append(y)

    return output

    


def sim_enc(input,C_enc,Gp,encoder,Enc):


 
    output = []
    y = 0
    iter = 1

    for r in input:

        error = r - y
        error_encode = encoder.encode(error,iter)
        error_enc = Enc.encrypt(error_encode)

        out_enc = C_enc.out(error_enc)
        out_dec = Enc.decrypt(out_enc)
        out_decode = encoder.decode(out_dec,iter+1)

        y = Gp.out(out_decode)
        output.append(y)
        iter += 1
        if iter == 10:
            iter = 1
            C_enc.reset()

    return output



## Plant State Space    
Ap = np.matrix([[0.99998,0.0197],[-0.0197,0.97025]])
Bp = np.matrix([[0.0000999],[0.0098508]])
Cp = np.matrix([[1,0]])
Dp = np.matrix([[0]])

initial_cond = np.zeros((2,1))
initial_cond[0] = 1
plant = ss(Ap,Bp,Cp,Dp,initial_cond)


# Controller State Space
Ac = np.matrix([[1,0.0063],[0,0.3678]])
Bc = np.matrix([[0],[0.0063]])
Cc = np.matrix([[10,-99.90]])
Dc = np.matrix([[3]])

controller = ss(Ac,Bc,Cc,Dc)


# Encrypted Control statespace
Enc = Encyrptoin(512,True)
g,n = Enc.publicKey()
encoder = MED(n,100)

Ae = encoder.encode(Ac)
Be = encoder.encode(Bc)
Ce = encoder.encode(Cc)
De = encoder.encode(Dc)


initial_value = encoder.encode(np.zeros((2,1)))
encrypted_initial_value = Enc.encrypt_mat(initial_value)
controller_enc = ess((g,n),Ae,Be,Ce,De,encrypted_initial_value)

# r = 1
# r_encode = encoder.encode(r)
# r_enc = Enc.encrypt(r_encode)

# out_enc = controller_enc.out(r_enc)
# out_dec = Enc.decrypt(out_enc)
# out_decode = encoder.decode(out_dec,2)
# print(out_decode)





start = -1
end = 5
ts = 0.01
l = int((end-start)/ts)
t = np.linspace(start,end,l)
u = [0]*l
y = sim(u,controller,plant)
plant.reset()
y_enc = sim_enc(u,controller_enc,plant,encoder,Enc)


plt.plot(t,y)
plt.plot(t,y_enc)
plt.plot(t,u,linestyle='--')
plt.xlim([start,end])

end_time = time.time()

print(((end_time-start_time)/l)*1000,end='')
print('ms')

plt.show()
