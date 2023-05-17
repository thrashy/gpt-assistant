import openai
from typing import List


class GPTModel:
    """
    A wrapper for the OpenAI GPT model.
    """

    def __init__(self, api_key: str, model: str = "gpt-4", max_tokens: int = 4000, temperature: float = 0.6):
        """
        Initializes the GPTModel object with the provided parameters.

        :param api_key: The OpenAI API key.
        :param model: The model to be used, default is 'gpt-4'.
        :param max_tokens: The maximum number of tokens for generated responses, default is 4000.
        :param temperature: The temperature for generated responses, default is 0.6.
        """

        if not api_key:
            raise ValueError("API key is not provided")
        openai.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

    @staticmethod
    def create_gpt_message(user_message: str) -> List[dict]:
        """
        Creates a message in the format expected by the GPT model.

        :param user_message: The user's message.
        :return: A list containing a dictionary with the user's message.
        """

        return [{'role': 'user', 'content': f"{user_message}"}]

    def generate_gpt_response(self, messages: List[dict]) -> str:
        """
        Generates a response from the GPT model.

        :param messages: A list of messages in the format expected by the GPT model.
        :return: The GPT model's response.
        """
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        return response.choices[0].message['content'].strip()
