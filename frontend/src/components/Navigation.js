/* eslint-disable jsx-a11y/anchor-is-valid */
import React from "react";
import { Navbar, Container } from "react-bootstrap";
import { useAuth0 } from "../contexts/auth0-context";

function Navigation() {
  const { isLoading, user, logout } = useAuth0();

  return (
    <Navbar expand="lg" sticky="top">
      <Container>
        <Navbar.Brand className="text-color-main">Sherlock</Navbar.Brand>
        <Navbar.Toggle />
        <Navbar.Collapse className="justify-content-end">
          {!isLoading && user && (
            <>
              <span className="greeting">Hi {user.given_name}!</span>

              <a
                className="cta-btn cta-btn--hero"
                onClick={() => logout({ returnTo: window.location.origin })}
              >
                Logout
              </a>
            </>
          )}
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Navigation;
