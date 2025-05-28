# TelegramChatbot - Front
Interface for Telegram chatbot.

# Using requirements.in file
1. Create a new virtual environment
2. Activate the virtual environment
3. Make sure you have the latest pip3 version: `python3 -m pip install --upgrade pip`
4. Install `pip-tools`
```BASH
(venv)project_folder: pip3 install pip-tools
```
5. Compile the `requirements.in` file:
```BASH
pip-compile
```
6. Finally we install the package through `pip-sync`:
```BASH
pip-sync
```
This command will install all the packages listed in the `requirments.txt` file.
If we dont pass any arguments with the command the default value will be `requirements.txt` file

Example of `pip-sync` with parameter:
```BASH
pip-sync requirements.txt
```

# Store your Telegram token
```BASH
export BOT_TOKEN=your-bot-token-here
```

## Store your Telegram token for debug in VSCode
If you are working with VSCode, you can create a `launch.json` file to export and set locally your `BOT_TOKEN`.
1. In the root project, execute the following command to create the file:
```BASH
mkdir ".vscode" && touch "./.vscode/launch.json"
```
2. Paste the following content into `launch.json` using your `BOT_TOKEN`:
```JSON
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: TelegramBot",
            "type": "debugpy",
            "request": "launch",
            // ENV VARS.
            "env" : {
                "BOT_TOKEN" : "your-bot-token-here",
            },
            "justMyCode": true
        }
    ]
}
```
Following the steps from above, you will have the `BOT_TOKEN` available for debug.

# Running the project
Execute the following command:
```BASH
python3 telegram_bot.py
```

## Sources
* [pip-tools](https://suyojtamrakar.medium.com/managing-your-requirements-txt-with-pip-tools-in-python-8d07d9dfa464)
* [TelegramBot simple examples](https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/)
* [TelegramBotApi Docs](https://github.com/eternnoir/pyTelegramBotAPI)

# Important notes
1. Change the BOT_TOKEN for your own Telegram Token.
2. Change the BASE_API_URL for the API of your services.