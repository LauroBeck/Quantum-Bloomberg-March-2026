import numpy as np
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

cvx_momentum = 0.08
mkt_volatility = 0.02

qc = QuantumCircuit(2, 2)

qc.ry(cvx_momentum, 0)
qc.ry(mkt_volatility, 1)
qc.cz(0, 1)

qc.measure_all()

service = QiskitRuntimeService()
backend = service.least_busy(simulator=False)

sampler = Sampler(mode=backend)
job = sampler.run([qc])

print("Energy Job ID:", job.job_id())
