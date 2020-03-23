import React from "react";
import loading from "../../assets/loading.svg";

function Loading(props) {
  return (
    <div {...props}>
      <img src={loading} alt="Loading" />
    </div>
  );
}

export default Loading;
