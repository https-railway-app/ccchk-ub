import importlib
import sys
import asyncio

from flask import Flask
from ubb import Ubot
from ubb.modules import ALL_MODULES


for module_name in ALL_MODULES:
    imported_module = importlib.import_module(f"ubb.modules.{module_name}")

app = Flask(__name__)
loop = asyncio.get_event_loop()


async def main():
    async with Ubot:
        # Run the client until Ctrl+C is pressed, or the client disconnects
        print('Your bot is alive. Use .alive to check.\n'
              'Use .help to check the command list.\n'
              '(Press Ctrl+C to stop this)')
        await Ubot.run_until_disconnected()


@app.route("/", methods=['GET'])
def getMe():
    return {"MyTelegramAccount": loop.run_until_complete(main())}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
