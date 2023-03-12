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
import { FaCode, FaQuestion } from "react-icons/fa";

const Navbar = () => {
  const { colorMode, toggleColorMode } = useColorMode();

  const ButtonColor = useColorModeValue("gray.300", "gray.700");
  return (
    <Box bg={useColorModeValue("gray.100", "gray.900")} px={4}>
      <Flex h={16} alignItems={"center"} justifyContent={"space-between"}>
        <Flex alignItems={"center"}>
          <Image
            boxSize={{ base: 10, md: 10 }}
            objectFit={"cover"}
            src={useColorModeValue("logo-color.png", "logo-white.png")}
            alt="Noam Logo"
            mx={3}
            fallbackSrc="https://via.placeholder.com/150"
          />
          <Heading fontSize={{ base: 22, md: 32 }}>Noam</Heading>
        </Flex>

        <Flex alignItems={"center"}>
          <Stack direction={"row"} spacing={{ base: 3, md: 7 }}>
            <Link href="https://blog.justinjzhang.com/noam" isExternal>
              <Button
                leftIcon={<ChatIcon />}
                display={{ base: "none", md: "block" }}
                bgColor={ButtonColor}
              >
                What is this?
              </Button>
              <Button
                display={{ base: "block", md: "none" }}
                bgColor={ButtonColor}
              >
                <FaQuestion />
              </Button>
            </Link>
            <Link href="https://github.com/JustinZhang17/noam" isExternal>
              <Button
                leftIcon={<FaCode />}
                display={{ base: "none", md: "block" }}
                bgColor={ButtonColor}
              >
                Source Code
              </Button>
              <Button
                display={{ base: "block", md: "none" }}
                bgColor={ButtonColor}
              >
                <FaCode />
              </Button>
            </Link>
            <Button onClick={toggleColorMode} bgColor={ButtonColor}>
              {colorMode === "light" ? <MoonIcon /> : <SunIcon />}
            </Button>
          </Stack>
        </Flex>
      </Flex>
    </Box>
  );
};

export default Navbar;
