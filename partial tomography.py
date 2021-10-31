# circuits to measure in different basis

# measurement of $\sigma _z \otimes \sigma _z$ observable.
meas_zz = QuantumCircuit(2, 2)
meas_zz.measure(0, 0)
meas_zz.measure(1, 1)
print(meas_zz)

# measurement of $\sigma _x \otimes \sigma _x$ observable.
meas_xx = QuantumCircuit(2, 2)
meas_xx.h(0)
meas_xx.h(1)
meas_xx.measure(0, 0)
meas_xx.measure(1, 1)
print(meas_xx)

# measurement of $\sigma _y \otimes \sigma _y$ observable.
meas_yy = QuantumCircuit(2, 2)
meas_yy.sdg(0)
meas_yy.sdg(1)
meas_yy.h(0)
meas_yy.h(1)
meas_yy.measure(0, 0)
meas_yy.measure(1, 1)
print(meas_yy)

# measurement of $\sigma _x \otimes \sigma _y$ observable.
meas_yy = QuantumCircuit(2, 2)
meas_yy.sdg(1)
meas_yy.h(0)
meas_yy.h(1)
meas_yy.measure(0, 0)
meas_yy.measure(1, 1)
print(meas_xy)

# measurement of $\sigma _y \otimes \sigma _x$ observable.
meas_yy = QuantumCircuit(2, 2)
meas_yy.sdg(0)
meas_yy.h(0)
meas_yy.h(1)
meas_yy.measure(0, 0)
meas_yy.measure(1, 1)
print(meas_yx)



circuits_zz = []
circuits_xx = []
circuits_yy = []
circuits_xy = []
circuits_yx = []

for c in circuits_x_state:
    circuits_zz.append(c.compose(meas_zz, [2, 3]))
    circuits_xx.append(c.compose(meas_xx, [2, 3]))
    circuits_yy.append(c.compose(meas_yy, [2, 3]))
    circuits_xy.append(c.compose(meas_xy, [2, 3]))
    circuits_yx.append(c.compose(meas_yx, [2, 3]))
    

shots = 8000
result_zz = execute(circuits_zz, backend=ideal_simulator, shots=shots).result()
counts_zz = [result_zz.get_counts(i) for i in range(len(circuits_zz))]

result_xx = execute(circuits_xx, backend=ideal_simulator, shots=shots).result()
counts_xx = [result_xx.get_counts(i) for i in range(len(circuits_xx))]

result_yy = execute(circuits_yy, backend=ideal_simulator, shots=shots).result()
counts_yy = [result_yy.get_counts(i) for i in range(len(circuits_yy))]


def process_counts(counts_zz, counts_xx, counts_yy):
    # Convert the results of measurement to probabilities.
    p1 = np.array([c.get('00', 0) for c in counts_zz])
    p2 = np.array([c.get('10', 0) for c in counts_zz])
    p3 = np.array([c.get('01', 0) for c in counts_zz])
    p4 = np.array([c.get('11', 0) for c in counts_zz])

    p5 = np.array([c.get('00', 0) for c in counts_xx])
    p6 = np.array([c.get('10', 0) for c in counts_xx])
    p7 = np.array([c.get('01', 0) for c in counts_xx])
    p8 = np.array([c.get('11', 0) for c in counts_xx])

    p9 = np.array([c.get('00', 0) for c in counts_yy])
    p10 = np.array([c.get('10', 0) for c in counts_yy])
    p11 = np.array([c.get('01', 0) for c in counts_yy])
    p12 = np.array([c.get('11', 0) for c in counts_yy])
    
    p13 = np.array([c.get('00', 0) for c in counts_xy])
    p14 = np.array([c.get('10', 0) for c in counts_xy])
    p15 = np.array([c.get('01', 0) for c in counts_xy])
    p16 = np.array([c.get('11', 0) for c in counts_xy])
    
    p17 = np.array([c.get('00', 0) for c in counts_yx])
    p18 = np.array([c.get('10', 0) for c in counts_yx])
    p19 = np.array([c.get('01', 0) for c in counts_yx])
    p20 = np.array([c.get('11', 0) for c in counts_yx])
    
    

    # According to Hilbert-Schmidt's decomposition, t_z is the third component of the correlation matrix(T).
    tz = (p1 - p2 - p3 + p4) / shots
    tx = (p5 - p6 - p7 + p8) / shots
    ty = (p9 - p10 - p11 + p12) / shots
    txy = (p13 - p14 - p15 + p16)/ shots
    tyx = (p17 - p18 - p19 + p20)/ shots
    

    # By having joint probabilities, one can also obtain the marginal probabilities.
    # So we have Alice's (rz) and Bob's (sz) Bloch vectors.
    rz = (p1 - p3 + p2 - p4) / shots
    sz = (p1 + p3 - p2 - p4) / shots

