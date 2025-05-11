from random import choice, choices

class Agente:
    def __init__(self, tipo):
        self.tipo = tipo
        self.balance = 1_000.0
        self.tarjetas = 0

    def accion(self, precio_anterior, precio_actual):
        raise NotImplementedError

    def actualizar_stock(self, accion):
        if accion == "COMPRAR":
            self.tarjetas += 1
        elif accion == "VENDER" and self.tarjetas > 0:
            self.tarjetas -= 1


class AgenteAleatorio(Agente):
    def accion(self, precio_anterior, precio_actual):
        return choices(["COMPRAR", "VENDER", "NO HACER NADA"], weights=[1,1,1])[0]


class AgenteTendencia(Agente):
    def accion(self, precio_anterior, precio_actual):
        cambio_precio = ((precio_actual - precio_anterior) / precio_anterior) * 100

        if cambio_precio >= 1:
            return choices(['COMPRAR', 'NO HACER NADA'], weights=[75, 25])[0]
        else:
            return choices(['VENDER', 'NO HACER NADA'], weights=[20, 80])[0]

class AgenteNoTendencia(Agente):
    def accion(self, precio_anterior, precio_actual):
        cambio_precio = ((precio_actual - precio_anterior) / precio_anterior) * 100

        if cambio_precio <= -1:

            resultado = choices(['COMPRAR', 'NO HACER NADA'], weights=[75, 25])[0]
            print("++++++++++++++++++++++++++++++++++++++")
            print("++++++++++++++++++++++++++++++++++++++")
            print(resultado)
            return resultado
        else:
            return choices(['VENDER', 'NO HACER NADA'], weights=[20, 80])[0]


class AgenteMaximizar(Agente):
        def __init__(self, tipo):
            super().__init__(tipo)
            self.historial_precios = []

        def accion(self, precio_anterior, precio_actual):
            self.historial_precios.append(precio_actual)

            if len(self.historial_precios) > 2:
                ultimo_precio, penultimo_precio = self.historial_precios[-2:]
                if penultimo_precio > ultimo_precio:
                    if self.tarjetas > 0:
                        return "VENDER"
                elif ultimo_precio > penultimo_precio:
                    if self.balance >= precio_actual:
                        return "COMPRAR"
                else:
                    "NO HACER NADA"
            return "OK"