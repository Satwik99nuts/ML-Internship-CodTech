$$
This is my Task-03 which I have completed and is working completely fine. 
I am writing some of the notes here which I have collected--->
$$

# NOTES:
TASK-03: Image Classification using CNN
📌 What is it?
Image Classification assigns labels to images (e.g., "cat", "dog", "car") using a Convolutional Neural Network (CNN).

🛠️ What is used?
Dataset: CIFAR-10 (10 image classes)

Model: Convolutional Neural Network

Libraries: TensorFlow, Keras, Matplotlib

💡 Why is it used?
CNNs automatically learn spatial features (edges, textures, shapes) from images.

They outperform traditional machine learning in image-related tasks.

🔍 How I tackled it:
Dataset Loading: Used CIFAR-10 directly from TensorFlow datasets.

Preprocessing: Normalized pixel values (0-255 to 0-1).

CNN Architecture: Stacked convolutional, pooling, dropout, and dense layers.

Model Compilation: Used Adam optimizer and categorical crossentropy.

Training: Trained for several epochs.

Evaluation: Measured accuracy and plotted training/validation graphs.

🎓 Key Learning Points:
Convolution Layers: Extract features like edges.

Pooling Layers: Reduce the size to make the model faster.

Overfitting: Solved by dropout layers and data augmentation.

Softmax Activation: Used in the final layer for multi-class classification.