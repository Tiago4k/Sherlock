import React from 'react';
import { Container } from 'react-bootstrap';

function Footer() {
  return (
    <footer className='footer navbar-static-bottom'>
      <Container>
        <a href='#top' aria-label='Back To Top' className='back-to-top'>
          <i className='fa fa-angle-up fa-2x' aria-hidden='true' />
        </a>
        <hr />
        <p className='footer__text'>
          © {new Date().getFullYear()} - Created by Tiago Ramalho
        </p>
        <p className='footer__text'>
          Theme by{' '}
          <a href='https://www.gatsbyjs.org/starters/cobidev/gatsby-simplefolio/'>
            cobidev
          </a>
        </p>
      </Container>
    </footer>
  );
}

export default Footer;
