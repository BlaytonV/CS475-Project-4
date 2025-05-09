import matplotlib.pyplot as plt
import re

# Prepare lists for data
sizes = []
speedup_mult = []
speedup_sum = []

# Read your results.txt file
with open("results.txt", "r") as f:
    for line in f:
        # Match a line that looks like:  1024    N ... S ... ( 5.00)   N ... S ... ( 5.06)
        match = re.findall(r"^\s*(\d+)\s+N\s+[\d.]+\s+S\s+[\d.]+\s+\(\s*([\d.]+)\)\s+N\s+[\d.]+\s+S\s+[\d.]+\s+\(\s*([\d.]+)\)", line)
        if match:
            arr_size, mult_speedup, sum_speedup = match[0]
            sizes.append(int(arr_size))
            speedup_mult.append(float(mult_speedup))
            speedup_sum.append(float(sum_speedup))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(sizes, speedup_mult, marker='o', label="Array Multiplication Speedup")
plt.plot(sizes, speedup_sum, marker='s', label="MulSum Speedup")

plt.xscale('log', base=2)
plt.xlabel("Array Size")
plt.ylabel("Speedup (SIMD / Non-SIMD)")
plt.title("SIMD Speedup vs Array Size")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("speedup_plot.png")
plt.show()
