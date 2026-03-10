import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp

# 1. Setup Circuit (6 Qubits for full portfolio)
# Mapping: 0:Nasdaq, 1:IBM, 2:JEPQ, 3:TSLA, 4:JPM, 5:BNY
qc = QuantumCircuit(6, 6)

# 2. Tech Assets (March 9 Data)
qc.u(2.1, 0, 0, 0)      # Nasdaq +1.32%
qc.u(1.0, 0.45, 0, 1)   # IBM -2.08%
qc.u(2.0, 0, 0, 2)      # JEPQ +1.28%
qc.u(1.65, 0.15, 0, 3)  # TSLA +0.49%

# 3. Financial Stability Anchors
# JPM (+0.15%): Low volatility, stable rotation
qc.u(0.5, 0, 0, 4) 

# BNY (Targeting liquidity correlation)
# Modeling BNY as a phase-pivot for the financial sector
qc.u(0.6, 0.1, 0, 5)

# 4. Cross-Sector Entanglement (Finance-Tech Correlation)
# Entangling JPM with the Nasdaq to model systemic risk
qc.h(4)
qc.cx(4, 0) 

# 5. Measurement
qc.measure_all()

print("Architecture expanded to 6-Asset Portfolio.")
print(qc.draw(output='text'))
