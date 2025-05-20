import os
import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import glob

class ChatLogParser:
    def __init__(self):
        self.user_messages = []
        self.ai_messages = []
        self.lines = []

    def parse(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.lines = file.readlines()
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            return False

        self.user_messages = []
        self.ai_messages = []
        current_speaker = None
        current_message = []

        for line in self.lines:
            line = line.strip()
            if line.startswith('User:'):
                if current_message and current_speaker:
                    message_text = ' '.join(current_message).strip()
                    self._store_message(current_speaker, message_text)
                current_speaker = 'User'
                current_message = [line[5:].strip()]
            elif line.startswith('AI:'):
                if current_message and current_speaker:
                    message_text = ' '.join(current_message).strip()
                    self._store_message(current_speaker, message_text)
                current_speaker = 'AI'
                current_message = [line[3:].strip()]
            elif line and current_speaker:
                current_message.append(line)

        if current_message and current_speaker:
            message_text = ' '.join(current_message).strip()
            self._store_message(current_speaker, message_text)

        return bool(self.user_messages or self.ai_messages)

    def _store_message(self, speaker, message):
        if speaker == 'User':
            self.user_messages.append(message)
        else:
            self.ai_messages.append(message)

    def get_messages(self):
        return self.user_messages, self.ai_messages

    def get_all_messages(self):
        return self.user_messages + self.ai_messages


if __name__ == "__main__":
    pass