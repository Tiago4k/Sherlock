import styled from "styled-components";
import { string, number } from "prop-types";

import ProgressBarBase from "./ProgressBarBase";

const ProgressBar = styled(ProgressBarBase)`
  width: ${props => props.size};
  text-align: center;
  vertical-align: center;
  .chart-text {
    fill: ${props => props.textColor};
    transform: translateY(0.25em);
  }
  .chart-number {
    font-size: 0.6em;
    line-height: 1;
    text-anchor: middle;
    transform: translateY(-0.25em);
  }
  .chart-label {
    font-size: 0.3em;
    text-transform: uppercase;
    text-anchor: middle;
    transform: translateY(0.7em);
  }
  .figure-key [class*="shape-"] {
    margin-right: 8px;
  }
  .figure-key-list {
    list-style: none;
    display: flex;
    justify-content: space-between;
  }
  .figure-key-list li {
    margin: 5px auto;
  }
  .shape-circle {
    display: inline-block;
    vertical-align: middle;
    width: 21px;
    height: 21px;
    background-color: ${props => props.strokeColor};
    text-transform: capitalize;
  }
`;

ProgressBar.propTypes = {
  textColor: string,
  strokeColor: string,
  size: string,
  percentage: number
};

ProgressBar.defaultProps = {
  textColor: "#54535a",
  strokeColor: "#ffb347",
  size: "70%"
};

export default ProgressBar;
