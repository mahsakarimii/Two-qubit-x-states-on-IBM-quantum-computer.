start = 0
stop = 1
n_step = 50 # number of points between 0-1 for probabilities

p1 = np.linspace(start, stop, n_step+1) # raw probability 
p2 = np.linspace(start, stop, n_step+1)
p3 = np.linspace(start, stop, n_step+1)
p4 = np.linspace(start, stop, n_step+1)


p11 = []
p22 = []
p33 = []
p44 = []

# Filter probablities for this condition : p1+p2+p3+p4 = 1

for i in range(n_step+1):
    for j in range(n_step+1):
        for k in range(n_step+1):
            for l in range(n_step+1):
                    if .999<p1[i] + p2[j] + p3[k] + p4[l] <1.001:
                        p11.append(p1[i])
                        p22.append(p2[j])
                        p33.append(p3[k])
                        p44.append(p4[l])  


# Just convert list to numpy array
p11s = np.array(p11)
p22s = np.array(p22)
p33s = np.array(p33)
p44s = np.array(p44)

# Relation between probabities and coordinate axes.
x = p11s + p22s - p33s - p44s
y = -p11s + p22s + p33s - p44s
z = p11s - p22s + p33s - p44s

# Theoretical results for calculating the parameters of a, ß and ?.
# These parameters encode the probabilities of P11s, P22s, P33s, and P44s to qubits 3 and 4.
a_00, a_01, a_10, a_11 = np.sqrt([p11s, p22s, p33s, p44s])

sin_a = np.clip(2 * (a_00 * a_11 - a_01 * a_10), -1, 1)
cos_a = np.sqrt(1 - sin_a**2)
a = np.arcsin(sin_a)
a = np.array(a)

ß = np.zeros(len(a))
? = np.zeros(len(a))
for i in range(len(a)):
    if np.isclose(cos_a[i], 0, atol=1e-5):
        ß[i] = 2 * np.arctan(a_10[i] / (a_00[i] + 10**(-20)))
        ?[i] = 0
    else:
        ca = np.cos(a[i] / 2)
        sa = np.sin(a[i] / 2)
        A = 1 / cos_a[i] * (np.array([[ca * a_00[i] - sa * a_11[i],  ca * a_01[i] + sa * a_10[i]],
                                      [sa * a_01[i] + ca * a_10[i], -sa * a_00[i] + ca * a_11[i]]]))
        vals, vects = np.linalg.eig(A@A.T)
        maxcol = list(vals).index(max(vals))
        b = vects[:,maxcol]
        vals, vects = np.linalg.eig(A.T@A)
        maxcol = list(vals).index(max(vals))
        c = vects[:,maxcol]
        if b[0] < 0 or (np.isclose(b[0], 0) and b[1] < 0):
            b = -b
        for _ in range(2):
                if np.allclose(np.outer(b, c), A):
                    break
                else:
                    c = -c
        else:
            raise RuntimeError("Could not fix sign for c")
     
        ß[i] = 2 * np.arctan(b[1] / (b[0] + 10**(-20)))
        ?[i] = 2 * np.arctan(c[1] / (c[0] + 10**(-20)))

