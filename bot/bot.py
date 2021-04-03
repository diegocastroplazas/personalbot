import settings
import boto3
import json

from bot import exceptions


class Bot(object):
    def __init__(self, **kwargs):
        self.name = settings.BOT_NAME
        self.client = boto3.client("lex-runtime")
    
    def send_text(self, text: str):
        response = self.client.post_text(
            botName=self.name,
            botAlias='Prod',
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
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            if response["dialogState"] == 'Failed':
                raise exceptions.DialogFailed
            return response["message"]