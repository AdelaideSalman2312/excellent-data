# Initializing global variables 
Dera = 500 
wrapress = 650 
fittedBlazer = 800 

# Dera-Specific Style Multipliers (ONLY applies if silhouette is Dera)
Backless = 2.0
Jumpsuit = 2.5
shortBackless = 1.5
shortRomper = 1.8

# Setting Fabric Cost Multipliers
stretchJersey = 1.0
nonStretchAnkara = 1.3

# Tailoring Add on Cost
customFitting = 1500

order_log = []

# .lower() converts "Dera" -> "dera", "Fitted Blazer" -> "fitted blazer" Python s very strictly case sensitive sikujua hii
chosenSilhouette = input("Enter silhouette (dera, wrap dress, fitted blazer): ").lower().strip()

# Compare against ALL LOWERCASE strings, and use  global variables
if chosenSilhouette == "dera":
    base_price_dera = 500
    print("You have chosen the dera silhouette. The base price is " + str(base_price_dera))
elif chosenSilhouette == "wrap dress":
    base_price_wrap = 650
    print("You have chosen the wrap dress silhouette. The base price is " + str(base_price_wrap))
elif chosenSilhouette == "fitted blazer":
    base_price_fb = 800
    print("You have chosen the fitted blazer silhouette. The base price is " + str(base_price_fb))
else:
    print("Unknown Silhouette Chosen. Please Select from the available options")