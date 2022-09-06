class CriptoView:

    def __init__(self):
        pass

    def pedir_monedas(self):
        origen = input("¿Que moneda quieres cambiar? ")
        destino = input("¿Que moneda deseas obtener? ")
        return (origen, destino)


    def mostrar_cambio(self, origen, destino, cambio):
        print("Un {} vale como {:,.2f} {}".format(
            origen, cambio, destino,
    ))


    def quieres_seguir(self):
        seguir = input("¿Quieres cambiar algo mas? (S/N) ")
        return seguir.upper()
