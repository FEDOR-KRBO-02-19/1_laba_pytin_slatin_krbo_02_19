import matplotlib.pyplot as plt
import numpy as np

orientation = []
radius_vector = []

# Инициализация логов файла
log_file = open("examp17.txt", "r")

# Считывает из файла строки логов и осталуных данных в список
stroki_logov = log_file.readlines()

# Координаты движения робота
x_kord = []
y_kord = []

# инициализация датасетов
x_dataset = []
y_dataset = []

for i in stroki_logov:
    # инициализация декартовых координат робота и угла его поворота куки
    orient = i.strip().split(";")[0]

    # инициализация ридиус векторов в усвловиях полярных координат
    vectors = i.strip().split(";")[1]

    # разделенеи проинициализрванных данных
    orientation.append(orient.split(","))
    radius_vector.append(vectors.split(","))

orientation = np.array(orientation, float)
radius_vector = np.array(radius_vector, float)

for i in orientation:
    x_kord.append(i[0])
    y_kord.append(i[1])

var = 0
for x, y, alpha in orientation:
    alpha0 = alpha + 2.0944  # вычисление левого края "сектора" лидара
    for j in radius_vector[var]:
        if j != 5.6 and j >= 0.4:
            x_dataset.append((j * np.cos(alpha0)) + x + 0.3 * np.cos(alpha))
            y_dataset.append((j * np.sin(alpha0)) + y + 0.3 * np.sin(alpha))
        alpha0 -= 0.0063
    var += 1

fig, ax = plt.subplots()
ax.scatter(x_dataset, y_dataset, s=1, c="g")
ax.plot(x_kord, y_kord, linewidth=5, color='black')
plt.savefig("chernovik")
plt.show()
