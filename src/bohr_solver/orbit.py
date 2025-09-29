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
