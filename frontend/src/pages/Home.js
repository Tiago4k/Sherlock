import React from "react";

// component imports
import Hero from "../components/Hero";
import About from "../components/About";
import Navbar from "../components/Navigation";
import Footer from "../components/Footer";

function Home() {
  return (
    <React.Fragment>
      <Navbar />
      <Hero />
      <About />
      <Footer />
    </React.Fragment>
  );
}

export default Home;
