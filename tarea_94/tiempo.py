def tierra(tiempocaida):
    z= 9.8*(int(tiempocaida)**2)
    return z
def marte(tiempocaida):
    z= 3.7*(int(tiempocaida)**2)
    return z
def jupyter(tiempocaida):
    z= 24.8*(int(tiempocaida)**2)
    return z

t=input("Introduzca el tiempo que tardó el objeto en llegar al suelo :")
print("La altura a la que estaba el objeto en la Tierra era :" +str(tierra(t)))
print("La altura a la que estaba el objeto en la Marte era :" + str(marte(t)))
print("La altura a la que estaba el objeto en la Jupiter era :" + str(jupyter(t)))