import os
import re
from collections import Counter
import socket

# Function to count words in a file
def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text)
            return len(words)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return 0

# Function to find top 3 frequent words
def top_frequent_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text)
            word_counts = Counter(words)
            return word_counts.most_common(3)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []

# Function to handle contractions and find top 3 frequent words
def handle_contractions(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            # Split contractions into individual words
            text = re.sub(r"(\w+)'(\w+)", r"\1 \2", text)
            words = re.findall(r'\b\w+\b', text)
            word_counts = Counter(words)
            return word_counts.most_common(3)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []

# Function to get the IP address of the machine
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Main script logic
if __name__ == "__main__":
    # Paths to the text files
    file1 = "/home/data/IF-1.txt"
    file2 = "/home/data/AlwaysRememberUsThisWay-1.txt"

    # Debug: Check if files exist
    if not os.path.exists(file1):
        print(f"Error: {file1} does not exist.")
    if not os.path.exists(file2):
        print(f"Error: {file2} does not exist.")

    # Count words in each file
    word_count1 = count_words(file1)
    word_count2 = count_words(file2)
    grand_total = word_count1 + word_count2

    # Find top 3 frequent words in IF-1.txt
    top_words_if = top_frequent_words(file1)

    # Handle contractions and find top 3 frequent words in AlwaysRememberUsThisWay-1.txt
    top_words_always = handle_contractions(file2)

    # Get the IP address
    ip_address = get_ip_address()

    # Write results to result.txt
    output_dir = "C:/Users/Nobelpreet/OneDrive/Desktop/docker/output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "result.txt")

    with open(output_file, 'w') as result:
        result.write(f"Total words in IF-1.txt: {word_count1}\n")
        result.write(f"Total words in AlwaysRememberUsThisWay-1.txt: {word_count2}\n")
        result.write(f"Grand total of words: {grand_total}\n")
        result.write(f"Top 3 frequent words in IF-1.txt: {top_words_if}\n")
        result.write(f"Top 3 frequent words in AlwaysRememberUsThisWay-1.txt (after handling contractions): {top_words_always}\n")
        result.write(f"IP address of the machine: {ip_address}\n")

    # Print the contents of result.txt to the console
    with open(output_file, 'r') as result:
        print(result.read())
