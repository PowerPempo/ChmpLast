import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import simpson

# Дані для "Гватемали" з кроком 0,2 по осі X
data = {
    'X': [-4, -3.5, -3, -2.5, -2, -1.5, -1, 0, 1, 2, 3, 4],  # значення X
    'Y': [-3.5, -3.8, -4.2, -4.5, -4.6, -4.6, -4.6, -4, -3, -2, -1, 0]  # значення Y
}

# Створення DataFrame
df3 = pd.DataFrame(data)

# Побудова графіка
plt.figure(figsize=(8, 4))
plt.plot(df3['X'], df3['Y'], marker='o', linestyle='-', color='b')

# Налаштування графіка
plt.title('Візуалізація частини кривої, що обмежує площу Гватемали')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

# Показати графік
plt.show()

# Метод прямокутників для обчислення інтегралу
x_values = df3['X']
y_values = df3['Y']

# Обчислення інтегралу методом середніх прямокутників
integral = 0
n = len(x_values) - 1  # кількість інтервалів
for i in range(n):
    # Ширина кожного інтервалу
    h = x_values[i+1] - x_values[i]
    # Середнє значення на інтервалі
    f_avg = (y_values[i] + y_values[i+1]) / 2
    # Площа прямокутника
    integral += h * f_avg

# Виведення інтегралу, обчисленого методом середніх прямокутників
print("Метод середніх прямокутників")
print(f"Інтеграл: {integral}")

# Перевірка за допомогою вбудованої функції симпсона
result_scipy = simpson(y=y_values, x=x_values)

# Виведення інтегралу, обчисленого методом Симпсона
print("Перевірка методом Симпсона")
print(f"Інтеграл: {result_scipy}")
