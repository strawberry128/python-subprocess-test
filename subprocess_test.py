import subprocess

if __name__ == '__main__':
    print('start subprocess test')
    subprocess.Popen('python3 sleep.py'.split(' '))
    print('end subprocess test')
