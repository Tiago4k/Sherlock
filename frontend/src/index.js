import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { Auth0Provider } from './contexts/auth0-context';
import config from './auth_config.json';
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
    domain={config.domain}
    client_id={config.clientId}
    redirect_uri={window.location.origin}
    onRedirectCallback={onRedirectCallback}
  >
    <App />
  </Auth0Provider>,
  document.getElementById('root')
);
