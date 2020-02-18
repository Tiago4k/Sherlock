import React from 'react';

const Card = props => {
  return (
    <div className='card text-center'>
      <div className='card-body'>{props.card}</div>
    </div>
  );
};

export default Card;
