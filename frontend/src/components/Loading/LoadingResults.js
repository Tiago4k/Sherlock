import React, { Fragment } from "react";
import { Container, Row } from "react-bootstrap";
import Loading from "./Loading";

export default function LoadingResults() {
  return (
    <Fragment>
      <Container>
        <Row className="align-self-center justify-content-sm-center">
          <p className="hero-subtitle-analyse">
            Sherlock is analysing your image...
          </p>
        </Row>
        <Loading className={"spinner--container"} />
      </Container>
    </Fragment>
  );
}
