import "./App.css";
import { useState } from "react";

function App() {

  const [image,setImage]=useState(null);

  const [result,setResult]=useState("");

  const [confidence,setConfidence]=useState("");


  const predict=async()=>{

    if(!image){

      alert("Please upload image");

      return;

    }

    const formData=new FormData();

    formData.append(

      "image",

      image

    );


    const response=await fetch(

      "http://127.0.0.1:5000/predict",

      {

        method:"POST",

        body:formData

      }

    );


    const data=await response.json();

    setResult(data.prediction);

    setConfidence(data.confidence);

  };


  return(

    <div className="container">

      <div className="card">

        <h1>

          Handwritten Digit Classifier

        </h1>

        <p>

          Upload a handwritten digit image

        </p>

        <input

          type="file"

          accept="image/*"

          onChange={(e)=>

            setImage(

              e.target.files[0]

            )

          }

        />

        <br/><br/>

        {

          image &&

          <img

            src={URL.createObjectURL(image)}

            className="preview"

            alt="digit"

          />

        }

        <br/>

        <button

          onClick={predict}

        >

          Predict

        </button>

        <h2>

          Predicted Digit :

          {result}

        </h2>

        <h3>

          Confidence :

          {confidence} %

        </h3>

      </div>

    </div>

  );

}

export default App;