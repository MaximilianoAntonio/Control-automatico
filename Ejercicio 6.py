import control as ctrl
import matplotlib.pyplot as plt

# Parámetros del sistema
k = 0.2  # Valor de k determinado
num = [16]
den = [1, (16*k+0.8), 16]

# Crear el sistema en lazo cerrado
sys = ctrl.TransferFunction(num, den)

# Simulación de la respuesta al escalón
t, y = ctrl.step_response(sys)

# Graficar la respuesta

plt.plot(t, y, label='Respuesta al escalón unitario')
plt.title('Respuesta al escalón unitario (k = 0.2)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Respuesta')
plt.axvline(x=0.604, color='red', linestyle='--', label='Tiempo de levantamiento (Tr) 0.604 [s]')
plt.axvline(x=0.907, color='green', linestyle='--', label='Tiempo peak (Tp) 0.907 [s]')
plt.axvline(x=2, color='purple', linestyle='--', label='Tiempo de asentamiento (Ts) 2 [s]')
plt.plot([], [], ' ', label='Sobrepaso 16.3%')
plt.grid()
plt.legend() 
plt.show()