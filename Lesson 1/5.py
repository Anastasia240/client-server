import subprocess

ping_results = ''

args = ['ping', 'yandex.ru']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    ping_results += line.decode('cp866')

args = ['ping', 'youtube.com']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    ping_results += line.decode('cp866')

print(ping_results.encode('utf-8').decode('utf-8'))
