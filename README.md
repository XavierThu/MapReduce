# MapReduce
This is a MapReduce assignment implemented on AWS EC2.

The dataset used is "APPLE_iPhone_SE.csv" downloaded from [https://www.kaggle.com/datasets/therohk/examine-the-examiner](https://www.kaggle.com/datasets/kmldas/apple-iphone-se-reviews-ratings). 

The "preprocess.py" code is used for data preprocessing, including tasks like removing stop words and performing lemmatization.

The "Non-MapReduce.py" is a Python code that performs a similar word frequency count using a non-MapReduce algorithm. The results of this Python code are saved in the "python_results" folder.

The "analysis.py" file is used to analyze word frequencies and generate a word cloud based on those frequencies. 

The "WordCount.java," "WordMapper.java," and "SumReducer.java" contain the driver, mapper, and reducer codes respectively, used for counting word frequencies. 

The 'output_file.txt' is the output from downloading using WinSCP after doing the AWS Wordcount

The "word_cloud_Word_Counts.png" is the output of gain from running 'analysis.py'

The 'wordcloud.png' is the output gain from running 'Non-MapReduce.py'
