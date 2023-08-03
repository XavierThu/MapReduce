import os
import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Function to read the input file and perform word count
def word_count(filename):
    encodings = ['utf-8', 'latin-1', 'ISO-8859-1', 'cp1252', 'ascii']
    
    for encoding in encodings:
        try:
            # Read the file with the specified encoding
            with open(filename, 'r', encoding=encoding, errors='replace') as file:
                text = file.read().lower()
                break
        except UnicodeDecodeError:
            continue
    else:
        raise UnicodeDecodeError("Failed to read the file with all attempted encodings.")

    # Remove non-alphanumeric characters and split the text into words
    words = re.findall(r'\b\w+\b', text)

    # Count the occurrences of each word
    word_counts = Counter(words)

    return word_counts

# Main function
if __name__ == "__main__":
    input_file = "cleaned_APPLE_iPhone_SE.txt"
    word_counts = word_count(input_file)

    total_words = sum(word_counts.values())
    unique_words = len(word_counts)

    print("Total Words:", total_words)
    print("Unique Words:", unique_words)

    # Print the most common words
    print("Most Common Words:")
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")

    # Generate and save the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('wordcloud.png', bbox_inches='tight')
    plt.show()
