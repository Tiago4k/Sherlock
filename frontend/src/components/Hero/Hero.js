import React, { useState, useEffect } from 'react';
import { Container } from 'react-bootstrap';
import Fade from 'react-reveal/Fade';
import { Link } from 'react-router-dom';

function Hero() {
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
    <section id='hero' className='jumbotron'>
      <Container>
        <Fade
          left={isDesktop}
          bottom={isMobile}
          duration={1000}
          delay={500}
          distance='30px'
        >
          <h1 className='hero-title'>
            Meet
            <span className='text-color-main'> Sherlock</span>.
            <br /> The clever
            <span className='text-color-main'> Machine Learning</span>{' '}
            detective.
          </h1>
        </Fade>
        <Fade
          left={isDesktop}
          bottom={isMobile}
          duration={1000}
          delay={1000}
          distance='30px'
        >
          <Container>
            <div className='row'>
              <div className='hero-cta flex-center'>
                <a className='cta-btn cta-btn--hero' href='#about'>
                  Learn More
                </a>
                <Link className='cta-btn cta-btn--hero' to='/Analyse'>
                  Get Started
                </Link>
              </div>
            </div>
          </Container>
        </Fade>
      </Container>
    </section>
  );
}

export default Hero;
