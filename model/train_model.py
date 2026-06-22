from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Load dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Reshape
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

# Normalize
X_train = X_train / 255.0
X_test = X_test / 255.0

# Create CNN model
model = Sequential([
    
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)), #scans image using 32 filters
    
    MaxPooling2D((2,2)), # reduces image size
    
    Flatten(),
    
    Dense(128, activation='relu'),
    
    Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(
    X_train,
    y_train,
    epochs=5,
    validation_data=(X_test, y_test)
)

model.save("digit_model.keras")

print("Model saved successfully!")