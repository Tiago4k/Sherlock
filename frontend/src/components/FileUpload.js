/* eslint-disable jsx-a11y/anchor-is-valid */
import React, { useContext, useState } from "react";
import { Container, Form, Row } from "react-bootstrap";
import { Button, Icon, Label } from "semantic-ui-react";
import axios from "axios";

// context imports
import { GlobalContext } from "../contexts/GlobalState";
import { useAuth0 } from "../contexts/auth0-context";

// component imports
import LoadingResults from "./Loading/LoadingResults";

import "bulma/css/bulma.css";

const url = process.env.REACT_APP_API_URL;

const Input = props => (
  <input
    className="file-input"
    type="file"
    accept=".png, .jpg, .jpeg, .tif, .bmp"
    id="customFile"
    {...props}
  />
);

function FileUpload() {
  const { uploaded, updateStates } = useContext(GlobalContext);
  const { user } = useAuth0();

  const [file, setFile] = useState("");
  const [filename, setFilename] = useState("Choose File");
  const [showLoading, setShowLoading] = useState(false);

  let email = "testing_email@test.com";

  if (user) {
    email = user.email;
  }

  const onChange = e => {
    setFile(e.target.files[0]);
    setFilename(e.target.files[0].name);
  };

  const submitForm = async e => {
    e.preventDefault();
    try {
      // Send converted img to uploadToServer
      await fileToBase64(filename, file).then(result => {
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
    setShowLoading(true);
    const payload = {
      file: imgFile,
      email: email
    };

    const options = {
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "application/json",
        "Access-Control-Allow-Methods": "GET, POST"
      }
    };

    try {
      const response = await axios.post(url, payload, options);

      const prediction = response.data.prediction;
      const confidence = response.data.confidence;
      setShowLoading(false);
      console.log("File Successfully Uploaded!");
      // calls updateStates() from GlobalContext to update results
      updateStates(true, prediction, confidence, file, filename);
    } catch (err) {
      setShowLoading(false);
      if (err.response.status === 400) {
        console.log("No File Uploaded!");
      } else if (err.response.status === 500) {
        console.log("There seems to be an issue with the server.");
      } else {
        console.log("Unexpected error occurred.");
      }
    }
  };
  const Clear = () => {
    setFile("");
    setFilename("Choose File");
  };

  if (showLoading) {
    return <LoadingResults />;
  }

  return (
    <React.Fragment>
      {!uploaded ? (
        <React.Fragment>
          <Container>
            <p className="hero-subtitle-analyse">
              Upload an image to check for forgery.
              <br />
              Receive a<span className="text-color-main"> prediction </span>in
              seconds!
            </p>
          </Container>
          <Form onSubmit={submitForm}>
            <Container>
              <Row className="justify-content-center">
                <label>
                  <Input onChange={onChange} />
                  <Icon size="massive" name="cloud upload" />
                  {!file && (
                    <Row className="justify-content-center mt-3">
                      <Label size="huge" pointing>
                        Choose a file
                      </Label>
                    </Row>
                  )}
                </label>
              </Row>
            </Container>
            {filename !== "Choose File" ? (
              <React.Fragment>
                <Row className="justify-content-center align-items-center mt-4">
                  <span className="filename" htmlFor="customFile">
                    {filename}
                  </span>
                  <span onClick={() => Clear()}>
                    <Icon color="red" name="close" />
                  </span>
                </Row>
                <Row className="justify-content-center mt-5">
                  <Button basic color="blue" size="massive" animated>
                    <Button.Content type="submit" visible>
                      Start
                    </Button.Content>
                    <Button.Content hidden>
                      <Icon name="arrow right" />
                    </Button.Content>
                  </Button>
                </Row>
              </React.Fragment>
            ) : null}
          </Form>
        </React.Fragment>
      ) : null}
    </React.Fragment>
  );
}

export default FileUpload;
