import { ChatIcon } from "@chakra-ui/icons";
import {
  Box,
  Button,
  Flex,
  Stack,
  Text,
  useColorModeValue,
  Link,
} from "@chakra-ui/react";

const Promo = () => {
  return (
    <Box bg={useColorModeValue("orange.200", "orange.400")} px={4}>
      <Flex h={16} alignItems={"center"} justifyContent={"space-between"}>
        <Flex alignItems={"center"} mx={5}>
          <ChatIcon boxSize={4} mr={3} />
          <Text>Come see what other projects I've been working on!</Text>
        </Flex>

        <Flex alignItems={"center"}>
          <Stack direction={"row"} spacing={7}>
            <Link href='https://linktr.ee/justinjzhang' isExternal>
              <Button>Click Here</Button>
            </Link>
          </Stack>
        </Flex>
      </Flex>
    </Box>
  );
};

export default Promo;
