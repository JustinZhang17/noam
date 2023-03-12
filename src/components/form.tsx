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
  useToast,
} from "@chakra-ui/react";
import axios from "axios";
import { saveAs } from "file-saver";

const Form = () => {
  const [wlLength, setWlLength] = React.useState("200");
  const [apiKey, setApiKey] = React.useState("");
  const [listLoading, setListLoading] = React.useState(false);
  const Toast = useToast();

  const formError = (): void => {
    Toast({
      title: "Error: Wordlist Request Failed.",
      description: "Please check your Api Key and Wordlist Length are valid.",
      status: "error",
      variant: "solid",
      duration: 4000,
      isClosable: true,
    });
    setListLoading(false);
  };

  const getWordlist = async (size: number, apiKey: string) => {
    if (apiKey === "" || size > 600) return formError();

    try {
      const resp = await axios.get(
        "/wordlist?size=" + size + "&apiKey=" + apiKey,
        {
          headers: {
            method: "GET",
          },
          responseType: "blob",
        }
      );

      Toast({
        title: "Wordlist Created!",
        description: "Filename: Noam-Wordlist-" + size + ".xlsx",
        status: "success",
        duration: 9000,
        isClosable: true,
      });

      setListLoading(false);
      const blob = new Blob([resp.data], {
        type:
          resp.data?.type ??
          "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      });
      saveAs(blob, "Noam-Wordlist-" + size + ".xlsx");
    } catch (err: any) {
      console.error(err);
      if (err?.code === "ERR_BAD_REQUEST") {
        return formError();
      }
      setListLoading(false);
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
        mt={5}
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
