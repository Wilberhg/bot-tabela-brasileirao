from brasileirao.brasileirao import Brasileirao

with Brasileirao(driver_path="C:/SeleniumDrivers/chromedriver.exe") as bot:
    bot.access_site()
    bot.scroll_table()
    bot.next_round()