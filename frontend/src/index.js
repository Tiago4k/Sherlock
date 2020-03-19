import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { Auth0Provider } from './contexts/auth0-context';
import history from './utils/history';

import './style/main.scss';
import 'bootstrap/dist/css/bootstrap.min.css';

// A function that routes the user to the right place
// after login
const onRedirectCallback = appState => {
  history.push(
    appState && appState.targetUrl
      ? appState.targetUrl
      : window.location.pathname
  );
};


ReactDOM.render(
  <Auth0Provider
    domain={process.env.REACT_APP_AUTH_DOMAIN}
    client_id={process.env.REACT_APP_AUTH_CLIENT_ID}
    redirect_uri={window.location.origin}
    onRedirectCallback={onRedirectCallback}
  >
    <App />
  </Auth0Provider>,
  document.getElementById('root')
);
