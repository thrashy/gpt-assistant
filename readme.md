# GPT Assistant
Audio Transcriber with GPT Model and Text-to-Speech

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [License](#license)

## Introduction
This is a Python application that records audio, transcribes it using the OpenAI API, generates a response with the
GPT model and finally converts the response to speech.

The application includes the following main components:
- `AudioRecorder`: Class to handle audio recording.
- `AudioTranscriber`: A class used to transcribe audio files using the OpenAI API.
- `GPTModel`: A wrapper for the OpenAI GPT model.
- `TextToSpeech`: A class to convert text to speech and play the speech.
- `main`: A function that orchestrates the whole process using the classes above.

## Installation
The application is written in Python 3.10 and uses a number of external libraries. The required libraries are listed
in the Python program, which can be installed with pip.

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

## Getting Started
To run the application, you need to set the `OPENAI_API_KEY` environment variable with your OpenAI API key and

This can be done by renaming the file `example.env` to `.env` in the root directory of the project, and updating
the following line:

```env
OPENAI_API_KEY=your_openai_api_key
```

Replace `your_openai_api_key` with your actual OpenAI API key.

## Usage
You can run the application with the following command:

```bash
python main.py
```

The application will start recording audio. It will stop recording when it detects a silence of length specified by
`SILENCE_LIMIT` in the `AudioRecorder` class. The recorded audio is then transcribed using the OpenAI API.
The transcription is passed to the GPT model to generate a response. The response is then converted to speech and
played back.

## License
This project is licensed under the terms of the MIT license.