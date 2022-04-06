internet = float(input("Internet: "))
seguroAuto = float(input("Seguro del Auto: "))
gas = float(input("Gas: "))
patente = float(input("Patente: "))
luz = float(input("Luz: "))
spotify = float(input("Spotify: "))
netflix = float(input("Netflix: "))
directv = float(input("DirecTv: "))
youtube = float(input("Youtube Premiun: "))
amazon = float(input("Amazon Prime: "))
alquiler = float(input("Alquiler: "))
carrefour = float(input("Carrefour: "))
pack = float(input("Disney+/Star+/Hbo Max: "))

gastosTotales = internet + seguroAuto + gas + patente + luz + spotify + netflix + directv + youtube + amazon + alquiler + carrefour + pack
gastosCadaUno = gastosTotales / 2

mes = "Abril"

print("Contabilidad Mes " + mes + " 2022")
print("Los Gastos Totales son: ")
print("$ " + "\033[1m" + str(round(gastosTotales,2)) + "\033[0m")
print("Los Gastos de Bere de " + mes + " son: ")
print("$ " + "\033[1m" + str(round(gastosCadaUno,2)) + "\033[0m")