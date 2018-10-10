import subprocess

subprocess.call("while true; do nvidia-smi >> /logs/resources.log; sleep 10; done")
subprocess.call("python mnist.py --num_steps 5000", shell=True)
