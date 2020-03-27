/* eslint-disable jsx-a11y/anchor-is-valid */
import React from "react";
import { Nav, Navbar, Container } from "react-bootstrap";
import { Link } from "react-router-dom";
import { Button, Icon } from "semantic-ui-react";

// context imports
import { useAuth0 } from "../contexts/auth0-context";

import Logo from "../assets/Sherlock_logo.svg";
import "bulma/css/bulma.css";

function Navigation() {
  const { isLoading, user, logout } = useAuth0();

  let username = "";
  if (user) {
    if (user.given_name) {
      username = user.given_name;
    } else {
      username = user.nickname;
    }
  }

  return (
    <Navbar collapseOnSelect expand="lg" sticky="top">
      <Container>
        <Navbar.Brand>
          <Link to="/">
            <img src={Logo} className="logo" alt="Sherlock logo" />
          </Link>
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse className="justify-content-end">
          <Nav>
            {!isLoading && user && (
              <React.Fragment>
                <span className="greeting">Hi {username}!</span>
                <Button
                  color="yellow"
                  size="huge"
                  animated
                  onClick={() => logout({ returnTo: window.location.origin })}
                >
                  <Button.Content type="submit" visible>
                    Logout
                  </Button.Content>
                  <Button.Content hidden>
                    <Icon name="sign-out" />
                  </Button.Content>
                </Button>
              </React.Fragment>
            )}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Navigation;
