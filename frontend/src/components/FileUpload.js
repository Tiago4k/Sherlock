/* eslint-disable jsx-a11y/anchor-is-valid */
import React, { useState, useContext } from "react";
import { Container, Form, Row } from "react-bootstrap";
import { GlobalContext } from "../contexts/GlobalState";
import { useAuth0 } from "../contexts/auth0-context";

import axios from "axios";
import Message from "./Message";
import Progress from "./Progress";
import "bulma/css/bulma.css";

const url = "https://router-api-rxt3flnjda-ez.a.run.app";

const Input = props => (
  <input
    className="file-input"
    type="file"
    accept=".png, .jpg, .jpeg, .tif, .bmp"
    id="customFile"
    {...props}
  />
);

const FileUpload = () => {
  const { uploaded, updateStates } = useContext(GlobalContext);

  const [file, setFile] = useState("");
  const [filename, setFilename] = useState("Choose File");
  const [imgBits, setImgBits] = useState("");
  const [message, setMessage] = useState("");
  const [uploadPrecentage, setUploadPrecentage] = useState(0);

  const onChange = e => {
    setFile(e.target.files[0]);
    setFilename(e.target.files[0].name);
  };

  const submitForm = async e => {
    e.preventDefault();

    try {
      // Send converted img to uploadToServer
      await fileToBase64(filename, file).then(result => {
        setImgBits(result);
        uploadToServer(result);
      });
    } catch (err) {
      console.log(err);
    }
  };

  const fileToBase64 = (fname, filepath) => {
    return new Promise(resolve => {
      let tempFile = new File([filepath], fname);
      let reader = new FileReader();
      // Read file content on file loaded event
      reader.onload = function(event) {
        resolve(event.target.result);
      };

      // Convert data to base64
      reader.readAsDataURL(tempFile);
    });
  };

  const uploadToServer = async imgFile => {
    const formData = new FormData();
    formData.append("file", imgFile);

    try {
      const response = await axios.post(
        url,
        { file: imgFile },
        {
          headers: {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json",
            "Access-Control-Allow-Methods": "GET, POST"
          }
        },
        {
          onUploadProgress: progressEvent => {
            setUploadPrecentage(
              parseInt(
                Math.round((progressEvent.loaded / progressEvent.total) * 100)
              )
            );
            setTimeout(() => setUploadPrecentage(0), 10000);
          }
        }
      );

      const prediction = response.data.prediction;
      const confidence = response.data.confidence;

      setMessage("File Successfully Uploaded!");

      // calls updateStates() from GlobalContext to update results
      updateStates(true, prediction, confidence);
    } catch (err) {
      if (err.response.status === 400) {
        setMessage("No File Uploaded!");
      } else if (err.response.status === 500) {
        setMessage("There seems to be an issue with the server.");
      }
    }
  };

  const clearImage = e => {
    setFile(null);
    setFilename(null);
  };

  return (
    <>
      {!uploaded ? (
        <Container fluid>
          {message ? <Message msg={message} /> : null}
          <Form onSubmit={submitForm}>
            <Row className="justify-content-md-center">
              <div className="file is-centered is-boxed is-large">
                <label className="file-label">
                  <Input onChange={onChange} />
                  <span className="file-cta">
                    <span className="file-icon">
                      <i className="fas fa-upload"></i>
                    </span>
                    <span className="file-label">Choose a file…</span>
                  </span>
                </label>
              </div>
            </Row>
            {filename !== "Choose File" ? (
              <>
                <Row className="justify-content-md-center mt-3">
                  <label style={{ fontSize: 18 }} htmlFor="customFile">
                    {filename}
                  </label>
                </Row>
                <Row>
                  <Progress precentage={uploadPrecentage} />
                </Row>
              </>
            ) : null}
            <Row className="justify-content-md-center mt-3">
              <button type="submit" className="button is-large is-fullwidth">
                Submit
              </button>
            </Row>
          </Form>
        </Container>
      ) : (
        <Container fluid>
          <Row className="justify-content-md-center mt-3">
            <img style={{ width: "100%" }} src={imgBits} alt="" />
          </Row>
          <Row className="justify-content-md-center mt-3">
            <p style={{ fontSize: 18 }} htmlFor="customFile">
              {filename}
            </p>
          </Row>
          <Row className="justify-content-md-center mt-3">
            <Form onSubmit={clearImage}>
              {" "}
              <button type="submit" className="button is-large is-fullwidth">
                Clear
              </button>
            </Form>
          </Row>
        </Container>
      )}
    </>
  );
};

export default FileUpload;
