import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import {Link, NavLink} from "react-router-dom";

export default function BookShopNav() {
    return(
        <Navbar expand="lg" className="bg-body-tertiary">
            <Container>
                <Navbar.Brand href="/">Books Shop</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Link><NavLink to={"/home"}>Home</NavLink></Nav.Link>
                        <Nav.Link><NavLink to={"/placeholder"}>1</NavLink></Nav.Link>
                        <Nav.Link><NavLink to={"/placeholder"}>2</NavLink></Nav.Link>
                        <Nav.Link><NavLink to={"/placeholder"}>3</NavLink></Nav.Link>
                        <Nav.Link><NavLink to={"/placeholder"}>4</NavLink></Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    )
}