/* eslint-disable jsx-a11y/anchor-is-valid */
import React, { useState, useEffect, useContext } from "react";
import { Container, Col, Row } from "react-bootstrap";
import Fade from "react-reveal/Fade";

import { useAuth0 } from "../contexts/auth0-context";
import { GlobalContext } from "../contexts/GlobalState";

import Navbar from "../components/Navigation";
import Footer from "../components/Footer";
import Card from "../components/Card";
import FileUpload from "../components/FileUpload";

function Analyse() {
  // Global contexts
  const { user } = useAuth0();
  const { results, uploaded } = useContext(GlobalContext);

  const [isDesktop, setIsDesktop] = useState(false);
  const [isMobile, setIsMobile] = useState(false);

  useEffect(() => {
    if (window.innerWidth > 769) {
      setIsDesktop(true);
      setIsMobile(false);
    } else {
      setIsMobile(true);
      setIsDesktop(false);
    }
  }, []);

  return (
    <>
      <Navbar />
      <section id="hero">
        <Container className="align-self-center">
          <Row className="about-wrapper">
            <Col sm={8}>
              <Container>
                <Fade
                  left={isDesktop}
                  bottom={isMobile}
                  duration={1000}
                  delay={500}
                  distance="100px"
                >
                  {uploaded ? (
                    <Col>
                      <div className="about-wrapper__info">
                        <p className="about-wrapper__info-text">
                          {" "}
                          Image Uploaded!
                        </p>
                      </div>
                    </Col>
                  ) : (
                    <Col>
                      <div className="about-wrapper__info">
                        <p className="about-wrapper__info-text">
                          {" "}
                          Upload an image to check for forgery.
                        </p>
                        {/* <br /> */}
                        <p className="about-wrapper__info-text text-color-main">
                          {" "}
                          Receive a prediction in seconds!
                        </p>{" "}
                      </div>
                    </Col>
                  )}
                </Fade>
              </Container>
            </Col>
            <Col sm={4}>
              <Container>
                <Card card={<FileUpload />} />
              </Container>
            </Col>
          </Row>
        </Container>
      </section>
      <Footer />
    </>
  );
}

export default Analyse;
