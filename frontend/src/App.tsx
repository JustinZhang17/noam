import * as React from "react";
import Navbar from "./components/navbar";
import Form from "./components/form";
import Promo from "./components/promo";

const App = () => {
  return (
    <>
      <Promo />
      <Navbar />
      <Form />
    </>
  );
};

export default App;
