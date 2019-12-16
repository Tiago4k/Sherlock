import React, { Fragment, useState } from 'react';
import Container from 'react-bootstrap/Container';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';

const url = 'http://localhost:8080/';

const FileUpload = () => {
  const [file, setFile] = useState('');
  const [filename, setFilename] = useState('Choose File');
  const [results, setResults] = useState({});
  const [uploadedFile, setUploadedFile] = useState({});

  const onChange = e => {
    setFile(e.target.files[0]);
    setFilename(e.target.files[0].name);
  };

  const handleImageUpload = async e => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch(url, {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        throw new Error('Ooops, something went wrong!');
      }

      const data = await response.json();

      const prediction = data['Prediction'];
      const confidence = data['Confidence'];
      const encodedImage = data['EncodedImage'];

      setUploadedFile({ filename, encodedImage });
      setResults({ prediction, confidence });
      console.log(results);
    } catch (error) {
      console.log('Uploading failed:', error.message);
    }
  };

  return (
    <Fragment>
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
        <input
          type='submit'
          value='Upload'
          className='btn btn-primary btn-block mt-4'
        />
      </form>
      {uploadedFile ? (
        <div className='row mt-5'>
          <div className='col-md-8 m-auto'>
            <h3 className='text-center'>{uploadedFile.fileName}</h3>
            <Container md='auto'>
              <Row>
                <Col sm={true}>
                  <p>Prediction: {results.prediction}</p>
                  <p>Confidence: {results.confidence}</p>
                </Col>
                <Col xl={true}>
                  {' '}
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
