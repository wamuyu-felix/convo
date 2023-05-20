# Conversation Reader

This Python module allows you to read out a conversation stored in a text file using the `pyttsx3` library. The script can be executed from the command line by typing `python convo path_to_conversation_file`.

## Installation

To use this module, you need to have Python installed on your system. Additionally, make sure you have the following dependencies installed:

- `pyttsx3` version 2.90
- `argparse`

You can install these dependencies by running the following command:

```shell
pip install pyttsx3==2.90 argparse
```

Alternatively you could run the following command:

```shell
pip install -r requirements.txt
```

## Usage

To run the script, navigate to `convo` directory and execute the following command:

```shell
python convo path_to_conversation_file
```

Replace `path_to_conversation_file` with the actual path to your conversation file. The conversation file should be a plain text file containing the dialogues.

For example, if your conversation file is named `conversation.txt` and it is located in the the convo directory, you can run the following command:

```shell
python convo conversation.txt
```

## Example Conversation File Format

The conversation file should follow a specific format to be correctly read by the module. Each line in the file represents a single message in the conversation, and the format for each line should be as follows:

```
[Sender]: [Message]
```

Here's an example conversation file:

```
User1: Hello, how are you?
User2: I'm good, thanks! How about you?
User1: I'm doing great, thanks for asking.
```

## Output

When you run the script, it will read the conversation file and read out each message using the default text-to-speech engine provided by `pyttsx3`.

The script will display the dialogue line by line, indicating the sender and their message. The text will be read out using the system's default audio output.

## License

This module is licensed under the [MIT License](LICENSE). Feel free to modify and use it in your own projects.

## Credits

This module was developed by [Felix King]. If you have any questions or suggestions, please feel free to contact me at [wamuyufelixking@email.com].
