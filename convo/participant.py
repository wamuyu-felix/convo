class Participant:
    def __init__(self, name, voice=0, rate=200, alias=None) -> None:
        self._name = name
        self._voice = voice
        self._rate = rate
        self._alias = alias

    def __str__(self) -> str:
        return f'{self.name}: voice: {self.voice} rate: {self.rate}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        self._alias = value

    @property
    def voice(self):
        return self._voice

    @voice.setter
    def voice(self, value):
        if not value.isdigit() or 0 > value > 1:
            raise ValueError('Voice should be either 0 or 1')
        else:
            self._voice = value

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        if not value.isdigit() or 0 > value > 1:
            raise ValueError('Rate should be an integer between 50 and 400')
        else:
            self._rate = value

    def say(self, engine, message):
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[self.voice].id)
        engine.setProperty('rate', self.rate)
        name = self.alias if self.alias is not None else self.name
        print(f'{self.name}: {message}')
        engine.say(f'{name} says ')
        engine.say(message)
        engine.runAndWait()
