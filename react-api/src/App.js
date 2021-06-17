// React.js
import React from 'react';

// Components
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
import Navbar from './component/navbar';
import Container from '@material-ui/core/Container';

// Pages
import HomePage from './pages/home';
import EmployeePage from "./pages/employee.js"; 
import DepartmentPage from './pages/department'
import HistoryPage from './pages/history'

// CSS
import 'bootstrap/dist/css/bootstrap.css'
import '../src/index.css'


function App() { 
  return(
  <div>
    <Router>
      <Container fixed>
      <Navbar />
        <Switch>
        <Route exact path="/">
                <HomePage />
        </Route>
        <Route exact path="/employee">
              <EmployeePage />
        </Route>
        <Route exact path="/department">
                <DepartmentPage />
        </Route>
        <Route exact path="/history">
                <HistoryPage />
        </Route>
        </Switch>
  
        </Container>
    </Router>
  </div>
  )

}

export default App
