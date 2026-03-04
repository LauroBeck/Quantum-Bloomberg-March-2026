import numpy as np
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

russell = 0.086
dow = 0.015
cvx = 0.11

qc = QuantumCircuit(3, 3)

qc.ry(russell, 0)
qc.ry(dow, 1)
qc.ry(cvx, 2)

qc.cz(0, 1)
qc.cz(1, 2)

qc.measure_all()

service = QiskitRuntimeService()
backend = service.least_busy(simulator=False)

sampler = Sampler(mode=backend)
job = sampler.run([qc])

print("Broad Market Job ID:", job.job_id())
