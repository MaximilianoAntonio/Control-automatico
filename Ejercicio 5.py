import control as ctrl
import matplotlib.pyplot as plt

# Sistema original
num_orig = [10]
den_orig = [1, 1, 10]
sys_orig = ctrl.TransferFunction(num_orig, den_orig)

# Sistema con nueva retroalimentación
K_h = 2.16
num_new = [10]
den_new = [1, 1, 10*K_h]
sys_new = ctrl.TransferFunction(num_new, den_new)

# Simulación de la respuesta al escalón
t, y_orig = ctrl.step_response(sys_orig)
t2, y_new = ctrl.step_response(sys_new)

# Graficar resultados
plt.plot(t, y_orig, color='b', label='Sistema Original')
plt.title('Respuesta al escalón unitario')
plt.xlabel('Tiempo (s)')
plt.ylabel('Respuesta')
plt.legend()
plt.grid()
plt.show()

# Graficar resultados
plt.plot(t2, y_new, color='r', label='Sistema con nueva retroalimentación')
plt.title('Respuesta al escalón unitario')
plt.xlabel('Tiempo (s)')
plt.ylabel('Respuesta')
plt.legend()
plt.grid()
plt.show()

# Graficar resultados
plt.plot(t, y_orig, color='b', label='Sistema Original')
plt.plot(t2, y_new, color='r', label='Sistema con nueva retroalimentación')
plt.title('Respuesta al escalón unitario')
plt.xlabel('Tiempo (s)')
plt.ylabel('Respuesta')
plt.legend()
plt.grid()
plt.show()
