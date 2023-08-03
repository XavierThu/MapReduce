import pandas as pd
import nltk
from nltk.corpus import stopwords
import string

# Download the NLTK resources (stopwords) if not already downloaded
nltk.download('stopwords')

# Load the dataset
df = pd.read_csv('APPLE_iPhone_SE.csv')

# Text preprocessing steps
# Set text to lower case
review = df['Reviews'].apply(lambda x: x.lower())

# Tokenization
review = review.apply(nltk.word_tokenize)

# Removing Stop Words
stop_words = set(stopwords.words('english'))
review = review.apply(lambda x: [word for word in x if word not in stop_words])

# Removing Special Characters and Punctuation
review = review.apply(lambda x: [word for word in x if word.isalnum()])

# Stemming text
stemmer = nltk.stem.SnowballStemmer('english')
review = review.apply(lambda x: " ".join(stemmer.stem(word) for word in x))

# Save the cleaned dataset to a new txt file
with open('cleaned_APPLE_iPhone_SE.txt', 'w') as txt_file:
    txt_file.write(" ".join(review.tolist()))

print("Text written to cleaned_APPLE_iPhone_SE.txt file.")
