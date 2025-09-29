def energy_level(self, n: int = 1, Z: int = None) -> float:
    """
    Calcula la energía del nivel n para un átomo con número atómico Z
    usando la fórmula de Bohr para átomos tipo hidrógeno.
    La energía se devuelve en joules (J).

    E_n = -13.6 * Z^2 / n^2   (energía en eV, convertida a J)

    Args:
        n (int, opcional): Número del nivel de energía (n >= 1). Por defecto 1.
        Z (int, opcional): Número atómico del átomo. Por defecto se usa self.Z o 1.

    Returns:
        float: Energía del nivel n en joules (J)
    """
    if n < 1:
        raise ValueError("El número cuántico principal n debe ser >= 1")
    
    Z_used = Z if Z is not None else getattr(self, "Z", 1)
    energy_ev = -13.6 * (Z_used ** 2) / (n ** 2)  # energía en eV
    energy_j = energy_ev * 1.602176634e-19         # conversión a J
    return energy_j
