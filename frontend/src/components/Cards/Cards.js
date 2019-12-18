import React, { Component } from 'react';
import Card from './CardUI';
import { Fragment } from 'react';
import FileUpload from '../../components/FileUpload';

class Cards extends Component {
  render() {
    return (
      <Fragment>
        <div className='col-md-4'>
          <Card card={<FileUpload />} />
        </div>
      </Fragment>
    );
  }
}

export default Cards;
