import os
import shutil
from the_summarizer import ChatSummarizer

def main():
    summarizer = ChatSummarizer()
    folder_path = "chat_logs"
    single_file_path = "chat.txt"

    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    else:
        for item in os.listdir(output_dir):
            item_path = os.path.join(output_dir, item)
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)

    folder_exists = os.path.isdir(folder_path)
    folder_summaries = None
    if folder_exists:
        folder_summaries = summarizer.summarize_multiple(folder_path)
        if folder_summaries:
            print()
            print("Summaries for Chat Logs in Folder:\n\n")
            # print(folder_summaries)
            print('\n'.join('\t' + line for line in folder_summaries.splitlines()))

            with open(os.path.join(output_dir, "folder_summaries.txt"), 'w', encoding='utf-8') as f:
                f.write("Summaries for Chat Logs in Folder:\n\n")
                f.write(folder_summaries)


    if folder_summaries:
        print("\n")

    single_file_exists = os.path.isfile(single_file_path)
    single_summary = None
    if single_file_exists:
        single_summary = summarizer.summarize(single_file_path)
        if single_summary:
            if not folder_summaries:
                print()
            print("Summary for Single Chat Log:\n\n")
            print('\n'.join('\t' + line for line in single_summary.splitlines()))

            with open(os.path.join(output_dir, "single_summary.txt"), 'w', encoding='utf-8') as f:
                f.write("Summary for Single Chat Log:\n\n")
                f.write(single_summary)
    
    invalid_files = summarizer.receive_invalid_files()
    if invalid_files:
        print("\n\nList of Files that contains invalid conversation:\n")
        for cnt, inv in enumerate(invalid_files):
            print(f"\t{cnt + 1}. {inv}")

    if not folder_summaries and not single_summary:
        print("\nNo .txt files were found either within the 'chat_log' directory or in the current working directory.")


if __name__ == "__main__":
    main()