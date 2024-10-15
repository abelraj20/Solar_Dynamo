import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate


def solar(t, y, a, c):
    B, v = y    # B is mag field, v is plasma flow velocity
    dBdt = -a*B + 2*B*v
    dvdt = c - B**2 - (v**2)
    dydt = np.array([dBdt, dvdt])
    return dydt

# define a lambda function in a proper program that takes these arguments
lfun = lambda t, y, : solar(t, y, a, c)

# Define the initial parameters
B0 = 0.1  # initial position
v0 = 2  # initial velocity
y0 = (B0, v0)  # initial state
t0 = 0  # initial time

a = 1
c = 1

# Define the final time and the number of time steps
tf = 10  # final time
n = 1001  # Number of points at which output will be evaluated

# Create an array of the time steps
t = np.linspace(t0, tf, n)  # Points at which output will be evaluated

# Calls the method integrate.solve_ivp()
result = integrate.solve_ivp(fun=lfun,  # The function defining the derivative
                             t_span=(t0, tf),  # Initial and final times
                             y0=y0,  # Initial state
                             method="RK45",  # Integration method
                             t_eval=t)  # Time points for result to be defined at

# Read the solution and time from the result array returned by Scipy
B, v = result.y
t = result.t


# Plotting the results
fig, ax = plt.subplots(1, 2, figsize=(12, 6))  # 1 row, 2 columns

# Plot prey and predator populations as a function of time
ax[0].plot(t, B, label=r"Magnetic Field (B)")
ax[0].plot(t, v, label=r"Plasma Flow Velocity (m/s)")
ax[0].set_xlabel(r"Time")
ax[0].legend(loc='upper right')

# Create a phase space plot (Predator vs Prey)
ax[1].plot(B, v, 'k')
#ax[1].axis('equal')
ax[1].set_xlabel(r"Prey Population (x)")
ax[1].set_ylabel(r"Predator Population (y)")

# Show the plot
plt.tight_layout()

plt.savefig("s1.png", bbox_inches='tight')
plt.show()
