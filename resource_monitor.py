import os
import signal
import subprocess

p = subprocess.Popen("while true; do nvidia-smi >> /logs/resources.log; sleep 10; done", shell=True)
subprocess.call("python mnist.py --num_steps 5000", shell=True)

os.killpg(os.getpgid(p.pid), signal.SIGTERM)
