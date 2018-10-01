# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
from qiskit import register, execute, load_qasm_file, get_backend
import json
import time
import sys
print("Usage: python3 QiskitInterface.py <Key> <Backend> <Shots>")
apikey = sys.argv[1]
backend = sys.argv[2]
shots = sys.argv[3]
timeout = 60
sleeptime = 10

print("Qiskit API Interface")
print(" Registering API trust")
url = "https://quantumexperience.ng.bluemix.net/api"
register(apikey, url)
print("QASM FILE Read ")
circuit = load_qasm_file('input.txt')
print("SENDING TO IBM Quantum Experience")
print(" IBMQ AT IBM Quantum Experience:")
try:
    job = execute(circuit, get_backend(backend), shots=shots, max_credits=3)
    result = job.result().get_data()
    with open('output.txt', 'w') as resultFile:
        resultFile.write(str(next(iter(result['counts']))))
    sys.exit()
except:
    print("Failed execution (Probably not enough tokens)")
print(" Result later than timeout. Going to failover.")
print(" SIMULATOR AT IBM:")
ex = execute(circuit, 'ibmq_qasm_simulator', shots=shots)
result = ex.result().get_data()
print(result)
print("DONE")
with open('output.txt', 'w') as resultFile:
   resultFile.write(str(next(iter(result['counts']))))