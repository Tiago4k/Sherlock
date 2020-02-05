import React, { Fragment, useState } from 'react';
import axios from 'axios';
import Message from './Message/Message';
import Progress from './Progress';
import Container from 'react-bootstrap/Container';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';

const url = 'http://localhost:8080/';

const FileUpload = () => {
  const [file, setFile] = useState('');
  const [filename, setFilename] = useState('Choose File');
  const [results, setResults] = useState({});
  const [uploadedFile, setUploadedFile] = useState({});
  const [message, setMessage] = useState('');
  const [uploadPrecentage, setUploadPrecentage] = useState(0);

  const onChange = e => {
    setFile(e.target.files[0]);
    setFilename(e.target.files[0].name);
  };

  const handleImageUpload = async e => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post(url, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        onUploadProgress: progressEvent => {
          setUploadPrecentage(
            parseInt(
              Math.round((progressEvent.loaded / progressEvent.total) * 100)
            )
          );
          setTimeout(() => setUploadPrecentage(0), 10000);
        }
      });

      const prediction = response.data.Prediction;
      const confidence = response.data.Confidence;
      const encodedImage = response.data.EncodedImage;

      setUploadedFile({ filename, encodedImage });
      setResults({ prediction, confidence });
      setMessage('File Successfully Uploaded!');
    } catch (err) {
      if (err.response.status === 400) {
        setMessage('No File Uploaded!');
      } else if (err.response.status === 500) {
        setMessage('There seems to be an issue with the server.');
      }
    }
  };

  return (
    <Fragment>
      {message ? <Message msg={message} /> : null}
      <form onSubmit={handleImageUpload}>
        <div className='custom-file mb-4'>
          <input
            type='file'
            className='custom-file-input'
            id='customFile'
            onChange={onChange}
          />
          <label className='custom-file-label' htmlFor='customFile'>
            {filename}
          </label>
        </div>
        <Progress precentage={uploadPrecentage} />
        <input
          type='submit'
          value='Upload'
          className='btn btn-primary btn-block mt-4'
        />
      </form>
      {uploadedFile ? (
        <div className='row mt-5'>
          <div className='col-md-8 m-auto'>
            <h3 className='text-center'>{''}</h3>
            <Container md='auto'>
              <Row>
                <Col sm={true}>
                  <p>Prediction: {results.prediction}</p>
                  <p>Confidence: {results.confidence}</p>
                </Col>
                <Col xl={true}>
                  <h4 className='text-center'>{uploadedFile.filename}</h4>
                  <img
                    style={{ width: '100%' }}
                    src={'data:image/jpeg;base64,' + uploadedFile.encodedImage}
                    alt=''
                  />
                </Col>
              </Row>
            </Container>
          </div>
        </div>
      ) : null}
    </Fragment>
  );
};

export default FileUpload;
