def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 1.8) + 32
    return fahrenheit

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

def is_genap(bilangan_bulat):
    if bilangan_bulat % 2 == 0:
        return True
    else:
        return False
    
print(is_genap(4))
print(is_genap(7))