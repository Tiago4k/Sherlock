import React from 'react';
import Navbar from '../components/Header/Nav';
import Card from '../components/Cards/Cards';
import { Router, Route, Switch } from 'react-router-dom';
import Profile from '../components/Profile';
import history from '../utils/history';
import PrivateRoute from '../components/PrivateRoute';

import '../style/App.css';
import Typography from '@material-ui/core/Typography';

function Analyse() {
  return (
    <div>
      <Router history={history}>
        <header>
          <Navbar />
        </header>
        <Switch>
          <Route path='/' exact />
          <PrivateRoute path='/profile' component={Profile} />
        </Switch>
      </Router>
      <div className='container mt-4'>
        <div className='custom-file mb-3' align='center'>
          <Typography variant='h4'>
            {' '}
            <br />
            <br />
            Welcome to Sherlock!
            <br />
            <br />
          </Typography>
        </div>
      </div>
      <div className='container mb-3 h-100'>
        <div className='row h-100 justify-content-center align-items-center'>
          <Card />
        </div>
      </div>
    </div>
  );
}

export default Analyse;
