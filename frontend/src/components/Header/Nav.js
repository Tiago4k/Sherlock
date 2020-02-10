import React from 'react';
import Navbar from 'react-bootstrap/Navbar';

function Nav() {
  return (
    <Navbar>
      <Navbar.Brand href='/'>Sherlock</Navbar.Brand>
      <Navbar.Toggle />
      <Navbar.Collapse className='justify-content-end'>
        <Navbar.Text>
          Signed in as: <a href='/'>Test</a>
        </Navbar.Text>
      </Navbar.Collapse>
    </Navbar>
  );
}

export default Nav;
