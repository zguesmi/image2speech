import sys


class FatalError(Exception):

    def __init__(self, message):
        sys.exit(message)


class AppConfigNotFoundError(FatalError):

    message = 'Can not load app config file - {}'

    def __init__(self, filename):
        super().__init__(self.message.format(filename))


class InputConfigNotFoundError(FatalError):

    message = 'Can not load input config file - {}'

    def __init__(self, filename):
        super().__init__(self.message.format(filename))


class IllegalAppConfigFormatError(FatalError):

    message = 'Error parsing app config file\n{}'

    def __init__(self, err):
        super().__init__(self.message.format(err))


class IllegalInputConfigFormatError(FatalError):

    message = 'Error parsing input config file - required format is name:lang\n{}'

    def __init__(self, err):
        super().__init__(self.message.format(err))


class CustomError(Exception):

    def __init__(self, message):
        print(message)


class FileNotFoundError(CustomError):

    message = 'File not found - {}'

    def __init__(self, filename):
        super().__init__(self.message.format(filename))


class FileTypeNotSupportedError(CustomError):

    message = 'File type not supported - {}'

    def __init__(self, filename):
        super().__init__(self.message.format(filename))


class UnsupportedLanguageError(CustomError):

    message = 'Unsupported language - "{}"'

    def __init__(self, lang):
        super().__init__(self.message.format(lang))


class IllegalVoiceNameError(CustomError):

    message = 'Unsupported voice - "{}"\nDefaulting to "{}"'

    def __init__(self, voice, default):
        super().__init__(self.message.format(voice, default))


class IllegalLatencyError(CustomError):

    message = 'Illegal latency value - "{}"\nLatency should be in [0.0 .. 2.0]. Defaulting to "{}"'

    def __init__(self, latency, default):
        super().__init__(self.message.format(latency, default))


class CanNotExtractTextError(CustomError):

    message = 'Error extracting text from image - {}\n{}'

    def __init__(self, err, filename):
        super().__init__(self.message.format(filename, err))


class CanNotSaveTextError(CustomError):

    message = 'Error writing text to file - {}\n{}'

    def __init__(self, err, filename):
        super().__init__(self.message.format(filename, err))


class CanNotConvertTextToSpeechError(CustomError):

    message = 'Error extracting text from image - {}\n{}'

    def __init__(self, err, filename):
        super().__init__(self.message.format(filename, err))


class CanNotCreateConsensusFile(FatalError):

    message = 'Error creating consensus file - {}\n{}'

    def __init__(self, err, filename):
        super().__init__(self.message.format(filename, err))