import React from 'react';


const Card = props => {
  return (
  <div class="card text-center">
    <div class="card-body">
      {props.card}
    </div>
  </div>
  );
};


export default Card;
