# 💻 Simulador de Mercado de Tarjetas Gráficas - Prueba Técnica

Este proyecto es una simulación de un mercado de tarjetas gráficas donde 100 agentes pueden comprar, vender o no hacer nada en función de unas reglas definidas

El objetivo es ver cómo evoluciona el precio cuando estos agentes interactúan a lo largo de las 1.000 rondas del mercado

## 🧠 Los Agentes

- **Aleatorios (51):** Cada rona tienen 1/3 de posibilidades de comprar, vender o no hacer nada
- **Tendencias (24):** Si el precio de las tarjetas gráficas sube un 1% o más, tienen un 75% de probabilidades de comprar, si la subida no llega al 1%, tienen un 20% de vender
- **No Tendencias (24):** Si el precio de las tarjetas gráficas baja un 1% o más, tienen un 75% de probabilidades de comprar, si la baja no llega al 1%, tienen un 20% de vender
- **Maximizar (1):** Este está diseñado de forma que maximice sus ganancias y tiene que acabar con o tarjetas gráficas

## ⚙️ Cómo funciona

- El mercado empieza con 1000.000 tarjetas gráficas a un precio inicial de 200$
- Cada ronda, el orden de los agentes se mezcla y cada uno decide qué hacer dependiendo de si sube o baja el precio de las tarjetas gráficas
- El precio de las tarjetas gráficas fluctúa con cada compra o venta de los agentes, si un agente compra, el precio sube un 0.5%, si un agente vende una tarjeta gráfica, el precio baja un 0.5%
- Cada gente empieza con 1.000$ y no puede pedir prestado dinero ni vender si no tiene tarjetas gráficas

## ▶️ Cómo ejecutar

1. Tener Python 3 instalado
2. Clonar el repositorio
3. Ejecutar el archivo `main.py`
4. En la consola de comandos se podrá ver el resultado del programa