import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

def main():
    plt.close('all')
    plt.figure(figsize=(10, 6))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
    plt.xlabel('B')
    plt.ylabel('v')

    plt.xlim([-3, 3])
    plt.ylim([-3, 3])

    # B-nullcline: B = 0 (vertical line at B = 0)
    plt.axvline(0, color='r', linestyle='-', label='B-nullcline')

    # B-nullcline: v = a / 2 (horizontal line at v = a/2)
    plt.axhline(a / 2, color='r', linestyle='-')

    B_vals = np.linspace(-np.sqrt(c), np.sqrt(c), 400)

    # Fixing the gap by refining the boundary check and limiting values to avoid precision issues
    epsilon = 1e-10  # Small value to handle floating-point inaccuracies
    valid_indices = B_vals**2 <= (c + epsilon)  # Ensure that (c - B_vals**2) is non-negative with tolerance

    # Only compute sqrt for valid values
    v_nullcline_positive = np.sqrt(np.clip(c - B_vals[valid_indices]**2, 0, None))  # Clip to ensure non-negative argument
    v_nullcline_negative = -np.sqrt(np.clip(c - B_vals[valid_indices]**2, 0, None))  # Same for the negative branch

    # Plot both branches of the v-nullcline, ensuring continuity
    plt.plot(B_vals[valid_indices], v_nullcline_positive, 'b-', label='v-nullcline')
    plt.plot(B_vals[valid_indices], v_nullcline_negative, 'b-')

    # Now add the v vs B line plot
    # Example: Plot a simple linear relation between v and B (v = B)
    v_vs_B_B_vals = np.linspace(-3, 3, 400)
    v_vs_B = v_vs_B_B_vals  # You can define any relationship you want between v and B here, e.g., v = B
    plt.plot(B, v, '-', color='black', label=r"v(t) vs B(t)")

    # Finding intersections
    B_intersection_1 = 0
    v_intersection_1 = c ** 0.5

    B_intersection_2 = 0
    v_intersection_2 = -1 * c ** 0.5

    B_intersection_3 = np.sqrt(c - (a / 2) ** 2)
    v_intersection_3 = a / 2

    B_intersection_4 = -1 * np.sqrt(c - (a / 2) ** 2)
    v_intersection_4 = a / 2

    intersections = [
        (B_intersection_1, v_intersection_1),
        (B_intersection_2, v_intersection_2),
        (B_intersection_3, v_intersection_3),
        (B_intersection_4, v_intersection_4)
    ]

    # Plot intersection points
    for (B_int, v_int) in intersections:
        plt.plot(B_int, v_int, 'go')  # 'go' means green circle

    plt.legend()
    plt.savefig('s2.png', bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    # Define values for a and c
    a = 1.0
    c = 4.0
    main()
