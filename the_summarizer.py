import os
import glob
from the_parser import ChatLogParser
from the_extractor import KeywordExtractor


class ChatSummarizer:
    def __init__(self):
        self.parser = ChatLogParser()
        self.extractor = KeywordExtractor(use_tfidf=True)

    def infer_conversation_nature(self, keywords):
        # Infer the conversation nature.
        if not keywords:
            return "General conversation"
        return f"Conversation about {', '.join(keywords[:3])}"

    def summarize(self, file_path, corpus=None):
        # Create summary for a single chat
        if not self.parser.parse(file_path):
            return None

        user_messages, ai_messages = self.parser.get_messages()
        total_messages = len(user_messages) + len(ai_messages)
        total_exchanges = min(len(user_messages), len(ai_messages))
        all_messages = self.parser.get_all_messages()
        top_keywords = self.extractor.extract(all_messages, corpus=corpus)
        conversation_nature = self.infer_conversation_nature(top_keywords)

        summary = (
            f"Summary for {os.path.basename(file_path)}:\n"
            f"- The conversation had {total_exchanges} exchanges.\n"
            f"- Total messages: {total_messages} (User: {len(user_messages)}, AI: {len(ai_messages)}).\n"
            f"- {conversation_nature}.\n"
            f"- Most common keywords: {', '.join(top_keywords)}."
        )
        return summary
    
    def summarize_multiple(self, folder_path):
        """Summarize all .txt chat logs in a folder."""
        txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
        if not txt_files:
            return None

        summaries = []
        for file_path in txt_files:
            if self.parser.parse(file_path):
                corpus = [' '.join(self.parser.get_all_messages())]
                summary = self.summarize(file_path, corpus=corpus)
                if summary:
                    summaries.append(summary)
        return "\n\n".join(summaries)
    
if __name__ == "__main__":
    pass
