from bohr_solver import BohrAtom

def run_demonstration():
    """Executes a full demonstration of the BohrAtom class features."""

    print(" Welcome to the Bohr Atom Model Demonstration! ")

    # --- 1. Initialize a Hydrogen Atom ---
    print("\n--- 1. Initializing a Hydrogen atom (Z=1) ---")
    hydrogen = BohrAtom(Z=1)
    print(f"Created a BohrAtom instance for an atom with Z = {hydrogen.Z}")

    # --- 2. Perform Basic Calculations ---
    print("\n--- 2. Performing Core Calculations ---")

    # Calculate ground state energy
    ground_state_energy = hydrogen.calculate_energy_level(n=1)
    print(f"Ground state energy (n=1): {ground_state_energy:.3f} eV")

    # Calculate radius of the first orbit
    first_orbit_radius = hydrogen.calculate_orbit_radius(n=1)
    print(f"Radius of first orbit (n=1): {first_orbit_radius:.3e} meters (The Bohr Radius)")

    # --- 3. Analyze an Electronic Transition ---
    print("\n--- 3. Analyzing the Balmer-alpha Transition (n=3 to n=2) ---")
    transition = hydrogen.calculate_transition(n_initial=3, n_final=2)
    if transition:
        print(f"Transition Type: {transition['type']}")
        print(f"  Photon Energy: {transition['energy_eV']:.3f} eV")
        print(f"  Wavelength: {transition['wavelength_nm']:.2f} nm (Visible Red Light)")

    # --- 4. Generate Visualizations ---
    print("\n--- 4. Generating Visualizations (plots will open in new windows) ---")

    # Plot the specific transition
    print("  -> Displaying the energy transition diagram...")
    hydrogen.plot_energy_transition(n_initial=3, n_final=2)

    # Plot the atom orbits in both 'scaled' and 'schematic' modes
    print("  -> Displaying the physically ACCURATE 'scaled' orbit plot...")
    hydrogen.plot_bohr_atom(n=4, mode='scaled')

    print("  -> Displaying the ILLUSTRATIVE 'schematic' orbit plot...")
    hydrogen.plot_bohr_atom(n=4, mode='schematic')

    # --- 5. Analyze a Different Atom ---
    print("\n--- 5. Analyzing a Hydrogen-like Ion: Singly Ionized Helium (Z=2) ---")
    helium_ion = BohrAtom(Z=2)
    he_ground_energy = helium_ion.calculate_energy_level(n=1)
    print(f"Ground state energy for He+ (Z=2) is {he_ground_energy:.3f} eV.")
    print(f"(Note: It's Z^2 = 4 times the energy of Hydrogen, as expected!)")

    print("\n Demonstration Complete.")

if __name__ == "__main__":
    run_demonstration()
