from .bhashini_asr import BhashiniASR
from .whisper_asr import WhisperASR
from .faster_whisper_asr import FasterWhisperASR

class ASRFactory:
    @staticmethod
    def create_asr_pipeline(type, **kwargs):
        if type == "whisper":
            return WhisperASR(**kwargs)
        if type == "faster_whisper":
            return FasterWhisperASR(**kwargs)
        if type == "bhashini":
            return BhashiniASR(**kwargs)
        else:
            raise ValueError(f"Unknown ASR pipeline type: {type}")
