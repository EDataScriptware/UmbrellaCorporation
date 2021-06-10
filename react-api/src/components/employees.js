import React from 'react'
    
    const Employees = ({ employees }) => {
      return (
        <div>
          <center><h1>Employee List</h1></center>
          {employees.map((employee) => (
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">{employee.first_name}</h5>
                <h6 class="card-subtitle mb-2 text-muted">{employee.name}</h6>
                <p class="card-text">{employee.last_name}</p>
              </div>
            </div>
          ))}
        </div>
      )
    };
    
    export default Employees