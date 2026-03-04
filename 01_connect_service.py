from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()

print("IBM account loaded successfully.")
print("Instances:", service.instances())
