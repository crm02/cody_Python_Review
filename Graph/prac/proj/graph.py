import matplotlib.pyplot as plt
from systemInfo import get_cpu_per


cpu_percentages = [get_cpu_per() for i in range(10)]
plt.plot(cpu_percentages,'b-')
plt.show()

