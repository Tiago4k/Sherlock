/* eslint-disable jsx-a11y/anchor-is-valid */
import React from "react";
import { Navbar, Container } from "react-bootstrap";
import { Button, Icon } from "semantic-ui-react";

// context imports
import { useAuth0 } from "../contexts/auth0-context";

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
    <Navbar expand="lg" sticky="top">
      <Container>
        <Navbar.Brand className="text-color-main">Sherlock</Navbar.Brand>
        <Navbar.Toggle />
        <Navbar.Collapse className="justify-content-end">
          {!isLoading && user && (
            <>
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
            </>
          )}
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Navigation;
