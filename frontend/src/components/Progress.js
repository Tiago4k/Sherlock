import React from 'react';
import PropTypes from 'prop-types';

const Progress = ({ precentage }) => {
  return (
    <div className='progress'>
      <div
        className='progress-bar progress-bar-striped bg-success progress-bar-animated'
        role='progressbar'
        style={{ width: `${precentage}%` }}
      >
        {precentage}%
      </div>
    </div>
  );
};

Progress.propTypes = {
  precentage: PropTypes.number.isRequired
};

export default Progress;
