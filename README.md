# dev-twitter-bot
Twitter bot that posts inspirational quotes for developers

## Getting Started

Clone the repo 

```
git clone https://github.com/denibulkashvili/dev-twitter-bot.git
cd dev-twitter-bot
```

Create a new virtual environment
```
python3 -m venv tutorial-env
```

OR (with Anaconda)
```
conda create --name myenv
```

### Installing

Install required libraries 

```
pip install -r requirements.txt
```
Create a [new Twitter account and a new app](https://developer.twitter.com/en/apps) and save your credentials into .env file in the project folder.  

### Running
Run the bot with 
```
python bot.py
```

## Deployment

The bot can use a basic Flask server to run live. 

## Built With

* Python3
* Tweepy
* Requests
* Python-dotenv

## Contributing

Any contributions are welcome. 

## License

This project is licensed under the MIT License

## Acknowledgments

* Quotes are currently being pulled from [Programming Quotes API for Storm Consultancy](http://quotes.stormconsultancy.co.uk/api)
