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
    const response = await fetch('http://127.0.0.1:5000/departments')
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
    <div className='department'>
        <Typography variant="h2" align="center" className='department'>
				Department Page 
				</Typography>
      {!isLoaded ? <div>Loading...</div> :
          <div className='cardgroups'>
           <CardDeck>
          {data.map((item) => {
            
            return <Card style={{ width: '18rem' }} className='card'>
                <Card.Header> {item.dept_name} </Card.Header>

             
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