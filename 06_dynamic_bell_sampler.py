import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

service = QiskitRuntimeService()
backend = service.backend("ibm_fez")

qr = 2
cr_mid = ClassicalRegister(1, name="mid")
cr_final = ClassicalRegister(2, name="final")

qc = QuantumCircuit(qr, cr_mid, cr_final)

qc.rz(np.pi/2, 1)
qc.sx(1)
qc.rz(np.pi/2, 1)
qc.cz(0, 1)

qc.measure(0, cr_mid[0])

with qc.if_test((cr_mid[0], 1)):
    qc.x(1)

qc.measure([0, 1], cr_final)

sampler = Sampler(mode=backend)
job = sampler.run([qc])

print("Dynamic Job ID:", job.job_id())
