import { useState } from "react";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";

function NavBar({ props }) {
  const [categories, setCategories] = useState(() => {
    let arr = [];
    for (let i = 0; i < props.length; i++) {
      if (!arr.includes(props[i].category)) {
        arr.push(props[i].category);
      }
    }
    return arr;
  });

  return (
    <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand>E-Commerce Site</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/">Home</Nav.Link>
            <NavDropdown title="Products" id="basic-nav-dropdown">
              {categories.map((category, i) => {
                return (
                  <NavDropdown.Item href={`/${category}`} key={i}>
                    {category}
                  </NavDropdown.Item>
                );
              })}
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavBar;
