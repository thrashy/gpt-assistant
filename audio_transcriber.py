import openai
import os
from contextlib import closing


class AudioTranscriber:
    """
    A class used to transcribe audio files using the OpenAI API.

    :param api_key : str the OpenAI API key to be used for transcription

    Methods
    -------
    transcribe(audio_file_path)
        Returns the transcription of the audio file at the given path.
    """

    def __init__(self, api_key: str):
        """
        Constructs the AudioTranscriber with the given API key or fetches from environment variables.

        :param api_key: the OpenAI API key to be used for transcription
        :raises ValueError If no api_key is provided or found in environment variables
        """
        api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("Missing OPENAI_API_KEY environment variable or API key not provided")
        openai.api_key = api_key

    @staticmethod
    def transcribe(audio_file_path: str) -> str:
        """
        Transcribes the audio file at the given path.

        :param audio_file_path: The path of the audio file to transcribe
        :returns The transcription of the audio file
        :raises FileNotFoundError If no file is found at the given path
        :raises ValueError If transcription could not be performed
        """
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"No audio file found at {audio_file_path}")

        with closing(open(audio_file_path, "rb")) as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)

            if transcript is None or not transcript.text:
                raise ValueError(f"Could not transcribe audio file at {audio_file_path}")

            return transcript.text
