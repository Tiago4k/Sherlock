/* eslint-disable jsx-a11y/anchor-is-valid */
import React, { useState, useEffect, useContext } from "react";
import { Container, Row, Form } from "react-bootstrap";
import { Button, Icon } from "semantic-ui-react";
import Fade from "react-reveal/Fade";

// context imports
// import { useAuth0 } from "../contexts/auth0-context";
import { GlobalContext } from "../contexts/GlobalState";

// component imports
import Navbar from "../components/Navigation";
import Footer from "../components/Footer";
import FileUpload from "../components/FileUpload";
import Results from "../components/Results";

function Analyse() {
  const [isDesktop, setIsDesktop] = useState(false);
  const [isMobile, setIsMobile] = useState(false);

  // Global contexts
  const { uploaded } = useContext(GlobalContext);
  // const { user } = useAuth0();

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
    <React.Fragment>
      <Navbar />
      <section id="hero" className="jumbotron">
        <Container>
          <Fade
            top={(isDesktop, isMobile)}
            duration={500}
            delay={100}
            distance="100px"
          >
            {uploaded ? (
              <React.Fragment>
                <Row style={{ alignSelf: "center", justifyContent: "center" }}>
                  <p className="hero-subtitle-analyse">
                    Analysis Completed.
                    <br />
                    Here are your results.
                  </p>
                </Row>
                <Row style={{ alignSelf: "center", justifyContent: "center" }}>
                  <Results />
                </Row>
                <Row
                  style={{
                    alignSelf: "center",
                    justifyContent: "center",
                    marginTop: "50px"
                  }}
                >
                  <Form>
                    {" "}
                    <Button basic color="blue" size="massive" animated>
                      <Button.Content type="submit" visible>
                        Clear Results
                      </Button.Content>
                      <Button.Content hidden>
                        <Icon name="remove" />
                      </Button.Content>
                    </Button>
                  </Form>
                </Row>
              </React.Fragment>
            ) : (
              <React.Fragment>
                <Container>
                  <FileUpload />
                </Container>
              </React.Fragment>
            )}
          </Fade>
        </Container>
      </section>
      <Footer />
    </React.Fragment>
  );
}

export default Analyse;
