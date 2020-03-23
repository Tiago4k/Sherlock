import React from "react";
import { Link } from "react-router-dom";
import { Container, Image } from "react-bootstrap";
import NotFound404 from "../assets/NotFound404.png";

const NotFoundPage = () => ({
  render() {
    return (
      <React.Fragment>
        <section id="hero" className="jumbotron">
          <Container>
            <h1 className="hero-subtitle flex-center">
              WHOOPS! SOMETHING HAS GONE WRONG
            </h1>
            <Image className="flex-center" src={NotFound404} />
            <p className="hero-subtitle-analyse flex-center">
              Even Sherlock couldn't find this page!
            </p>
            <div className="hero-cta flex-center">
              <Link to="/" className="cta-btn cta-btn--hero">
                Take Me Home
              </Link>
            </div>
          </Container>
        </section>
      </React.Fragment>
    );
  }
});
export default NotFoundPage;
