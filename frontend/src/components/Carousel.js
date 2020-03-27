import React, { useState, useEffect } from "react";
import { Container, Col, Row } from "react-bootstrap";
import Slider from "react-slick";

// context imports
import { useAuth0 } from "../contexts/auth0-context";

const url = process.env.REACT_APP_API_URL;

export default function Carousel() {
  const [userUploads, setUserUploads] = useState([]);
  const [isEmpty, setIsEmpty] = useState(false);
  const { user } = useAuth0();
  const email = encodeURIComponent(user.email);

  useEffect(() => {
    fetch(url + "/user/" + email)
      .then(res => res.json())
      .then(data => {
        if (data.uploads.length !== 0) {
          setUserUploads(data.uploads);
          setIsEmpty(false);
        } else {
          throw new Error("No Previous Uploads");
        }
      })
      .catch(error => setIsEmpty(true));

    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  let settings = {
    infinite: false,
    dots: true,
    speed: 1000,
    arrows: true,
    slidesToShow: 1,
    slidesToScroll: 1
  };
  return (
    <React.Fragment>
      <Container>
        <Row className="align-items-center justify-content-center">
          <h1 className="text-muted" style={{ paddingBottom: "2vh" }}>
            Previous Uploads
          </h1>
        </Row>
        <Row className="align-items-center justify-content-center">
          {!isEmpty ? (
            <React.Fragment>
              {userUploads.length === 0 ? (
                <div className="spinner-border" role="status">
                  <span className="sr-only">Loading...</span>
                </div>
              ) : (
                <Col xl={3} lg={3} md={3}>
                  <Slider {...settings}>
                    {userUploads.map(({ uuid, image, prediction }) => (
                      <div className="out" key={uuid}>
                        <div className="card">
                          <img
                            className="carousel-img"
                            alt=""
                            src={`data:application/octet-stream;base64,${image}`}
                          />
                          <div className="card-body">
                            <p className="card-title">Prediction</p>
                            {prediction === "Authentic" ? (
                              <p
                                className="card-text"
                                style={{ color: "#1db954" }}
                              >
                                {prediction}
                              </p>
                            ) : (
                              <p
                                className="card-text"
                                style={{ color: "#cd212a" }}
                              >
                                {prediction}
                              </p>
                            )}
                          </div>
                        </div>
                      </div>
                    ))}
                  </Slider>
                </Col>
              )}
            </React.Fragment>
          ) : (
            <div className="card" style={{ justifyContent: "center" }}>
              <p className="card-no-uploads">No Previous Uploads</p>
            </div>
          )}
        </Row>
      </Container>
    </React.Fragment>
  );
}
