import React, {useEffect, useState} from 'react'
import './App.css'
import axios from 'axios';

function Employees(){
  const url = 'http://127.0.0.1:5000/employees'
  const [employee, setEmployee] = useState(null)
  
  useEffect(() => {
    axios.get(url)
    .then(response => {console.log(response.data)})
    .then(response => { 
      setEmployee(response)
    })
  }, [url])

  return(
    <div></div>
  )

}
export default Employees