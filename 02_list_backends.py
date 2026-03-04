from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService(instance="open-instance")

print("Available backends:")
for backend in service.backends():
    print(backend.name)
