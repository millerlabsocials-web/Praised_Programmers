# We are going over calculating the Gibbs Free Energy of a Galvanic Cell

# Python is like a lab drawer where you have your typical glassware (erlenmeyer, beakers, glass rods, etc)
# Sometimes we need special glassware like a buret, or a 2L erlenmeyer, or even a HotPlate, things thats arent typically in our lab drawer

import math # In this case we need some special tools like doing a logarithm which is not usual glassware like addition or subtraction would be


# I like to have my Variables that either need to be manually changed the most or that are referenced throughout commonly at the top
# In this case our constants are going to be here at the top

# Reminder Variables are a way for us to reference a value that is either dependent on another value or something that is referenced multiple times
# We do NOT like magic numbers 

# Nernst Equation
# E_cell = E_standard -(RT/nF)ln(Q)

# Constants

R = 8.314 # J/(mol K)
Temp_C = 25 # Temperature in Celsius
Temp_K = Temp_C + 273.15 # Temperature converted to Kelvin
F = 96485 # Faradays constant C/mol
n = 2 # electrons transferred

# Concentrations

zn_concentration = 0.10 # Concentration of Zn in M
cu_concentration = 1.00 # Concentration of Cu in M

# Reaction Quotient (Q) 

Q = zn_concentration / cu_concentration # Reaction quotient between zn and cu following products/reactants

# Half Reaction potentials

zn_potential = -0.76 # Potential of Zinc half rxn in Volts
cu_potential = 0.34 # Potential of Cu half rxn in Volts

# Cell Voltage
# E_standard is the cell under standard conditions

E_standard = cu_potential - zn_potential  # Performing total cell voltage calculation following EStandard = ECathode - EAnode 

# E_Cell calculation from the Nernst Equation E_cell = E_standard -(RT/nF)ln(Q)

# Here is where we uses that Math import! Typically the format is import.function in this case math.log
# math.log refers to a natural log (ln)
# To do a log in base 10 its math.log10 
# We are calculating the cell potential in V here

E_Cell = E_standard - ((R * Temp_K) / (n * F)) * math.log(Q)  # Here is where we are able to call all of the variables defined above

# Lets say that we also want to get the Delta G of the system in kJ/mol

# Delta_G = -nFE_Cell

Delta_G = -(n * F * E_Cell) # This is in J/mol so we need to convert to kJ/mol we can do it either by dividing by 1000 in this variable
                            # Or create a second variable in the event that we wanted to refer to the first
Delta_G_kj = Delta_G / 1000 # In this case since the conversion from J to kJ will always be 1/1000 we use 1000 as a value instead of a variable

# Now we actually want to get readable values from this so we will use the print function
# When using the print function if you seperate "words in quotes" (String) or Values with commas it displays as a space


print("E Standard:", E_standard ,"V")
print("E Cell:", E_Cell,"V")
print("Delta G:", Delta_G_kj, "kJ/mol")