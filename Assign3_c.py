import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5.0, 6.0, 100)
y = np.linspace(-5.0,6.0, 100)
X, Y = np.meshgrid(x,y)
F = (X-47/15)**2 + (Y+3/5)**2 - (293/45) 
plt.contour(X,Y,F,[0])
x_values = [6, 0] 
y_values = [-11/4, 7/4] 
plt. plot(x_values, y_values)
plt.title('Line and Circle')
plt.plot(47/15, -3/5, 'o', color='black');
plt.text(47/15, -3/5,'  C(47/15, -3/5)')
plt.plot(1, -2, 'o', color='black');
plt.text(1, -2,'  P(1, -2)')
plt.plot(4, -3, 'o', color='black');
plt.text(4, -3.4,'  Q(4, -3)')
plt.text(-.7, 7/4,'3x + 4y = 7')
plt.show()

