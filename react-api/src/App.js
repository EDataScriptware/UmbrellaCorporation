import React, {Component, Router, Route, useHistory} from 'react';
import {Navbar, Nav} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.css'
import logo from '../src/media/img/logo.png'
import raccoon_city from '../src/media/img/raccoon_city.jpeg'
import '../src/index.css'
import EmployeeComponent from "./components/employee.js"; 

class App extends Component
{

render()
{
<Router>
  <Route path="/" component={App}>
    <Route path="employee" component={EmployeeComponent} />
  </Route>
</Router>

  
  
  return(
  <div class='html'> 
  <Navbar bg="dark" variant="dark">    
      <Navbar.Brand>
      <img
        alt=""
        src={logo}
        width="35"
        height="35"
        className="d-inline-block align-top"
      />{' '}
            Umbrella Corporation{'  '} <i><quote>"Every business is life itself."</quote></i>
      <Nav className="mr-auto">
      <Nav.Link to="/" >Home</Nav.Link>
      <Nav.Link to="/employee">Employees</Nav.Link>
      <Nav.Link to="/department">Departments</Nav.Link>
      <Nav.Link to="/history">History</Nav.Link>
      </Nav>
  </Navbar.Brand>
  </Navbar>
  <h1>Raccoon City is the heart of the Umbrella Corporation.</h1>
  <img src={raccoon_city}></img>

  

  
  
  
  </div>
 
 
 
 )

}
}

export default App