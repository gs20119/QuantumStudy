
from qiskit import QuantumCircuit, QuantumRegister

# Generate Quantum Qubits and Cirbuit
qubits = QuantumRegister(2, name="q")
circuit = QuantumCircuit(qubits)

q0, q1 = qubits
circuit.h(q0)
circuit.cx(q0,q1)
circuit.measure_all()
print(circuit)

# Visualize
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

circuit.draw("mpl")
plt.show()