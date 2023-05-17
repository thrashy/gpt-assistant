import audioop
import time
import wave
from collections import deque
from typing import List, Deque, Optional

import pyaudio
import logging


class AudioRecorder:
    """
    Class to handle audio recording.
    """

    def __init__(self, config: dict = None) -> None:
        """
        Initialize the AudioRecorder.
        """
        if config is None:
            config = {
                'FORMAT': pyaudio.paInt16,
                'CHANNELS': 1,
                'RATE': 44100,
                'CHUNK': 4096,
                'SILENCE_LIMIT': 2,
                'PREV_AUDIO': 0.5,
                'THRESHOLD': 600,
                'WAVE_OUTPUT_FILENAME': "temp.wav"
            }

        self.config = config
        self.frames: List[bytes] = []
        self.audio = pyaudio.PyAudio()

    def record_audio(self) -> None:
        """
        Record audio until a silence of length SILENCE_LIMIT is detected.
        """
        try:
            stream = self.audio.open(format=self.config['FORMAT'], channels=self.config['CHANNELS'],
                                     rate=self.config['RATE'], input=True,
                                     frames_per_buffer=self.config['CHUNK'])
            logging.info("Recording...")

            silence_start: Optional[float] = None
            prev_audio: Deque[bytes] = deque(
                maxlen=int(self.config['RATE'] / self.config['CHUNK'] * self.config['PREV_AUDIO']))
            while True:
                data: bytes = stream.read(self.config['CHUNK'])
                self.frames.append(data)
                amplitude: int = audioop.rms(data, 2)  # calculate amplitude
                if amplitude > self.config['THRESHOLD']:  # if amplitude is high enough, reset silence_start
                    silence_start = None
                elif silence_start is None:
                    silence_start = time.time()
                elif time.time() - silence_start > self.config['SILENCE_LIMIT']:
                    break  # if silence for more than the limit, break the loop
                else:
                    prev_audio.append(data)

            logging.info("Finished recording.")

            stream.stop_stream()
            stream.close()

            # Prepend audio from {PREV_AUDIO} seconds before noise was detected to the beginning of the recording
            self.frames = list(prev_audio) + self.frames

        except Exception as e:
            logging.error(f"Error while recording: {str(e)}")
            return

    def save_audio(self, output_filename: str) -> None:
        """
        Save the recorded audio to a file.
        """
        try:
            with wave.open(output_filename, 'wb') as wave_file:
                wave_file.setnchannels(self.config['CHANNELS'])
                wave_file.setsampwidth(self.audio.get_sample_size(self.config['FORMAT']))
                wave_file.setframerate(self.config['RATE'])
                wave_file.writeframes(b''.join(self.frames))

            logging.info(f"Audio saved to {output_filename}")

        except Exception as e:
            logging.error(f"Error while saving audio: {str(e)}")
            return

    def terminate(self):
        """
        Terminate the audio interface.
        """
        self.audio.terminate()
        logging.info("Audio interface terminated.")
