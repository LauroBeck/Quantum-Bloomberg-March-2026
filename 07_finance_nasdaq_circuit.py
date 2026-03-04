import numpy as np
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

nasdaq_theta = 0.0036
sp500_theta = 0.0004

qc = QuantumCircuit(3, 2)

qc.ry(nasdaq_theta, 0)
qc.ry(sp500_theta, 1)
qc.cz(0, 1)

qc.measure(0, 0)

with qc.if_test((0, 1)):
    qc.x(1)

qc.measure([1, 2], [0, 1])

service = QiskitRuntimeService()
backend = service.least_busy(simulator=False)

sampler = Sampler(mode=backend)
job = sampler.run([qc])

print("Finance Job ID:", job.job_id())
