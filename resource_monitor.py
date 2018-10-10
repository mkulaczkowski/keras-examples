import os
import signal
import subprocess

# subprocess.Popen("while true; do nvidia-smi >> /logs/resources.log; sleep 10; done", shell=True)
p = subprocess.Popen("while true; do echo 'abc-test' >> resources.log; sleep 5; done", shell=True)
subprocess.call("python mnist.py --num_steps 5000", shell=True)

os.killpg(os.getpgid(p.pid), signal.SIGTERM)
