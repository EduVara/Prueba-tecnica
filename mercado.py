from random import random, shuffle

from agentes import AgenteAleatorio, AgenteTendencia, AgenteNoTendencia, AgenteMaximizar


class Mercado:
    def __init__(self):
        self.precio_actual = 200.0
        self.agentes = []

        self.agentes += [AgenteAleatorio(f"Agente Aleatorio {i}") for i in range(51)]
        self.agentes += [AgenteTendencia(f"Agente Tendencia {i}") for i in range(24)]
        self.agentes += [AgenteNoTendencia(f"Agente NO Tendencia {i}") for i in range(24)]
        self.agentes += [AgenteMaximizar("Agente Maximizar")]

    def empezar_mercado(self):
        for i in range(1_000):
            precio_anterior = self.precio_actual
            shuffle(self.agentes)

            for agente in self.agentes:
                accion_agente = agente.accion(precio_anterior, self.precio_actual)

                if accion_agente == "COMPRAR" and agente.balance > self.precio_actual:
                    agente.balance -= self.precio_actual
                    agente.tarjetas += 1
                    self.precio_actual *= 1.0005
                elif accion_agente == "VENDER" and agente.tarjetas > 0:
                    agente.balance += self.precio_actual
                    agente.tarjetas -= 1
                    self.precio_actual *= 0.9995
