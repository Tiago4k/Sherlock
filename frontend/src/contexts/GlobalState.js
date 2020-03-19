import React, { createContext, useReducer } from "react";
import AppReducer from "./AppReducer";
// initial state
const initialState = {
  uploaded: false,
  results: [{ prediction: "", confidence: " " }]
};

// create context
export const GlobalContext = createContext(initialState);

// provider component
export const GlobalProvider = ({ children }) => {
  const [state, dispatch] = useReducer(AppReducer, initialState);

  function updateStates(uploaded, prediction, confidence) {
    dispatch({
      type: "UPDATE_STATES",
      payload: { uploaded, prediction, confidence }
    });
  }
  return (
    <GlobalContext.Provider
      value={{
        results: [state.prediction, state.confidence],
        uploaded: state.uploaded,
        updateStates
      }}
    >
      {children}
    </GlobalContext.Provider>
  );
};
