from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

service = QiskitRuntimeService(instance="open-instance")
backend = service.least_busy(simulator=False)

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

qc_t = transpile(qc, backend=backend, optimization_level=1)

sampler = Sampler(mode=backend)
job = sampler.run([qc_t])

print("Job ID:", job.job_id())
