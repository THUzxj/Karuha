
import karuha
from karuha.event.bot import BotReadyEvent


@karuha.on(BotReadyEvent)
async def handle(bot: karuha.Bot) -> None:
    # create a bot without login
    tid, params = await bot.account(
        scheme = 'basic',
        secret = f'{bot.name}:test123',
        fn = 'Test User',
        tags = 'test,test-user',
        auth = 'JRWPA',
        anon = 'JW',
        cred = 'email:test@example.com',
        do_login=True
    )
    print(tid, params)
    bot.cancel()

if __name__ == "__main__":
    karuha.load_config()
    start = 270
    for i in range(start, start+3):
        _config = karuha.get_config()
        _config.bots[0].name = f"test{i}"
        karuha.run()
