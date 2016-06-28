##Interpret weather beacon
#Obtain color and mode.
color = input("Enter a color (BLUE or RED):")
mode = input("Enter a mode (STEADY or FLASHING:)")
color = color.upper()
mode = mode.upper()
if color == "BLUE":
	if mode == "STEADY":
		result = "Clear view."
	else:
		result = "Clouds due."
else:
	if mode == "STEADY":
		result = "Rain ahead."
	else:
		result = "Snow instead."
print("The weather forcast is",result)