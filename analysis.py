import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def read_word_count_file(file_path):
    word_counts = {}
    with open(file_path, 'r') as file:
        for line in file:
            word, count = line.strip().split("\t")
            word_counts[word] = int(count)
    return word_counts

def generate_word_cloud(word_count, year):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_count)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f"Word Cloud - {year}")
    plt.axis('off')
    plt.savefig(f"word_cloud_{year}.png")  # Save the word cloud as an image file
    plt.close()

# File path of the output_file.txt
file_path = 'output_file.txt'

word_count = read_word_count_file(file_path)

# Print summary statistics
total_words = sum(word_count.values())
unique_words = len(word_count)
most_common_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]

print(f"Total Words: {total_words}")
print(f"Unique Words: {unique_words}")
print("Most Common Words:")
for word, count in most_common_words:
    print(f"{word}: {count}")
print("-----------------------------")

# Generate word cloud and save it as an image file
generate_word_cloud(word_count, "Word_Counts")
