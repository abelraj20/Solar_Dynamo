# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

def main():
    plt.close('all')
    coords = np.linspace(-3, 3, 21)
    B, v = np.meshgrid(coords, coords)
    dB = -a*B + 2*B*v
    dv = c - B**2 - v**2

    # Calculate the magnitude of the vector field
    magnitude = np.sqrt(dB**2 + dv**2)

    plt.figure(figsize=(6,6))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
    plt.xlabel('B')
    plt.ylabel('v')
    plt.quiver(B, v, dB, dv, magnitude, cmap='plasma')  # plot field as quiver
    plt.streamplot(B, v, dB, dv, linewidth=1, density=2)  # All streamlines in red

    # Add colorbar to indicate the vector field magnitude
    plt.colorbar(label='Magnitude')

    plt.savefig('S4.png', bbox_inches = 'tight')
    plt.show()


# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main()
