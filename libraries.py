import numpy as np
import plotly
import matplotlib
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from mpl_toolkits.mplot3d import Axes3D


import qiskit
from qiskit.circuit import QuantumCircuit, Parameter
from qiskit.providers.aer import QasmSimulator
from qiskit import execute, IBMQ, transpile, assemble
ideal_simulator = QasmSimulator()

from qiskit.providers.aer.noise import NoiseModel

from qiskit.quantum_info import concurrence

import time
from copy import deepcopy

# Tomography functions
from qiskit.ignis.verification.tomography import state_tomography_circuits, StateTomographyFitter
import qiskit.ignis.mitigation.measurement as mc


from qiskit.quantum_info import state_fidelity





