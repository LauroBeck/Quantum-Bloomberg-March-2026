import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2 as Estimator
from qiskit.quantum_info import SparsePauliOp

# 1. Setup Circuit (4 Qubits / 4 Classical Bits)
qc = QuantumCircuit(4, 4)

# 2. Encode Market Data (Final March 9 Closing)
# Q0: Nasdaq (+1.32%) | Q1: IBM (-2.08% + Vol) | Q2: JEPQ (+1.28%) | Q3: TSLA (+0.49%)
qc.u(2.1, 0, 0, 0)
qc.u(1.0, 0.45, 0, 1)
qc.u(2.0, 0, 0, 2)
qc.u(1.65, 0.15, 0, 3)

# 3. Market Drag / Volatility Correlation (CZ equivalent)
qc.h(2)
qc.cx(0, 2)
qc.h(2)

# 4. Measurement
qc.measure([0, 1, 2, 3], [0, 1, 2, 3])

# 5. Backend Execution (Example for ibm_fez)
# service = QiskitRuntimeService()
# backend = service.backend("ibm_fez")
# qc_t = transpile(qc, backend=backend, optimization_level=3)

print("Circuit compiled for March 9 Market Sentiment.")
print(qc.draw(output='text'))
