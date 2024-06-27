import json

with open("config.json", "r") as f:
    bot_config = json.load(f)

# Actualizar la configuración del bot según sea necesario
bot_config["api_key"] = "YOUR_API_KEY"
bot_config["api_secret"] = "YOUR_API_SECRET"
bot_config["symbol"] = "BTCUSDT"

with open("config.json", "w") as f:
    json.dump(bot_config, f)
