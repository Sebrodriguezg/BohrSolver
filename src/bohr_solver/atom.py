from . import calculations
from . import visualization

class BohrAtom:
    """
    A class to model a hydrogen-like atom based on Bohr's model.

    It serves as an interface to the underlying calculation and
    visualization functions and contains the necessary physical constants
    defined internally to avoid external dependencies.
    """
    def __init__(self, Z: int = 1):
        """
        Initializes the BohrAtom with a given atomic number (Z) and
        defines the required physical constants.

        Args:
            Z (int): The atomic number (number of protons). Defaults to 1.
        """
        if not isinstance(Z, int) or Z < 1:
            raise ValueError("Atomic number Z must be a positive integer.")
        self.Z = Z

        # --- Physical Constants (CODATA 2018 values) ---
        self.m_e = 9.1093837015e-31  # Electron mass (kg)
        self.e = 1.602176634e-19     # Elementary charge (C)
        self.h = 6.62607015e-34      # Planck constant (J*s)
        self.epsilon_0 = 8.8541878128e-12 # Vacuum permittivity (F/m)
        self.c = 299792458           # Speed of light (m/s)
        self.a0 = 5.29177210903e-11   # Bohr radius (m)

                # --- Derived Constants ---
        # Rydberg constant for an infinitely heavy nucleus (m⁻¹)
        self.R = (self.m_e * self.e**4) / (8 * self.epsilon_0**2 * self.h**3 * self.c)

    def calculate_energy_level(self, n: int, unit: str = 'eV') -> float:
        """
        Calculates the energy of an electron in a given quantum level 'n'.

        This method is a wrapper for the implementation in
        `bohr_model.calculations.calculate_energy_level`.
        """
        return calculations.calculate_energy_level(self, n, unit)

    def calculate_orbit_radius(self, n: int) -> float:
        """
        Calculates the radius of the orbit for a given quantum level 'n'.

        This method is a wrapper for the implementation in
        `bohr_model.calculations.calculate_orbit_radius`.
        """
        return calculations.calculate_orbit_radius(self, n)

    def calculate_transition(self, n_initial: int, n_final: int) -> dict:
        """
        Calculates properties of a photon from an electronic transition.

        This method is a wrapper for the implementation in
        `bohr_model.calculations.calculate_transition`.
        """
        return calculations.calculate_transition(self, n_initial, n_final)

    def plot_energy_levels(self, n_max: int = 5):
        """
        Generates a diagram of the first 'n_max' energy levels.

        This method is a wrapper for the implementation in
        `bohr_model.visualization.plot_energy_levels`.
        """
        visualization.plot_energy_levels(self, n_max)

    def plot_orbits(self, n_max: int = 4):
        """
        Generates a simplified 2D plot of the first 'n_max' electron orbits.

        This method is a wrapper for the implementation in
        `bohr_model.visualization.plot_orbits`.
        """
        visualization.plot_orbits(self, n_max)
