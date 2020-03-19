import React from 'react';
import { Router, Route, Switch } from 'react-router-dom';
import { GlobalProvider } from './contexts/GlobalState';
import { useAuth0 } from './contexts/auth0-context';

import history from './utils/history';
import PrivateRoute from './components/PrivateRoute';
import Home from './pages/Home';
import Analyse from './pages/Analyse';
import Loading from './components/Loading';
import Navbar from './components/Navigation';

// styles
import 'bulma/css/bulma.css';

function App() {
  const { loading } = useAuth0();

  if (loading) {
    return <Loading />;
  }

  return (
    <div>
      <GlobalProvider>
        <Navbar />
        <Router history={history}>
          <Switch>
            <Route exact path='/' component={Home} />
            <PrivateRoute path='/analyse' component={Analyse} />
          </Switch>
        </Router>
        {/* <Analyse /> */}
      </GlobalProvider>
    </div>
  );
}

export default App;
