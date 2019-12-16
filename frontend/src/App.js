import React from 'react';
import FileUpload from './components/FileUpload';
import { faReact } from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import './App.css';

const App = () => (
  <div className='container mt-4'>
    <h4 className='display-4 text-center mb-4'>
      <FontAwesomeIcon icon={faReact} /> React File Upload
    </h4>
    <FileUpload />
  </div>
);

export default App;
