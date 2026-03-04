from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import SparsePauliOp
from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2 as Estimator

service = QiskitRuntimeService()
backend = service.backend("ibm_fez")

bell = QuantumCircuit(2)
bell.h(0)
bell.cx(0, 1)

bell_t = transpile(bell, backend=backend)

obs = SparsePauliOp(["ZZ", "XX"])
mapped_obs = obs.apply_layout(bell_t.layout)

estimator = Estimator(mode=backend)
job = estimator.run([(bell_t, mapped_obs)])

print("Estimator Job ID:", job.job_id())
