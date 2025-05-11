from mercado import Mercado

if __name__ == '__main__':
    mercado = Mercado()
    mercado.empezar_mercado()

    print(f"{'Agente':<15} | {'Balance ($)':>12} | {'Tarjetas':>9}")
    print("-" * 42)
    for agente in mercado.agentes:
        print(f"{agente.tipo:<15} | {agente.balance:12.2f} | {agente.tarjetas:9d}")
    print("-" * 42)
    print(f"Precio final de las tarjetas gráficas{mercado.precio_actual:12.2f}")
    print(f"{'Precio final de las tarjetas gráficas:':} ${mercado.precio_actual:,.2f}")