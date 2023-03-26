// External Imports
import React from "react";
import { fireEvent, render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import { ChakraProvider } from "@chakra-ui/react";

// Internal Imports
import Navbar from "../components/navbar";
import theme from "../theme";

describe("Navbar Smoke Tests", () => {
  it("renders the Navbar Title", () => {
    render(<Navbar />);
    const title = screen.getByText("Noam");
    expect(title).toBeInTheDocument();
  });

  it("renders the Navbar Blog Link", () => {
    render(<Navbar />);
    const icon = screen.getByTestId("chat-icon");
    const link = screen.getByText("What is this?");
    expect(icon).toBeInTheDocument();
    expect(link).toBeInTheDocument();
  });

  it("renders the Navbar Github Link", () => {
    render(<Navbar />);
    const icon = screen.getByTestId("code-icon");
    const link = screen.getByText("Source Code");
    expect(icon).toBeInTheDocument();
    expect(link).toBeInTheDocument();
  });

  it("renders the theme toggle button", () => {
    render(<Navbar />);
    const button = screen.getByTestId("theme-button");
    expect(button).toBeInTheDocument();
  });
});

describe("Navbar Intractability", () => {
  it("toggle the theme using the dark-light button", () => {
    render(
      <ChakraProvider theme={theme}>
        <Navbar />
      </ChakraProvider>
    );
    const button = screen.getByTestId("theme-button");
    const darkButton = screen.getByTestId("dark-button");
    expect(darkButton).toBeInTheDocument();
    fireEvent.click(button);
    const lightButton = screen.getByTestId("light-button");
    expect(lightButton).toBeInTheDocument();
  });
});
