import React from 'react';
import FileUpload from './components/FileUpload';
import Navbar from './components/Navbar';
import Typography from '@material-ui/core/Typography';
import './App.css';

const App = () => (
  <div>
    <Navbar />
    <div className='container mt-4'>
      <div className='custom-file mb-3' align='center'>
        <Typography variant='h6'> Welcome to Sherlock!</Typography>
      </div>
      <Typography variant='body2'>
        <FileUpload />
      </Typography>
    </div>
  </div>
);

export default App;
