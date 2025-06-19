$$
This is my Task-02 which I have completed and is working completely fine. 
I am writing some of the notes here which I have collected--->
$$

# Notes:
TASK-02: Sentiment Analysis using TF-IDF and Logistic Regression
📌 What is it?
Sentiment Analysis is a type of Natural Language Processing (NLP) where we classify text as Positive, Negative, or Neutral based on its emotional tone.

🛠️ What is used?
TF-IDF Vectorization: Converts text into numerical features.

Logistic Regression: Used to classify the text.

Libraries: Pandas, Scikit-Learn, NLTK

💡 Why is it used?
TF-IDF helps highlight important words that are unique to specific sentiments.

Logistic Regression is simple, fast, and effective for binary or multi-class classification.

🔍 How I tackled it:
Dataset Preparation: Used customer reviews labeled as Positive or Negative.

Text Preprocessing: Removed punctuation, stopwords, and lowercased the text.

Feature Extraction: Used TF-IDF to convert cleaned text into a numerical format.

Model Training: Applied Logistic Regression to predict sentiments.

Evaluation: Checked accuracy, precision, recall, F1-score, and plotted confusion matrix.

🎓 Key Learning Points:
TF-IDF (Term Frequency-Inverse Document Frequency) gives more weight to important words.

Logistic Regression outputs probabilities and uses a sigmoid function to classify.

Text preprocessing is essential to remove noise.

