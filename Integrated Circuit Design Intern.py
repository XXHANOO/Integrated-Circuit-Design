import subprocess
import matplotlib.pyplot as plt

# SPICE netlist file content
netlist = """
* Low-Pass Filter Circuit Simulation
R1 N001 N002 1k
C1 N002 0 1uF
V1 N001 0 SIN(0 1 1k)
.TRAN 1us 5ms
.PRINT TRAN V(N002)
.END
"""

# Write netlist to a file
with open("low_pass_filter.cir", "w") as f:
    f.write(netlist)

# Run SPICE simulation
subprocess.run(["ngspice", "-b", "low_pass_filter.cir"], stdout=subprocess.PIPE)

# Simulate plot example results (replace with parsed data)
time = [0, 1, 2, 3, 4, 5]  # Replace with actual time data
voltage = [0, 0.2, 0.5, 0.7, 0.8, 0.9]  # Replace with actual voltage data

plt.plot(time, voltage, label="Output Voltage")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.title("Low-Pass Filter Output")
plt.legend()
plt.grid()
plt.show()
