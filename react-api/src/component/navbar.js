import { Link } from 'react-router-dom';
import logo from '../media/img/logo.png';
import '../css/navbar.css';


const Navbar = () => 
{
	return (
        <div><div className='logo'>Umbrella Corporation <img src={logo} width='50'/> </div>
    <nav className="navbar">   
            <div className="links">
                <Link to="/" >Home</Link>
                <Link to="/employee">Employees</Link>
                <Link to="/department">Departments</Link>
                <Link to="/history">History</Link>
            </div>
        </nav>
        </div>
    );
};

export default Navbar