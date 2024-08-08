import random
caracteres="iushoidvfdnvinfd463576586791435nfdvnfdvnfvnifdnvifdnvoihvoidsvpodshpspeurhfóiewjfaodsnckjnxmnvfijh2325252vpiurehfisfoisnjdnvajdfgpia"

longitud=int(input("longitud de la contraseña: "))
resultado=""
for i in range(longitud):
    resultado+=random.choice(cracteres)

print(f"tu contraseña es: {resultado}")

