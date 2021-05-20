import settings
import boto3
import json

from bot import exceptions


class Bot(object):
    def __init__(self, **kwargs):
        self.name = settings.BOT_NAME
        self.alias = settings.BOT_ALIAS
        self.client = boto3.client("lex-runtime")

    
    def send_text(self, text: str):
        response = self.client.post_text(
            botName=self.name,
            botAlias=self.alias,
            userId='string',
            sessionAttributes={
                'string': 'string'
            },
            requestAttributes={
                'string': 'string'
            },
            inputText=text,
            activeContexts=[
                {
                    'name': 'string',
                    'timeToLive': {
                        'timeToLiveInSeconds': 123,
                        'turnsToLive': 10
                    },
                    'parameters': {
                        'string': 'string'
                    }
                },
            ]
        )
        return response

    def get_text_response(self, response) -> str:
        print(response)
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            if response["dialogState"] == 'Failed':
                raise exceptions.DialogFailed
            return response["message"]


    def get_intent_method(self, response):
        intent_name = response.get("intentName")
        if intent_name:
            print(intent_name)