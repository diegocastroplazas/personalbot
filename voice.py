from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir
from playsound import playsound


class Voice(object):
    def __init__(self):
        session = Session(profile_name="default")
        self.polly = session.client("polly")

    def say(self, text):
        response = self.polly.synthesize_speech(
            Text=text, 
            OutputFormat="mp3",
            VoiceId="Miguel"
        )
        with closing(response["AudioStream"]) as stream:
            output = os.path.join('/home/diego/', 'output.mp3')
            with open(output, "wb") as file:
                file.write(stream.read())

            playsound(output)