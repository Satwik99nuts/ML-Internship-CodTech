$$
This is my Task-04 which I have completed and is working completely fine. 
I am writing some of the notes here which I have collected--->
$$


# Notes:
TASK-04: Recommendation System using Collaborative Filtering
📌 What is it?
Recommendation Systems suggest items to users based on their preferences or similar users’ preferences.

🛠️ What is used?
Dataset: MovieLens (UserId, MovieId, Rating)

Approach: User-User Collaborative Filtering using Cosine Similarity

Libraries: Pandas, Scikit-Learn

💡 Why is it used?
Collaborative filtering works well when we don't know item properties.

It learns from users' behavior and preferences.

🔍 How I tackled it:
Dataset Loading: Used MovieLens dataset.

User-Item Matrix: Created using Pandas pivot table.

Similarity Calculation: Used cosine similarity to find similar users.

Recommendation Function: Recommended items rated highly by similar users.

Evaluation: Manual inspection of recommendations (could add advanced metrics later).

🎓 Key Learning Points:
Collaborative Filtering: Uses user behavior to recommend items.

Cosine Similarity: Measures how similar two users are based on their ratings.

Cold Start Problem: New users or items don’t have enough data for recommendations.

Alternative Approach: Matrix Factorization (like SVD) can improve scalability.

✅ Final Master Summary:
Task	Topic	Tools Used	Key Concepts
1	Decision Tree	Scikit-Learn	Gini, Entropy, Visualization
2	Sentiment Analysis	TF-IDF, Logistic Regression	Text Preprocessing, Classification
3	Image Classification (CNN)	TensorFlow, CNN	Convolution Layers, Pooling
4	Recommendation System	Collaborative Filtering	User-Item Matrix, Cosine Similarity

🔔 If I Were Your Teacher, I Would Ask You:
What is the difference between TF-IDF and CountVectorizer?

How do you prevent overfitting in a Decision Tree? In CNN?

What are the limitations of User-User Collaborative Filtering?

Why is softmax used in CNN classification problems?

How would you handle a new user in a recommendation system?