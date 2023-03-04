// External Imports
import React from "react";
import {
  Box,
  Button,
  NumberInput,
  NumberInputField,
  NumberInputStepper,
  NumberDecrementStepper,
  NumberIncrementStepper,
  FormControl,
  FormLabel,
  FormHelperText,
  Input,
} from "@chakra-ui/react";

const Form = () => {
  const [wlLength, setWlLength] = React.useState("200");
  const [apiKey, setApiKey] = React.useState("");

  return (
    <Box
      display='flex'
      justifyContent='space-between'
      alignItems='center'
      flexDirection='column'
      mx={{ base: 5, md: 60 }}
      my={{ base: 10 }}
    >
      <FormControl>
        <FormLabel mt={6}>Wordlist Length</FormLabel>
        <NumberInput
          defaultValue={wlLength}
          min={1}
          max={600}
          onChange={(valueString: string) => setWlLength(valueString)}
          value={wlLength}
        >
          <NumberInputField />
          <NumberInputStepper>
            <NumberIncrementStepper />
            <NumberDecrementStepper />
          </NumberInputStepper>
        </NumberInput>
        <FormHelperText>Max 600 Words.</FormHelperText>

        <FormLabel mt={6}>Api Key</FormLabel>
        <Input
          placeholder='Enter your Api Key'
          onChange={(e: any) => setApiKey(e.target.value)}
          value={apiKey}
        />
        <FormHelperText>Don't share this with anyone.</FormHelperText>
      </FormControl>

      <Button
        onClick={() => {
          console.log("Clicked");
        }}
      >
        Submit
      </Button>
    </Box>
  );
};

// Input onChange event parameters need to be changed to be strongly typed

export default Form;
