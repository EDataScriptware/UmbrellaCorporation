import React, {Component} from 'react'
import Typography from '@material-ui/core/Typography';
import Card from 'react-bootstrap/Card'
import CardDeck from 'react-bootstrap/CardDeck'

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
    const {data, isLoaded} = this.state;
    return (
    <div className='employee'>
        <Typography variant="h2" align="center" className='employee'>
				Employee Page 
				</Typography>
      {!isLoaded ? <div>Loading...</div> :
          <div className='cardgroups'>
           <CardDeck>
          {data.map((item) => {

            var hireDate = new Date(item.hire_date).toLocaleDateString();
          
            return <Card style={{ width: '18rem' }} className='card'>
                <Card.Header> {item.job} </Card.Header>
                <Card.Body>{item.first_name} {item.last_name}
                </Card.Body>
                
                
                
                

                <Card.Footer>
                  Hire Date: {hireDate}
                </Card.Footer>

             
            </Card>
          })}
        </CardDeck>
        </div>
      }
    </div>
    )
  }

}

export default App