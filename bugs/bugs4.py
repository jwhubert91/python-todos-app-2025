temperatures = [10, 12, 14]
temperatures = [f"{str(temperature)}\n" for temperature in temperatures]
file = open("file.txt", 'w')
file.writelines(temperatures)

file.close()