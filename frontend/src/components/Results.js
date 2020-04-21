import React, { useContext } from "react";
import { Container, Col, Row, Image } from "react-bootstrap";

// component imports
import { GlobalContext } from "../contexts/GlobalState";
import ProgressBar from "./Progressbar/ProgressBar";
// import NotFound from "../assets/NotFound404.png";

function Results() {
  const { results, uploadInfo, elaImage } = useContext(GlobalContext);
  const { prediction, confidence } = results;
  const { file } = uploadInfo;

  let textColor = "";
  let strokeColor = "";

  let conf = parseFloat(confidence);

  if (conf > 99.0) {
    conf = "99.00";
  }

  if (prediction === "Authentic") {
    textColor = "text-color-authentic";
    strokeColor = "#1db954";
  } else {
    textColor = "text-color-tampered";
    strokeColor = "#cd212a";
  }

  return (
    <React.Fragment>
      <Container>
        <p className="hero-subtitle-analyse">
          <span className={`${textColor}`}> {prediction} </span>
        </p>
      </Container>
      <Row
        style={{
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        {prediction === "Authentic" || prediction === "Tampered" ? (
          <React.Fragment>
            <Col sm md={6} lg={6} xl={5}>
              <ProgressBar
                strokeColor={strokeColor}
                percentage={Math.floor(conf)}
              />
            </Col>
            <Col sm md={6} lg={6} xl={7}>
              <span className="results-text">
                What does this mean?
                {prediction === "Authentic" ? (
                  <p className="text-align-center">
                    Sherlock is {conf}% sure that this image is Authentic. Low
                    likehood of having been tampered with. <br />
                    Sherlock produced this ELA {"(Error Level Analysis)"} image
                    for the prediction.
                  </p>
                ) : prediction === "Tampered" ? (
                  <p className="text-align-center">
                    Sherlock is {conf}% sure that this image has been Tampered.
                    Here is a heatmap that highlights regions in the image that
                    Sherlock focused on while trying to make a prediction.
                  </p>
                ) : null}
              </span>
            </Col>
            <Row className="mt-3">
              <Col style={{ textAlign: "center" }}>
                <React.Fragment>
                  <Image
                    className="images"
                    src={URL.createObjectURL(file)}
                    alt="Your image"
                  />
                  <Row
                    style={{
                      alignSelf: "center",
                      justifyContent: "center",
                      marginTop: "5px",
                    }}
                  >
                    <p style={{ fontSize: "14px" }}>Your Image</p>
                  </Row>
                </React.Fragment>
              </Col>
              <Col style={{ textAlign: "center" }}>
                <React.Fragment>
                  <Image
                    className="images__ela"
                    src={`data:application/octet-stream;base64,${elaImage}`}
                    alt="Our ELA Conversion."
                  />
                  <Row
                    style={{
                      alignSelf: "center",
                      justifyContent: "center",
                      marginTop: "5px",
                    }}
                  >
                    <p style={{ fontSize: "14px" }}>Our ELA Conversion</p>
                  </Row>
                </React.Fragment>
              </Col>
            </Row>
          </React.Fragment>
        ) : (
          <span className="results-text">
            What does this mean?
            <p className="text-align-center">
              Sherlock wasn't able to confidently make a prediction on this
              image therefore no prediction has been.
            </p>
          </span>
        )}
      </Row>
    </React.Fragment>
  );
}

export default Results;
