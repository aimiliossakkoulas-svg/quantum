from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit import QuantumCircuit, transpile

# Replace 'YOUR_API_TOKEN' with your actual IBM Quantum API token
API_TOKEN = 'i7hoqsEcUmvXz_irSxNcQ73cRJ_tUEsINLCQ4vAwyeR_'

def connect_to_ibm_quantum():
    """
    Connect to IBM Quantum using the API token.
    """
    try:
        service = QiskitRuntimeService(channel="ibm_quantum_platform", token=API_TOKEN)
        print("Successfully connected to IBM Quantum!")
        # List available backends
        backends = service.backends()
        print(f"Available backends: {[backend.name for backend in backends]}")
        return service
    except Exception as e:
        print(f"Failed to connect: {e}")
        return None

if __name__ == "__main__":
    service = connect_to_ibm_quantum()
    if service:
        # Create Bell state circuit
        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure_all()

        # Visualize the circuit
        print("Bell State Circuit:")
        print(qc.draw('text'))

        # Select a backend, e.g., the first one
        backend = service.backends()[0]
        print(f"Using backend: {backend.name}")

        # Transpile
        transpiled_qc = transpile(qc, backend)

        # Run
        sampler = Sampler(backend)
        job = sampler.run([transpiled_qc])
        print("Job submitted. Waiting for results...")

        result = job.result()
        counts = result[0].data.c.get_counts()
        print(f"Measurement results: {counts}")