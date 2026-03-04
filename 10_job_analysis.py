from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()

job_id = "PASTE_JOB_ID_HERE"
job = service.job(job_id)

print("Status:", job.status())

if job.status().name == "DONE":
    result = job.result()
    reg = list(result[0].data.keys())[0]
    counts = result[0].data[reg].get_counts()
    print("Counts:", counts)
