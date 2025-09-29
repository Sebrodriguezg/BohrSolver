import matplotlib.pyplot as plt
import numpy as np

def plot_bohr_atom(Z: int, n: int, r_max: float = 3.0, decay_factor: float = 0.7):
    """
    Grafica un átomo tipo Bohr en el plano con contorno y signos en protones y electrones.
    
    Args:
        Z (int): Número de protones en el núcleo.
        n_levels (int): Número de niveles electrónicos a dibujar.
        r_max (float): Radio máximo para el nivel más externo.
        decay_factor (float): Factor de decaimiento geométrico de los radios (0 < decay_factor < 1).
    """
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Dibujar protones (pepas) con contorno y signo "+"
    theta_nucleus = np.linspace(0, 2*np.pi, Z, endpoint=False)
    r_nucleus = 0.15
    for i in range(Z):
        x = r_nucleus * np.cos(theta_nucleus[i])
        y = r_nucleus * np.sin(theta_nucleus[i])
        ax.plot(x, y, 'o', color='red', markersize=12, markeredgecolor='black', markeredgewidth=1.5)
        ax.text(x, y, "+", color='white', fontsize=8, ha='center', va='center', fontweight='bold')

    # Calcular radios de los niveles con decaimiento geométrico
    radii = [r_max * (decay_factor ** (n - i)) for i in range(1, n+1)]
    
    # Dibujar niveles
    for r in radii:
        circle = plt.Circle((0, 0), r, color='gray', fill=False, linestyle='--')
        ax.add_artist(circle)
        
    # Colocar un electrón solo en el último nivel con signo "-"
    x_e = radii[-1] * np.cos(np.pi / 4)
    y_e = radii[-1] * np.sin(np.pi / 4)
    ax.plot(x_e, y_e, 'o', color='blue', markersize=10, markeredgecolor='black', markeredgewidth=1.5)
    ax.text(x_e, y_e, "-", color='white', fontsize=8, ha='center', va='center', fontweight='bold')

    ax.set_aspect('equal', 'box')
    ax.set_xlim(-r_max-0.5, r_max+0.5)
    ax.set_ylim(-r_max-0.5, r_max+0.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(f"Átomo tipo Bohr con Z={Z} y {n_levels} niveles")
    plt.show()


def energy_transition_diagram(atom, n_i, n_f, Z=None):
    """
    Dibuja un diagrama de niveles de energía y una transición entre dos niveles.

    Args:
        atom: objeto que contiene el método energy_level
        n_i (int): nivel inicial
        n_f (int): nivel final
        Z (int, opcional): número atómico
    """
    # Asegurar que Z sea consistente
    Z_used = Z if Z is not None else getattr(atom, "Z", 1)
    
    # Calcular energía de todos los niveles hasta el máximo de n_i y n_f
    n_max = max(n_i, n_f)
    levels = []
    for n in range(1, n_max + 1):
        E = atom.energy_level(n=n, Z=Z_used)
        levels.append(E)
    
    # Dibujar niveles
    fig, ax = plt.subplots(figsize=(4, 6))
    for n, E in enumerate(levels, start=1):
        ax.hlines(E, xmin=0, xmax=1, color='blue')
        ax.text(1.05, E, f"n={n}", va='center')

    # Dibujar flecha de transición
    E_i = atom.energy_level(n=n_i, Z=Z_used)
    E_f = atom.energy_level(n=n_f, Z=Z_used)
    ax.annotate(
        '', xy=(0.5, E_f), xytext=(0.5, E_i),
        arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=8)
    )

    # Calcular energía de transición
    energy_transition = abs(E_f - E_i)  # en joules
    ax.text(0.55, (E_i + E_f)/2, f"{energy_transition:.2e} J", color='red', va='center')

    # Configuración del gráfico
    ax.set_xlim(0, 1.5)
    ax.set_xlabel('Átomo Z={}'.format(Z_used))
    ax.set_ylabel('Energía (J)')
    ax.set_title('Diagrama de Transición Electrónica')
    ax.set_xticks([])
    plt.show()