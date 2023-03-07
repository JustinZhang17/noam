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
import axios from "axios";

const Form = () => {
  const [wlLength, setWlLength] = React.useState("200");
  const [apiKey, setApiKey] = React.useState("");
  const [listLoading, setListLoading] = React.useState(false);

  const getWordlist = async (size: Number, apiKey: String) => {
    try {
      const config = {
        headers: {
          method: "GET",
        },
      };

      const resp = await axios.get(
        "/wordlist?size=" + size + "&apiKey=" + apiKey,
        config
      );

      setListLoading(false);
      console.log(resp);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <Box
      display="flex"
      justifyContent="space-between"
      alignItems="center"
      flexDirection="column"
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
          placeholder="Enter your Api Key"
          onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
            setApiKey(e.target.value);
          }}
          value={apiKey}
        />
        <FormHelperText>Don't share this with anyone.</FormHelperText>
      </FormControl>

      <Button
        isLoading={listLoading}
        onClick={() => {
          setListLoading(true);
          getWordlist(parseInt(wlLength), apiKey);
        }}
      >
        Submit
      </Button>
    </Box>
  );
};

export default Form;
