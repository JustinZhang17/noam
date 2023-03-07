// External Imports
import {
  Box,
  Flex,
  Button,
  Heading,
  Image,
  useColorModeValue,
  Stack,
  useColorMode,
  Link,
} from "@chakra-ui/react";
import { MoonIcon, SunIcon, ChatIcon } from "@chakra-ui/icons";
import { FaCode } from "react-icons/fa";

const Navbar = () => {
  const { colorMode, toggleColorMode } = useColorMode();
  return (
    <Box bg={useColorModeValue("gray.100", "gray.900")} px={4}>
      <Flex h={16} alignItems={"center"} justifyContent={"space-between"}>
        <Flex alignItems={"center"}>
          <Image
            boxSize={10}
            objectFit={"cover"}
            src={useColorModeValue("logo-color.png", "logo-white.png")}
            alt="Noam Logo"
            mx={3}
            fallbackSrc="https://via.placeholder.com/150"
          />
          <Heading>Noam</Heading>
        </Flex>

        <Flex alignItems={"center"}>
          <Stack direction={"row"} spacing={7}>
            <Link href="https://blog.justinjzhang.com/" isExternal>
              <Button leftIcon={<ChatIcon />}>What is this?</Button>
            </Link>
            <Link href="https://github.com/JustinZhang17" isExternal>
              <Button leftIcon={<FaCode />}>Source Code</Button>
            </Link>
            <Button onClick={toggleColorMode}>
              {colorMode === "light" ? <MoonIcon /> : <SunIcon />}
            </Button>
          </Stack>
        </Flex>
      </Flex>
    </Box>
  );
};

export default Navbar;
