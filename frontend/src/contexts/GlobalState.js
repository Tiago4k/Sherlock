import React, { createContext, useReducer } from "react";
import AppReducer from "./AppReducer";
// initial state
const initialState = {
  uploaded: false,
  uploadInfo: {
    file: "",
    filename: "Choose File"
  },
  results: { prediction: "", confidence: "" }
};

// create context
export const GlobalContext = createContext(initialState);

// provider component
export const GlobalProvider = ({ children }) => {
  const [state, dispatch] = useReducer(AppReducer, initialState);

  function updateStates(uploaded, prediction, confidence, file, filename) {
    dispatch({
      type: "UPDATE_STATES",
      payload: { uploaded, prediction, confidence, file, filename }
    });
  }
  return (
    <GlobalContext.Provider
      value={{
        results: state.results,
        uploaded: state.uploaded,
        uploadInfo: state.uploadInfo,
        updateStates
      }}
    >
      {children}
    </GlobalContext.Provider>
  );
};
