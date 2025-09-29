# library math for calculations
import math

class Electronic_Transition:
    """
    Calculate properties of a photon absord or emit in a electronic transition    
    """

    def calculate_transition(self, n_i=1, n_f=2):
        self.n_i = n_i
        self.n_f = n_f

    if self.n_i == self.n_f
        return {"error": "el nivel inicial no puede ser igual al final."}
    try:
        # |1/n_f² - 1/n_i²|
        term = abs((1 / self.n_f**2) - (1 / self.n_i**2))

        # Wavelength inverse (1/λ)
        inv_wavelength = self.R * (self.z**2) * term

        # Wavelength in meters
        self.wavelength = 1 / inv_wavelength

        # Frequency (ν = c/λ)
        self.frequency = self.c / self.wavelength

    except ZeroDivisionError:
        return {"error": "Division per 0, review quantum levels"}
    if self.n_i > self.n_f:
        self.transition_type = "Emission"
    else:
        self.transition_type = "Absortion"
    """
    """

    return {
        "wavelength_m" : self.wavelength,
        "wavelength_nm": self.wavelength  1e9,
        "frequency_hz": self.frequency,
        "type": self.transition_type
    }

