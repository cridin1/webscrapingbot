import asyncio
import telegram


TOKEN = "5247296052:AAEaZtE7W6mpDTrL754r3DCUAJZ59TYYn04"


async def main():
    bot = telegram.Bot("5247296052:AAEaZtE7W6mpDTrL754r3DCUAJZ59TYYn04")
    async with bot:
        print(await bot.get_me())

if __name__ == '__main__':
    asyncio.run(main())