import React from "react";
import { Router, Route, Switch } from "react-router-dom";
import history from "./utils/history";

// context imports
import { GlobalProvider } from "./contexts/GlobalState";
import { useAuth0 } from "./contexts/auth0-context";

// component imports
import PrivateRoute from "./components/PrivateRoute";
import Loading from "./components/Loading/Loading";

// pages
import Home from "./pages/Home";
import Analyse from "./pages/Analyse";
import NotFound from "./pages/NotFound";

// styles
import "bulma/css/bulma.css";

function App() {
  const { loading } = useAuth0();

  if (loading) {
    return <Loading className={"spinner"} />;
  }

  return (
    <div>
      <GlobalProvider>
        <Router history={history}>
          <Switch>
            <Route exact path="/" component={Home} />
            <PrivateRoute path="/analyse" component={Analyse} />
            <Route path="*" component={NotFound} />
          </Switch>
        </Router>
      </GlobalProvider>
    </div>
  );
}

export default App;
