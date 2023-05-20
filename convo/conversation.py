from pathlib import Path
from participant import Participant
import pyttsx3
import random


class Conversation:
    def __init__(self, filename, participants=None):
        self._filename = filename
        self.participants = []
        self.init_participants(participants)
        self.engine = pyttsx3.init()

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        path = Path(value)
        if path.is_file():
            self._filename = value
        else:
            self._filename = None
            raise FileNotFoundError(
                f'File could not be found at the spacified path: {value}')

    def init_participants(self, value):
        if value is None:
            value = self._participants_From_file()
        for participant in value:
            if participant['name'] in [p.name for p in self.participants]:
                return
            if (self._participant_in_file(participant['name'])):
                self.participants.append(
                    Participant(**participant))
            else:
                raise ValueError(
                    f'Invalid participant {participant} encountered. Make sure they exist in conversation file: {self.filename}')

    def _participant_in_file(self, participant_name):
        if (self.filename is None):
            raise FileNotFoundError('Conversation file could not be found')
        else:
            with open(self.filename) as fp:
                for line in fp.readlines():
                    if ':' not in line:
                        raise ValueError(
                            'Conversation does not match expected in format of Person: Message')
                    else:
                        [name, _] = line.split(':')
                        if name.lower() == participant_name.lower():
                            return True
                return False

    def play(self):
        if self.filename is None:
            raise FileNotFoundError(
                f'Conversation file: {self.filename} could not be found.')

        if self.participants is None:
            raise Exception('Participants could not be found.')

        with open(self.filename) as fp:
            for line in fp.readlines():
                if ':' in line:
                    [participant_name, message] = line.split(':')
                    participant = [
                        p for p in self.participants if p.name.lower() == participant_name.lower()]
                    if len(participant) == 0:
                        raise Exception(
                            f'Partipant {participant_name} could not be found')
                    else:
                        participant = participant[0]
                        participant.say(self.engine, message)
            self.engine.say('Conversation closes...')
            self.engine.runAndWait()

    def _participants_From_file(self):
        participants = []
        if self.filename is None:
            raise FileNotFoundError(
                f'Conversation file: {self.filename} could not be found.')
        else:
            with open(self.filename) as fp:
                for line in fp.readlines():
                    if ':' not in line:
                        raise ValueError(
                            'Conversation does not match expected in format of Person: Message')
                    else:
                        [name, _] = line.split(':')

                        if name not in [p['name'] for p in participants]:
                            participants.append(
                                {'name': name, 'voice': random.choice([0, 1])})

        return participants
