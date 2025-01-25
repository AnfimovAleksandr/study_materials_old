import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()


#   Напечатается следующее:
#       Task A: Compute factorial(2)...
#       Task B: Compute factorial(2)...
#       Task C: Compute factorial(2)...
#       Task A: factorial(2) = 2
#       Task B: Compute factorial(3)...
#       Task C: Compute factorial(3)...
#       Task B: factorial(3) = 6
#       Task C: Compute factorial(4)...
#       Task C: factorial(4) = 24

#       Параллельно запуститься вычисление 3 факториалов сначала A, потом B и после С. В первую секунду они пройдут первый раз цикл for. После этого они ждут секунду и начинают следующий. На втором этапе завершается вычисление А, а факториалы В и С второй раз проходят цикл. Аналогично на следующем этапе завершается В и продолжается С. Наконец последним завершается С.