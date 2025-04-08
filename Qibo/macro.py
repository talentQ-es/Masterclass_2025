# Librerías generales
import matplotlib.pyplot as plt
import numpy as np

#qibo
import qibo
from qibo import gates
from qibo.models import Circuit
#Uso de backend de numpy en Qibo\n",
qibo.set_backend("numpy")
# Función de dibujado de circuito con matplotlib 
from qibo.ui import plot_circuit

# qiskit
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector 

# definición de funciones de ayuda 

# función para mostrar circuit de un qubit 
miplot_circuit = lambda circuit: plot_circuit(circuit, cluster_gates=False, style="quantumspain")
qsplot_circuit = lambda circuit: plot_circuit(circuit, style="quantumspain")

# función para mostrar el histrograma de un dictionario

def plot_histogram (data_dict):
    # Extract keys and values
    x_values = list(data_dict.keys())   # estados cuanticos
    #x_values =list(map(lambda x: r"$|$" + x + r"$\rangle$", data_dict.keys()))
    y_values = list(data_dict.values()) # las cuentas

    
    plt.bar(x_values, y_values, edgecolor='none', alpha=0.7)

    # Customize x-axis
    plt.xticks(x_values)  # Solo mostrar los estados cuanticos

    # Labels and title
    plt.xlabel('Medidas')
    plt.ylabel('Cuentas')
    #plt.title('Frecuencias')

    # mostrar la gráfica
    plt.show()

def pinta_circuito_mpl(qcircuit):
    return QuantumCircuit.from_qasm_str(qcircuit.to_qasm()).draw('mpl',style='iqp')


def draw_state_Bloch(qcircuit):
    return Statevector(QuantumCircuit.from_qasm_str(qcircuit.to_qasm())).draw('Bloch')

def draw_state_Latex(qcircuit):
    return Statevector(QuantumCircuit.from_qasm_str(qcircuit.to_qasm())).draw('Latex')


