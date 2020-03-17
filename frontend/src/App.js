import React from "react";
import "bulma/css/bulma.css";
import { GlobalProvider } from "./contexts/GlobalState";

// import { useAuth0 } from "./contexts/auth0-context";
// import Home from "./pages/Home";
import Analyse from "./pages/Analyse";

function App() {
  // const { isLoading, user } = useAuth0();

  return (
    <div>
      {/* {!isLoading && !user && <Home />}
      {!isLoading && user && <Analyse />} */}
      <GlobalProvider>
        <Analyse />
      </GlobalProvider>
    </div>
  );
}

export default App;
