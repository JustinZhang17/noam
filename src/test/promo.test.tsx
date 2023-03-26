import React from "react";
import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import Promo from "../components/promo";

describe("Promo Smoke Tests", () => {
  it("renders the Promo Component", () => {
    render(<Promo />);
    const button = screen.getByText("Click Here");
    const text = screen.getByText("Come see what else I've been working on!");
    expect(button).toBeInTheDocument();
    expect(text).toBeInTheDocument();
  });
});
