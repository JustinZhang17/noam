import React from "react";
import { screen, render, fireEvent, waitFor } from "@testing-library/react";
import "@testing-library/jest-dom";

// Internal Imports
import Form from "../components/form";

describe("Form Smoke Tests", () => {
  beforeEach(() => {
    render(<Form />);
  });

  it("renders WordList Length Input", () => {
    const text = screen.getByText("Wordlist Length");
    const input = screen.getByDisplayValue("200");
    const helperText = screen.getByText("Max 600 Words.");

    expect(text).toBeInTheDocument();
    expect(input).toBeInTheDocument();
    expect(helperText).toBeInTheDocument();
  });

  it("renders Api Key Input", () => {
    const text = screen.getByText("Api Key");
    const input = screen.getByPlaceholderText("Enter your Api Key");
    const helperText = screen.getByText("Don't share this with anyone.");

    expect(text).toBeInTheDocument();
    expect(input).toBeInTheDocument();
    expect(helperText).toBeInTheDocument();
  });

  it("renders Submission Button", () => {
    const button = screen.getByText("Submit");
    expect(button).toBeInTheDocument();
  });
});

// TODO: Test Out of Range Input for Wordlist Length (ie. -1 and 601)
describe("Form Intractability", () => {
  beforeEach(() => {
    render(<Form />);
  });

  it("changes the wordlist length input", () => {
    const input = screen.getByDisplayValue("200");
    fireEvent.input(input, { target: { value: "600" } });
    expect(input).toHaveValue("600");
    fireEvent.input(input, { target: { value: "1" } });
    expect(input).toHaveValue("1");
  });

  it("changes the apiKey input", () => {
    const input = screen.getByPlaceholderText("Enter your Api Key");
    fireEvent.change(input, { target: { value: "RandomApiKey" } });
    expect(input).toHaveValue("RandomApiKey");
  });

  // it("submission throws error on invalid input", async () => {
  //   const button = screen.getByText("Submit");
  //   fireEvent.click(button);
  //   const error = await screen.findByText("Error: Wordlist Request Failed.");
  //   expect(error).toBeInTheDocument();
  // });
});
