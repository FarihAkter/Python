import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [students, setStudents] = useState([]);
  const [name, setName] = useState("");
  const [sid, setSid] = useState("");
  const [dept, setDept] = useState("");

  const fetchStudents = () => {
    axios.get("http://127.0.0.1:8000/students")
      .then(res => setStudents(res.data));
  };

  useEffect(() => {
    fetchStudents();
  }, []);

  const addStudent = () => {
    axios.post("http://127.0.0.1:8000/students", {
      id: sid,
      name: name,
      dept: dept
    }).then(() => {
      fetchStudents();
      setName("");
      setSid("");
      setDept("");
    });
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Student Management System</h1>

      <input placeholder="ID" value={sid} onChange={e => setSid(e.target.value)} />
      <input placeholder="Name" value={name} onChange={e => setName(e.target.value)} />
      <input placeholder="Dept" value={dept} onChange={e => setDept(e.target.value)} />

      <button onClick={addStudent}>Add Student</button>

      <h2>Student List</h2>
      {students.map((s, i) => (
        <p key={i}>{s.name} - {s.dept}</p>
      ))}
    </div>
  );
}

export default App;