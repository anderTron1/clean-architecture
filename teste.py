import asyncio

async def calcular():
    soma = 0
    for i in range(1, 100000000):
        soma += i
    print("Cálculo finalizado:", soma)

async def job(nome, tempo):
    await asyncio.sleep(tempo)
    print(f"Job {nome} finalizado após {tempo} segundos")

async def main():
    await asyncio.gather(
        calcular(),
        job("job1", 1),
    )

asyncio.run(main())