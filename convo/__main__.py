import argparse
from pathlib import Path
from conversation import Conversation

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path', help="Provide path to the conversation .txt file")
    args = parser.parse_args()
    convo_file = Path(args.path)

    if not convo_file.is_file():
        parser.exit(1, message="The conversation file doesn't exist")

    convo = Conversation(args.path)
    convo.play()
