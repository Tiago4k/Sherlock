import React from 'react';
import Navbar from './components/Navbar';
import Card from './components/Cards/Cards';
import Typography from '@material-ui/core/Typography';
import './App.css';
import FileUpload from './components/FileUpload';

const App = () => (
  <div>
    <Navbar />
    <div className='container mt-4'>
      <div className='custom-file mb-3' align='center'>
        <Typography variant='h4'>
          {' '}
          <br />
          <br />
          Welcome to Sherlock!
          <br />
          <br />
        </Typography>
      </div>
    </div>
    <div className='container mb-3 h-100'>
      <div className='row h-100 justify-content-center align-items-center'>
        <Card />
      </div>
    </div>
  </div>
);

export default App;
