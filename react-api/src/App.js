import React, { useState } from "react";
import "./App.css";

const url = "127.0.0.1:5000/employees";

function App() {
  const [employee, setUserData] = useState({});

  // WIP
  return (
    <div className="App">
      <header className="App-header">
        <h2>Employee List Data - Work In Progress</h2>
      </header>
      <div className="user-container">
        <h5 className="info-item">{employee.first_name}</h5>
        <h5 className="info-item">{employee.last_name}</h5>
        <h5 className="info-item">{employee.emp_id}</h5>
        <h5 className="info-item">{employee.city}</h5>
      </div>
    </div>
  );
}

export default App;