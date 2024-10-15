import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

# Define the initial parameters
B0 = [-1.5, -1, -0.3, 0, 0.3, 1, 1.5, 10]
v0 = 1
t0 = 0  # Initial time

a = 2
c = 2  # Carrying capacity (should be greater than initial population)


# Define the final time and the number of time steps
tf = 10  # Final time
n = 1001  # Number of points at which output will be evaluated

# Creates an array of the time steps
t = np.linspace(t0, tf, n)  # Points at which output will be evaluated

plt.figure(figsize=(12, 6))

for i in B0:
    # Calls the method integrate.solve_ivp()
    result = integrate.solve_ivp(fun=lfun,  # The function defining the derivative
                                t_span=(t0, tf),  # Initial and final times
                                y0=[i, v0],  # Initial state (as a list)
                                method="RK45",  # Integration method
                                t_eval=t)  # Time points for result to be defined at

    # Read the solution and time from the result array returned by Scipy
    B_values = result.y[0]  # Extracting magnetic field values
    v_values = result.y[1]  # Extracting plasma flow velocity values
    t_values = result.t  # Time values

    plt.plot(t_values, B_values, label=f"$B_0$ = {i}")

plt.xlabel(r"Time")
plt.ylabel(r"B (Tesla) ")
plt.legend(loc='best')

plt.savefig("G5.png", bbox_inches='tight')
plt.show()
