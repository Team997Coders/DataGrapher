#!/usr/bin/env python3
import matplotlib.pyplot as plt
import os

localfile = raw_input("Localfile: ")

remotehost = ''
remotefile = ''
username = ''

if localfile != 'auto':
    remotehost = raw_input("Remote Host: ")
    remotefile = raw_input("Remotefile: ")
    username = raw_input("Remote User: ")
else:
    remotehost = '10.9.97.2'
    b = raw_input("Remote File Name: ")
    remotefile = '~/spartanlogs/' + b
    localfile = b
    username = 'lvuser'

os.system('scp "%s@%s:%s" "%s"' % (username, remotehost, remotefile, localfile) )

data = open(localfile, 'r')

lines = data.read()

data.close()

time = []
voltage = []
current = []
ticks = []
target = []
error = []
pid_output = []

bits = lines.replace('\n', ',').split(',')

for x in range(7):
    bits.remove(lines[0])

print(bits)

for x in range(len(bits) / 7):
    time.append(int(bits[((x + 1) * 7) - 7]))
    voltage.append(int(bits[((x + 1) * 7) - 6]))
    current.append(int(bits[((x + 1) * 7) - 5]))
    ticks.append(int(bits[((x + 1) * 7) - 4]))
    target.append(int(bits[((x + 1) * 7) - 3]))
    error.append(int(bits[((x + 1) * 7) - 2]))
    pid_output.append(int(bits[((x + 1) * 7) - 1]))

print('BAH')

plt.plot(time, error)
plt.xlabel('Time')
plt.ylabel('Error')

plt.title('Graphy Boi') 
plt.show()