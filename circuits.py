# Prepare a parameterized 2-qubit X-state (first two qubits are ancillary)
p_a = Parameter('a')
p_ß = Parameter('ß')
p_γ = Parameter('γ')
x_state_prep = QuantumCircuit(4, 2)
x_state_prep.ry(p_a, 0)
x_state_prep.cx(0, 1)
x_state_prep.ry(p_ß, 0)
x_state_prep.ry(p_?, 1)
x_state_prep.cx(0, 2)
x_state_prep.cx(1, 3)
x_state_prep.ry(np.pi/3, 2)
x_state_prep.cx(2, 3)
print(x_state_prep)

# Plug in parameters (to cover all points)
circuits_x_state = []

for i in range(len(a)):
    x_state_prep_bound = x_state_prep.bind_parameters(
        {p_a: a[i],
         p_ß: ß[i],
         p_γ: γ[i]}
    )
    
    circuits_x_state.append(x_state_prep_bound)



for c in circuits_x_state:
    c.snapshot(label='ρ', snapshot_type='density_matrix', qubits=[2, 3])

ρs = []
res = execute(circuits_x_state, ideal_simulator).result()
for circuit_result in res.results:
    ρ = circuit_result.data.snapshots['density_matrix']['ρ'][0]['value']
    ρs.append(?)