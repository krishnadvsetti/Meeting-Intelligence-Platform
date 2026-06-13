import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

import Agent from "./pages/Agent";
import Meetings from "./pages/Meetings";
import Upload from "./pages/Upload";

function App() {

  return (

    <BrowserRouter>

      <div style={{ padding: "20px" }}>

        <h1>
          Meeting Intelligence Platform
        </h1>

        <nav>

          <Link to="/agent">
            Agent
          </Link>

          {" | "}

          <Link to="/meetings">
            Meetings
          </Link>

          {" | "}

          <Link to="/upload">
            Upload Audio
          </Link>

        </nav>

        <hr />

        <Routes>
  <Route path="/agent" element={<Agent />} />
  <Route path="/meetings" element={<Meetings />} />
  <Route path="/upload" element={<Upload />} />
</Routes>

      </div>

    </BrowserRouter>
  );
}

export default App;