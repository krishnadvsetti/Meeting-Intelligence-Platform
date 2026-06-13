import { useState } from "react";
import axios from "axios";

function Upload() {

  const [file, setFile] = useState(null);
  const [transcript, setTranscript] = useState("");

  const uploadAudio = async () => {

    if (!file) {
      alert("Please select a file");
      return;
    }

    try {

      const formData = new FormData();

      formData.append(
        "file",
        file
      );

      const response = await axios.post(
        "http://127.0.0.1:8000/upload-audio",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        }
      );

      console.log(response.data);

      setTranscript(
  response.data.transcript
);

    } catch (error) {

  console.error(error);

  alert(
    JSON.stringify(
      error.response?.data || error.message
    )
  );
  
    }
  };

  return (
    <div style={{ padding: "20px" }}>

      <h1>Upload Audio</h1>

      <input
        type="file"
        accept=".mp3,.wav"
        onChange={(e) =>
          setFile(e.target.files[0])
        }
      />

      <p>
        Selected File:
        {" "}
        {file ? file.name : "None"}
      </p>

      <button onClick={uploadAudio}>
        Upload
      </button>

      <hr />

      <h2>Transcript</h2>

      <textarea
        rows="15"
        cols="100"
        value={transcript}
        readOnly
      />

    </div>
  );
}

export default Upload;