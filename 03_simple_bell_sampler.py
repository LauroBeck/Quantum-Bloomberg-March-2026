from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

service = QiskitRuntimeService(instance="open-instance")
backend = service.least_busy(simulator=False)

print("Using backend:", backend.name)

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

sampler = Sampler(mode=backend)
job = sampler.run([qc])

print("Job ID:", job.job_id())
