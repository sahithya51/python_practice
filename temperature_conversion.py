#program to comvert temperature from celsious to farinheit
temperature_in_celsious = float(input("Enter temperature in celsious:"))
temperature_in_farinheit = (temperature_in_celsious*(9/5)) + 32
print("temperature in farinheit:",temperature_in_farinheit)

#program to comvert temperature from farinheit  to celsious 
temperature_in_farinheit = float(input("Enter temperature in farinheit:"))
temperature_in_celsious  = (5/9)*(temperature_in_farinheit - 32)
print("temperature in celsious:",temperature_in_celsious)