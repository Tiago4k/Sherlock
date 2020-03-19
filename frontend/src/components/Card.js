import React from "react";
import Card from "react-bootstrap/Card";

const Cards = props => {
  return (
    <Card>
      <Card.Body>{props.card}</Card.Body>
    </Card>
  );
};

export default Cards;
