# Initializing global variables 
Dera = 500 
wrapress = 650 
fittedBlazer = 800 

# Dera-Specific Style Multipliers
Backless = 2.0
Jumpsuit = 2.5
shortBackless = 1.5
shortRomper = 1.8

# Fabric Cost Multipliers
stretchJersey = 1.0
nonStretchAnkara = 1.3

# Tailoring Add-on Flat Cost
customFitting = 1500

order_log = []

# --- 1. SKU & METADATA INPUTS ---
SKU_ID = input("Enter SKU ID: ").strip()
sizeLabel = input("Enter Size Label (e.g., UK 16, UK 20, UK 24): ").strip().upper()
region = input("Enter Region: ").strip()
paymentMethod = input("Enter Payment Method (COD vs Mobile Money): ").strip()

# --- 2. SILHOUETTE SELECTION ---
chosenSilhouette = input("Enter silhouette (dera, wrap dress, fitted blazer): ").strip().lower()

base_price = 0

if chosenSilhouette == "dera":
    base_price = Dera
elif chosenSilhouette in ["wrap dress", "wrapress"]:
    base_price = wrapress
elif chosenSilhouette == "fitted blazer":
    base_price = fittedBlazer
else:
    print("Unknown Silhouette Chosen. Defaulting base price to 0.")

# --- 3. FABRIC & STYLE SELECTION ---
if chosenSilhouette == "dera":
    print("\nOptions for Dera: stretch jersey, non stretch ankara, backless, jumpsuit, short backless, short romper")
else:
    print("\nOptions: stretch jersey, non stretch ankara")

fabricType = input("Enter choice: ").strip().lower()

# Determine fabric/style multiplier
if fabricType == "stretch jersey":
    fabric_multiplier = stretchJersey
elif fabricType == "non stretch ankara":
    fabric_multiplier = nonStretchAnkara
elif chosenSilhouette == "dera" and fabricType == "backless":
    fabric_multiplier = Backless
elif chosenSilhouette == "dera" and fabricType == "jumpsuit":
    fabric_multiplier = Jumpsuit
elif chosenSilhouette == "dera" and fabricType == "short backless":
    fabric_multiplier = shortBackless
elif chosenSilhouette == "dera" and fabricType == "short romper":
    fabric_multiplier = shortRomper
else:
    fabric_multiplier = 1.0
    print("Unknown option entered. Defaulting fabric multiplier to 1.0.")

# --- 4. SIZE MULTIPLIER CALCULATION ---
if sizeLabel in ["UK 16", "UK 18"]:
    sizeMultiplier = 1.0
elif sizeLabel in ["UK 20", "UK 22"]:
    sizeMultiplier = 1.2
elif sizeLabel in ["UK 24", "UK 26"]:
    sizeMultiplier = 1.5
else:
    sizeMultiplier = 1.0
    print("Unknown Size Label. Defaulting size multiplier to 1.0.")

# --- 5. CUSTOM TAILORING ADD-ON ---
customTailoring = input("Do you want custom tailoring? (yes/no): ").strip().lower()

if customTailoring in ["yes", "y"]:
    tailoring_cost = customFitting
else:
    tailoring_cost = 0

# --- 6. FINAL PRICING CALCULATION ---
if base_price > 0:
    # Base price scaled by size and fabric/style multipliers, plus fixed tailoring fee
    subtotal = (base_price * sizeMultiplier * fabric_multiplier)
    final_total = subtotal + tailoring_cost

    print("\n" + "="*30)
    print("        ORDER BREAKDOWN        ")
    print("="*30)
    print(f"SKU ID: {SKU_ID}")
    print(f"Silhouette: {chosenSilhouette.title()}")
    print(f"Size: {sizeLabel}")
    print(f"Fabric/Style: {fabricType.title()}")
    print("-" * 30)
    print(f"Base Price:            KES {base_price:.2f}")
    print(f"Size Multiplier:       x{sizeMultiplier}")
    print(f"Fabric Multiplier:     x{fabric_multiplier}")
    print(f"Tailoring Fee:         + KES {tailoring_cost:.2f}")
    print("-" * 30)
    print(f"FINAL TOTAL:           KES {final_total:.2f}")
    print("="*30)