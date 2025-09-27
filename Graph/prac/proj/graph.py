import matplotlib.pyplot as plt
from systemInfo import get_cpu_per, get_ram
from matplotlib.animation import FuncAnimation
import numpy as np

def update(frame):
    new_cpu =get_cpu_per() 
    cpu.append(new_cpu)
    line.set_data(range(len(cpu)),cpu)

    new_ram = get_ram()
    ram.append(new_ram)
    line2.set_data(range(len(ram)),ram)

    ax.relim()
    ax.autoscale_view()
    plt.annotate(f'{get_ram()}',xy=(get_ram(),get_ram()))

    


cpu = []
ram = []

fig, ax = plt.subplots()
line, = ax.plot([],[], label='CPU')
line2, = ax.plot([],[],  label = 'RAM')
ax.legend()

ax.set_xlim(0,100)
ax.set_ylim(0,100)
ax.set_title('CPU and RAM Percentages')
ax.set_xlabel('Time')
ax.set_ylabel('%')




animation = FuncAnimation(fig, update, frames=None, interval= 0.1)
plt.show()


#cpu_percentages = [get_cpu_per() for i in range(10)]
#plt.plot(cpu_percentages,'b-')
#
#
#
#ram_per = [get_ram() for i in range(10)]
#plt.plot(ram_per,'r-')
#
#
#
## Labels
#plt.xlabel('Blue line CPU | Red line RAM',)
#
#plt.show()