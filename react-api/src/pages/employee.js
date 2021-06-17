import React, {Component} from 'react'
import Typography from '@material-ui/core/Typography';

class App extends Component 
{
  state =
  {
    data : [],
    isLoaded : false
  }

  async componentDidMount()
  {
  try 
  {
    const response = await fetch('http://127.0.0.1:5000/employees')
    const data = await response.json()
    console.log(data)
    setTimeout(() => {
      this.setState({ data: data.result, isLoaded : true})
    }, 500)

  }
  catch(err)
  {
    console.log(err)
  }
}

  render(){
    console.log('render method called')
    const {data, isLoaded} = this.state;
    return (
    <div>
        <Typography variant="h2" align="center">
				Employee Page 
				</Typography>
      {!isLoaded ? <div>Loading...</div> :
        
        <ul>
        {data.map((item) => {
          return <li key={item.emp_id}>{item.first_name} {item.last_name}</li>
        })}
        </ul>      
      }
    </div>
    )
  }

}

export default App