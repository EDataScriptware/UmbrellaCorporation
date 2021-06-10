import React, {Component} from 'react';
import Employees from './components/employees';

    class App extends Component {
      state = {
        employees: []
      }
      componentDidMount() {
        fetch('http://127.0.0.1:5000/employees')
        .then(res => res.json())
        .then((data) => {
          this.setState({ employees: data })
        })
        .catch(console.log)
      }

      render () {
        return (
          <Employees employees={this.state.employees} />
        );
      }
      
    }
    
    export default App;