from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
import numpy as np
import cv2

app = Flask(__name__)

CORS(app)

# Load model
model = load_model("model/digit_model.keras")

print("✅ Model Loaded Successfully!")


@app.route('/')
def home():

    return "MNIST Backend Running"


@app.route('/predict', methods=['POST'])

def predict():

    try:

        file = request.files['image']

        img = np.frombuffer(

            file.read(),

            np.uint8

        )


        # Convert to grayscale

        img = cv2.imdecode(

            img,

            cv2.IMREAD_GRAYSCALE

        )


        # Resize to MNIST size

        img = cv2.resize(

            img,

            (28,28)

        )


        # Invert colors

        img = cv2.bitwise_not(

            img

        )


        # Convert to black & white

        _, img = cv2.threshold(

            img,

            100,

            255,

            cv2.THRESH_BINARY

        )


        # Normalize

        img = img.astype(

            "float32"

        )

        img = img / 255.0


        # Reshape

        img = img.reshape(

            1,

            28,

            28,

            1

        )


        # Predict

        prediction = model.predict(

            img

        )


        digit = int(

            np.argmax(

                prediction

            )

        )


        confidence = float(

            np.max(

                prediction

            ) * 100

        )


        print(

            "Prediction :",

            digit

        )

        print(

            "Confidence :",

            round(

                confidence,

                2

            ),

            "%"

        )


        return jsonify({

            "prediction": digit,

            "confidence":

            round(

                confidence,

                2

            )

        })


    except Exception as e:

        print(e)

        return jsonify({

            "error": str(e)

        })


if __name__ == "__main__":

    app.run(

        debug=True

    )