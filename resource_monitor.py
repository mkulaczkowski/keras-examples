from argparse import ArgumentParser
import os
import signal
import subprocess

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--command', type=str, default='python main.py')
    parser.add_argument('--stat_frequency', type=int, default=10)
    opts = parser.parse_args()
    return opts

def main(opts):
    p = subprocess.Popen('while true; do nvidia-smi >> /logs/resources.log; sleep {}; done'.format(opts.stat_frequency), shell=True)
    subprocess.call(opts.command, shell=True)

    os.killpg(os.getpgid(p.pid), signal.SIGTERM)

if __name__ == '__main__':
    opts = parse_args()
    main(opts)
