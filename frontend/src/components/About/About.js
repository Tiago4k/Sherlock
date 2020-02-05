import React, { useEffect, useState } from 'react';
import Fade from 'react-reveal/Fade';
import Tilt from 'react-tilt';
import { Container, Row, Col } from 'react-bootstrap';
import Title from '../Title/Title';
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
          <Title title='About Me' />

          <Row key={uuidv1}>
            <Col lg={12} sm={12}>
              <Fade
                left={isDesktop}
                bottom={isMobile}
                duration={1000}
                delay={500}
                distance='30px'
              >
                <div className='about-wrapper__text'>
                  <h3 className='about-wrapper__text-title'>What Can I Do?</h3>
                  <div>
                    <p>
                      Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                      Excepturi neque, ipsa animi maiores repellendu
                      distinctioaperiam earum dolor voluptatum consequatur
                      blanditiis inventore debitis fuga numquam voluptate
                      architecto itaque molestiae.
                    </p>
                  </div>
                </div>
              </Fade>
            </Col>
            <Col lg={2} sm={12}>
              <Fade
                right={isDesktop}
                bottom={isMobile}
                duration={1000}
                delay={1000}
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
                        speed: 300,
                        transition: true,
                        axis: null,
                        reset: true,
                        easing: 'cubic-bezier(.03,.98,.52,.99)'
                      }}
                    >
                      {/* <div data-tilt className='thumbnail rounded'>
                        <ProjectImg alt={title} filename={img} />
                      </div> */}
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
