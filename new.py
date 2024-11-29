import numpy as np
import matplotlib.pyplot as plt

# Constants
beta_F = 25
V_CE = np.arange(-5, 10.1, 0.01)  # Sweep from -5V to 10V
I_B_values = [10e-3, 30e-3, 50e-3]  # Base currents in Amperes
I_S = 0.1e-15  # Saturation current

# Plot setup
plt.figure(figsize=(8, 6))
for I_B in I_B_values:
    I_C = np.minimum(beta_F * I_B, I_S * np.exp(V_CE / 0.025))  # Active and saturation
    plt.plot(V_CE, I_C * 1e3, label=f"I_B = {I_B*1e3} mA")

# Labels and legend
plt.title("Common-Emitter Output Characteristics")
plt.xlabel("V_CE (V)")
plt.ylabel("I_C (mA)")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid()
plt.legend()
plt.show()
