import React, { useEffect, useState } from "react";
import { Container, Col, Row } from "react-bootstrap";
import Fade from "react-reveal/Fade";

import KainosLogo from "../assets/kainos_logo.png";
import QueensLogo from "../assets/Queens_logo.jpg";

function About() {
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
    <section id="about">
      <Container>
        <span>What is Sherlock?</span>
        <Row className="about-wrapper mt-5">
          <Col md={6} sm={12}>
            <Fade
              left={isDesktop}
              bottom={isMobile}
              duration={1000}
              delay={1000}
              distance="30px"
            >
              <div className="about-wrapper__info">
                <p className="about-wrapper__info-text">
                  Sherlock is an AI detective.
                  <br />
                  Sherlock detects forgery in images by utilising Deep Neural
                  Networks and Error Level Analysis to provide a prediction on
                  whether an image have been tampered with or not. <br />
                  Simply upload an image and receive a prediction in seconds.
                </p>
                <p className="about-wrapper__info-text">
                  This project have been developed in collaboration with Kainos
                  and Queen's University Belfast.
                </p>
              </div>
            </Fade>
          </Col>
          <Col md={6} sm={12}>
            <Fade bottom duration={1000} delay={600} distance="30px">
              <Row className="align-self-center justify-content-center mt-5">
                <div className="about-wrapper__image">
                  <img
                    className="colab-logos"
                    src={KainosLogo}
                    alt="Kainos logo."
                  />
                </div>
              </Row>
              <Row className="align-self-center justify-content-center">
                <div className="about-wrapper__image">
                  <img
                    className="colab-logos"
                    src={QueensLogo}
                    alt="Queen's Univerity Belfast logo."
                  />
                </div>
              </Row>
            </Fade>
          </Col>
        </Row>
      </Container>
    </section>
  );
}

export default About;
