import { useState } from "react";
import axios from "axios";

function Agent() {

  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const askAgent = async () => {

    try {

      const result = await axios.post(
        "http://127.0.0.1:8000/agent",
        {
          query: query
        }
      );

      setResponse(
  result.data.response
);
      

    } catch (error) {

      console.error(error);

      setResponse(
        "Agent request failed."
      );
    }
  };

  return (
    <div style={{ padding: "20px" }}>

      <h1>Meeting Intelligence Agent</h1>

      <input
        type="text"
        value={query}
        onChange={(e) =>
          setQuery(e.target.value)
        }
        placeholder="Ask a question..."
        style={{
          width: "400px",
          padding: "10px"
        }}
      />

      <button
        onClick={askAgent}
        style={{
          marginLeft: "10px"
        }}
      >
        Ask Agent
      </button>

      <div
  style={{
    marginTop: "20px",
    whiteSpace: "pre-wrap"
  }}
>
  {JSON.stringify(
    response,
    null,
    2
  )}
</div>

    </div>
  );
}

export default Agent;