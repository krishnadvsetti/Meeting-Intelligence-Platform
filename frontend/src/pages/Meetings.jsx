import { useEffect, useState } from "react";
import axios from "axios";

function Meetings() {

  const [meetings, setMeetings] = useState([]);

  useEffect(() => {

    const fetchMeetings = async () => {

      try {

        const response = await axios.get(
          "http://127.0.0.1:8000/meetings"
        );

        setMeetings(response.data);

      } catch (error) {

        console.error(error);

      }
    };

    fetchMeetings();

  }, []);

  return (

    <div>

      <h2>Meetings Dashboard</h2>

      <table
        border="1"
        cellPadding="10"
        style={{
          borderCollapse: "collapse",
          width: "100%"
        }}
      >

        <thead>

          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Source</th>
          </tr>

        </thead>

        <tbody>

          {meetings.map((meeting) => (

            <tr key={meeting.id}>

              <td>{meeting.id}</td>
              <td>{meeting.title}</td>
              <td>{meeting.source}</td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>

  );
}

export default Meetings;