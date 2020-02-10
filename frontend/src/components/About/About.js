import React, { useEffect, useState } from 'react';
import Fade from 'react-reveal/Fade';
import Tilt from 'react-tilt';
import { Container, Row, Col } from 'react-bootstrap';
// import Title from '../Title/Title';

import uuidv1 from 'uuid/v1';

const About = () => {
  const [isDesktop, setIsDesktop] = useState(false);
  const [isMobile, setIsMobile] = useState(false);

  useEffect(() => {
    if (window.innerWidth > 769) {
      setIsDesktop(true);
      setIsMobile(false);
    } else {
      setIsMobile(true);
      setIsDesktop(false);
    }
  }, []);

  return (
    <section id='about'>
      <Container>
        <div className='about-wrapper'>
          <Row key={uuidv1}>
            <Col lg={4} sm={12}>
              <Fade
                left={isDesktop}
                bottom={isMobile}
                duration={1000}
                delay={300}
                distance='30px'
              >
                <div className='about-wrapper__text'>
                  <h4 className='about-wrapper__text-title'>
                    {' '}
                    Sherlock can predict whether an image has been manipulated
                    by analysing the difference in compression rates found in a
                    image.
                  </h4>
                  <div></div>
                </div>
              </Fade>
            </Col>
            <Col lg={8} sm={12}>
              <Fade
                right={isDesktop}
                bottom={isMobile}
                duration={1000}
                delay={800}
                distance='30px'
              >
                <div className='about-wrapper__image'>
                  <a
                    href='#!'
                    target='_blank'
                    aria-label='Project Link'
                    rel='noopener noreferrer'
                  >
                    <Tilt
                      options={{
                        reverse: false,
                        max: 8,
                        perspective: 1000,
                        scale: 1,
                        speed: 250,
                        transition: true,
                        axis: null,
                        reset: true,
                        easing: 'cubic-bezier(.03,.98,.52,.99)'
                      }}
                    >
                      <div data-tilt className='thumbnail rounded'>
                        <img
                          alt=''
                          src={require('../../assets/sample_overlay_1.png')}
                        />
                      </div>
                    </Tilt>
                  </a>
                </div>
              </Fade>
            </Col>
          </Row>
        </div>
      </Container>
    </section>
  );
};

export default About;
