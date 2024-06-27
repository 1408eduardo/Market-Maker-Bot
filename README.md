# Money Market Bot

init uniswap-market-maker-bot/


The Uniswap market maker trading bot works by automatically buying and selling tokens in a liquidity pool in order to maintain a target price. The bot is programmed to buy tokens when the price falls below the target price, and to sell tokens when the price rises above the target price. This helps to keep the price of the tokens in the pool stable and balances liquidity on either side of the pool.

The bot is programmed to use a fixed target price, but it can also be adapted to use a dynamic target price. A dynamic target price can be based on a linear price path or something like a simple moving average of past prices.

The bot can be used to trade any pair of tokens that are listed on Uniswap v3 on any EVM compatible chain. The bot is setup as default to be run on the ETH/UNI pool on Goerli testnet, which allows users to test the bot without using real funds.

The following are the steps on how to set up the Uniswap market maker trading bot:

- Fork the repository from GitHub.
- Install the necessary libraries with the Node package manager (npm).
- Create a .env file and add your private key and Alchemy API key.
- Edit the mm.js file to specify the tokens that you want to trade and the target price.
- Run `node mm.js`

The bot will start trading and will automatically buy and sell tokens in order to maintain the target price.

Note the code is for demonstration purposes only and is not battle tested in a production environment.
1. Clonar el repositorio

Primero, debes clonar el repositorio de Market Maker Bot utilizando el comando git clone:

import subprocess

repo_url = "https://github.com/1408eduardo/Market-Maker-Bot.git"
clone_cmd = f"git clone {repo_url}"
subprocess.run(clone_cmd, shell=True)


2. Cambiar al directorio del repositorio clonado

Una vez clonado el repositorio, debes cambiar al directorio del repositorio clonado:
import os

repo_name = repo_url.split("/")[-1].replace(".git", "")
os.chdir(repo_name)

3. Configurar el bot

Para configurar el bot, debes leer la configuración del bot desde el archivo config.json y actualizarla según sea necesario:

import json

with open("config.json", "r") as f:
    bot_config = json.load(f)

# Actualizar la configuración del bot según sea necesario
bot_config["api_key"] = "YOUR_API_KEY"
bot_config["api_secret"] = "YOUR_API_SECRET"
bot_config["symbol"] = "BTCUSDT"

with open("config.json", "w") as f:
    json.dump(bot_config, f)

    4. Iniciar el bot

Finalmente, debes iniciar el bot utilizando el comando python main.py:

import subprocess

start_cmd = "python main.py"
subprocess.run(start_cmd, shell=True)
5. Función completa

Aquí te muestro la función completa que clona el repositorio, configura el bot y lo inicia:

import os
import subprocess
import json

def clone_and_configure_bot(repo_url):
    # Clonar el repositorio
    clone_cmd = f"git clone {repo_url}"
    subprocess.run(clone_cmd, shell=True)

    # Cambiar al directorio del repositorio clonado
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    os.chdir(repo_name)

    # Configurar el bot
    with open("config.json", "r") as f:
        bot_config = json.load(f)

    # Actualizar la configuración del bot según sea necesario
    bot_config["api_key"] = "YOUR_API_KEY"
    bot_config["api_secret"] = "YOUR_API_SECRET"
    bot_config["symbol"] = "BTCUSDT"

    with open("config.json", "w") as f:
        json.dump(bot_config, f)

    # Iniciar el bot
    start_cmd = "python main.py"
    subprocess.run(start_cmd, shell=True)

repo_url = "https://github.com/1408eduardo/Market-Maker-Bot.git"
clone_and_configure_bot(repo_url)
Recuerda reemplazar YOUR_API_KEY y YOUR_API_SECRET con tus credenciales de API reales.

