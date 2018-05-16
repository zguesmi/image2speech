import os, sys, subprocess
import custom_exceptions as customExceptions

class TTS:

    '''
        this class uses mimic tts engine to convert text file to speech and saves
        it to a wav file
    '''

    _VOICES = ['ap', 'awb_time', 'awb', 'kal', 'kal16', 'rms', 'slt_hts', 'slt']
    _DEFAULT_VOICE = 'ap'
    _MIN_LATENCY, _MAX_LATENCY, _DEFAULT_LATENCY = 0.0, 2.0, 1.0
    _CMD = '/mimic/mimic -f {} -voice {} --setf duration_stretch={} -o {}'

    def __init__(self):
        pass

    
    def _isLegalVoiceName(self, voice):
        if not voice in self._VOICES:
            raise customExceptions.IllegalVoiceNameError(voice, self._DEFAULT_VOICE)


    def _isLegalLatency(self, latency):
        try:
            if not (self._MIN_LATENCY <= latency and latency <= self._MAX_LATENCY):
                raise customExceptions.IllegalLatencyError(latency, self._DEFAULT_LATENCY)
        except TypeError:
            raise customExceptions.IllegalLatencyError(latency, self._DEFAULT_LATENCY)


    def textToSpeech(self, path, voice, latency, out):

        try:
            self._isLegalVoiceName(voice)
        except customExceptions.IllegalVoiceNameError:
            voice = self._DEFAULT_VOICE

        try:
            self._isLegalLatency(latency)
        except customExceptions.IllegalLatencyError:
            latency = self._DEFAULT_LATENCY

        try:
            subprocess.call(self._CMD.format(path, voice, latency, out).split())
        except Exception as e:
            raise customExceptions.CanNotConvertTextToSpeechError(path, e)