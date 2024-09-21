import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

# Definir los sistemas
# Sistema I
num1 = [5]
den1 = [5, 1, 0]
sys1 = ctrl.TransferFunction(num1, den1)

# Sistema II
num2 = [5, 4]
den2 = [5, 1, 0]
sys2 = ctrl.TransferFunction(num2, den2)

# Sistema III
num3 = [5]
den3 = [5, 5, 0.8]
sys3 = ctrl.TransferFunction(num3, den3)

# Simulación de la respuesta al escalón unitario
t = np.linspace(0, 10, 1000)
t1, y1 = ctrl.step_response(sys1, T=t)
t2, y2 = ctrl.step_response(sys2, T=t)
t3, y3 = ctrl.step_response(sys3, T=t)

# Graficar la respuesta al escalón
plt.figure()
plt.plot(t1, y1, label='Sistema I')
plt.plot(t2, y2, label='Sistema II')
plt.plot(t3, y3, label='Sistema III')
plt.title('Respuesta al escalón unitario')
plt.xlabel('Tiempo (s)')
plt.ylabel('Respuesta')
plt.legend()
plt.grid()
plt.show()

# Simulación de la respuesta al impulso unitario
t1, y1_imp = ctrl.impulse_response(sys1, T=t)
t2, y2_imp = ctrl.impulse_response(sys2, T=t)
t3, y3_imp = ctrl.impulse_response(sys3, T=t)

# Graficar la respuesta al impulso
plt.figure()
plt.plot(t1, y1_imp, label='Sistema I')
plt.plot(t2, y2_imp, label='Sistema II')
plt.plot(t3, y3_imp, label='Sistema III')
plt.title('Respuesta al impulso unitario')
plt.xlabel('Tiempo (s)')
plt.ylabel('Respuesta')
plt.legend()
plt.grid()
plt.show()