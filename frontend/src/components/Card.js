import React from "react";
import { Container, Card } from "react-bootstrap";

const Cards = props => {
  return (
    <Container>
      <Card>
        <Card.Body>{props.card}</Card.Body>
      </Card>
    </Container>
  );
};

export default Cards;
