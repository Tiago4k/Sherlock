import React from 'react';
import Home from './pages/Home';
import Analyse from './pages/Analyse';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

// import Profile from './components/Profile';
// import history from './utils/history';
// import PrivateRoute from './components/PrivateRoute';

function App() {
  return (
    <main>
      <Router>
        <Switch>
          <Route path='/' component={Home} exact />
          <Route path='/Analyse' component={Analyse} />
        </Switch>
      </Router>
    </main>
  );
}

export default App;
