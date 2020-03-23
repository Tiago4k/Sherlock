import React from "react";

// component imports
import Hero from "../components/Hero";
import Navbar from "../components/Navigation";
import Footer from "../components/Footer";

function Home() {
  return (
    <React.Fragment>
      <Navbar />
      <Hero />
      <Footer />
    </React.Fragment>
  );
}

export default Home;
