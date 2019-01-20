#!/usr/bin/env python3
import matplotlib.pyplot as plt
import os

localfile = raw_input("Localfile: ")

remotehost = raw_input("Remote Host: ")

remotefile = raw_input("Remotefile: ")

os.system('scp "%s:%s" "%s"' % (remotehost, remotefile, localfile) )

data = open('1_log.csv', 'r')

lines = data.read()

"""while True:
    a = data.readline()
    print('"' + a + '"')
    if not a:
        print('Break')
        break
    else:
        lines.append(int(a))
        print(int(a))"""

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

"""for x in range(len(bits)):
    print(x)"""

for x in range(len(bits) / 7):
#        bits = lines[x].split(',')
#    print(((x + 1) * 7) - 7)
    time.append(int(bits[((x + 1) * 7) - 7]))
#    print('"' + bits[((x + 1) * 7) - 6] + '"')
    voltage.append(int(bits[((x + 1) * 7) - 6]))
    current.append(int(bits[((x + 1) * 7) - 5]))
    ticks.append(int(bits[((x + 1) * 7) - 4]))
    target.append(int(bits[((x + 1) * 7) - 3]))
    error.append(int(bits[((x + 1) * 7) - 2]))
#    print('"' + bits[((x + 1) * 7) - 2] + '"')
    pid_output.append(int(bits[((x + 1) * 7) - 1]))

print('BAH')

#time.remove(time[0])
#error.remove(error[0])

plt.plot(time, error)
plt.xlabel('Time')
plt.ylabel('Error')

plt.title('Graphy Boi') 
plt.show()