import React, { Fragment, useState } from 'react';

const url = 'http://localhost:8080/';

const FileUpload = () => {
  const [file, setFile] = useState('');
  const [filename, setFilename] = useState('Choose File');
  const [uploadedFile, setUploadedFile] = useState({});
  const [results, setResults] = useState({});

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

      setResults({ prediction, confidence });
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
          <div className='col-md-6 m-auto'>
            <h3 className='text-center'>{''}</h3>
            <img style={{ width: '100%' }} src={''} alt='' />
          </div>
        </div>
      ) : null}
    </Fragment>
  );
};

export default FileUpload;
