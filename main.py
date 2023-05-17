from dotenv import load_dotenv
import logging
import os

from audio_recorder import AudioRecorder
from audio_transcriber import AudioTranscriber
from gpt_model import GPTModel
from text_to_speech import TextToSpeech


def main():
    load_dotenv(override=True)
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)

    wave_output_filename = "temp.wav"

    openai_api_key = os.getenv("OPENAI_API_KEY")
    openai_model = os.getenv("OPENAI_MODEL")
    openai_max_tokens = int(os.getenv("OPENAI_MAX_TOKENS"))

    recorder = AudioRecorder()
    recorder.record_audio()
    recorder.save_audio(wave_output_filename)
    recorder.terminate()

    transcriber = AudioTranscriber(openai_api_key)
    transcription = transcriber.transcribe(wave_output_filename)

    gpt_model = GPTModel(openai_api_key, openai_model, openai_max_tokens)
    answer = gpt_model.generate_gpt_response(gpt_model.create_gpt_message(transcription))

    tts = TextToSpeech()

    tts.convert(answer)
    tts.play_audio()


if __name__ == "__main__":
    main()
