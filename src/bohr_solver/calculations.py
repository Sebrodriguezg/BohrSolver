def calculate_transition(atom, n_i=1, n_f=2):
    atom.n_i = n_i
    atom.n_f = n_f

    if atom.n_i == atom.n_f
        return {"error": "el nivel inicial no puede ser igual al final."}
    try:
        # |1/n_f² - 1/n_i²|
        term = abs((1 / atom.n_f**2) - (1 / atom.n_i**2))

        # Wavelength inverse (1/λ)
        inv_wavelength = atom.R * (atom.z**2) * term

        # Wavelength in meters
        atom.wavelength = 1 / inv_wavelength

        # Frequency (ν = c/λ)
        atom.frequency = atom.c / atom.wavelength

    except ZeroDivisionError:
        return {"error": "Division per 0, review quantum levels"}
    if atom.n_i > atom.n_f:
        atom.transition_type = "Emission"
    else:
        atom.transition_type = "Absortion"
    """
    """

def calculate_orbit_radius(atom, n: int) -> float:
    """
    Calculates the radius of the orbit for a given quantum level 'n'.

    Args:
        atom: An instance of the BohrAtom class.
        n (int): The principal quantum number (n > 0).

    Returns:
        float: The radius of the orbit in meters.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Principal quantum number n must be a positive integer.")
    
    return (n**2 / atom.Z) * atom.a0

def energy_level(atom, n: int = 1, Z: int = None) -> float:
    """
    Calcula la energía del nivel n para un átomo con número atómico Z
    usando la fórmula de Bohr para átomos tipo hidrógeno.
    La energía se devuelve en joules (J).

    E_n = -13.6 * Z^2 / n^2   (energía en eV, convertida a J)

    Args:
        n (int, opcional): Número del nivel de energía (n >= 1). Por defecto 1.
        Z (int, opcional): Número atómico del átomo. Por defecto se usa atom.Z o 1.

    Returns:
        float: Energía del nivel n en joules (J)
    """
    if n < 1:
        raise ValueError("El número cuántico principal n debe ser >= 1")
    
    Z_used = Z if Z is not None else getattr(atom, "Z", 1)
    energy_ev = -13.6 * (Z_used ** 2) / (n ** 2)  # energía en eV
    energy_j = energy_ev * 1.602176634e-19         # conversión a J
    return energy_j
