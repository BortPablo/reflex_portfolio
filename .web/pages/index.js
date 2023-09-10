import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { E, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, uploadFiles, useEventLoop } from "/utils/state"
import { EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import { Box, Button, ButtonGroup, Center, Container, Heading, HStack, Image, Link, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Tab, TabList, TabPanel, TabPanels, Tabs, Text, useColorMode, VStack } from "@chakra-ui/react"
import NextLink from "next/link"
import { ArrowForwardIcon } from "@chakra-ui/icons"
import NextHead from "next/head"


export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const { colorMode, toggleColorMode } = useColorMode()
  const focusRef = useRef();
  
  // Main event loop.
  const [Event, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => Event(initialEvents.map((e) => ({...e})))
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {`http://localhost:8000`}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <VStack>
  <Heading sx={{"fontSize": "2.5em", "fontWeight": "bold", "marginY": "0.25em", "marginX": "0.25em", "textAlign": "center", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "bgClip": "text", "height": "2em"}}>
  {`Pablo Bort`}
</Heading>
  <Tabs orientation={`vertical`} sx={{"width": "90%"}} variant={`soft-rounded`}>
  <TabList>
  <Tab sx={{"height": "10em"}}>
  <Heading sx={{"fontSize": "2.5em", "fontWeight": "bold", "marginY": "0.25em", "marginX": "0.25em", "textAlign": "center", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "bgClip": "text"}}>
  {`About me`}
</Heading>
</Tab>
  <Tab sx={{"height": "10em"}}>
  <Heading sx={{"fontSize": "2.5em", "fontWeight": "bold", "marginY": "0.25em", "marginX": "0.25em", "textAlign": "center", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "bgClip": "text"}}>
  {`Technologies`}
</Heading>
</Tab>
  <Tab sx={{"height": "10em"}}>
  <Heading sx={{"fontSize": "2.5em", "fontWeight": "bold", "marginY": "0.25em", "marginX": "0.25em", "textAlign": "center", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "bgClip": "text"}}>
  {`Personal projects`}
</Heading>
</Tab>
</TabList>
  <TabPanels>
  <TabPanel>
  <HStack>
  <Container sx={{"width": "60%"}}>
  <VStack>
  <Text sx={{"padding": "1em", "borderRadius": "5px", "marginY": "0.25em", "display": "inline-block", "fontFamily": "Hack Nerd Font Mono", "fontSize": "15px"}}>
  {`Graduated in physics with a master's degree in Big Data Analytics. 
                Currently working as a Data Scientist, engaging with a variety of projects, 
                including European energy initiatives.`}
</Text>
  <Text sx={{"padding": "1em", "borderRadius": "5px", "marginY": "0.25em", "display": "inline-block", "fontFamily": "Hack Nerd Font Mono", "fontSize": "15px"}}>
  {`Interested in Artificial Intelligence, data analysis, and visualization.
                 This portfolio showcases projects that highlight my commitment to leveraging data for meaningful outcomes.
                 I invite you to explore and connect.`}
</Text>
  <Link as={NextLink} href={`https://drive.google.com/uc?id=1NRtDqXdPOhDFerh0NApQIdvkTrrPJCTh&export=download`}>
  <Button sx={{"borderRadius": "1em", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "opacity": "0.8", "_hover": {"background": "white", "boxShadow": "0 0 5px 5px #FF0080"}}}>
  <Text sx={{"padding": "1em", "borderRadius": "5px", "marginY": "0.25em", "display": "inline-block", "fontFamily": "Hack Nerd Font Mono", "fontSize": "15px"}}>
  {`Download CV`}
</Text>
  <Image src={`/icons/cv.png`} sx={{"width": "100%", "height": "100%"}}/>
</Button>
</Link>
</VStack>
</Container>
  <Container sx={{"width": "40%"}}>
  <Center>
  <Image src={`/me/me.jpg`} sx={{"borderRadius": "25% 25%"}}/>
</Center>
</Container>
</HStack>
</TabPanel>
  <TabPanel>
  <VStack>
  <HStack sx={{"height": "10em", "width": "100%", "borderRadius": "1em", "border": "1px solid #FF0080"}}>
  <VStack sx={{"width": "20%"}}>
  <Heading sx={{"fontSize": "1.5em", "textAlign": "center", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "bgClip": "text"}}>
  {`ETL/ML frameworks`}
</Heading>
</VStack>
  <Box sx={{"width": "75%"}}>
  <HStack>
  <VStack sx={{"width": "25%"}}>
  <Image src={`/icons/MLflow-Logo.svg`}/>
</VStack>
  <VStack sx={{"width": "25%"}}>
  <Image src={`/icons/Qlik_Logo.png`} sx={{"width": "70%", "height": "70%"}}/>
</VStack>
  <VStack sx={{"width": "25%"}}>
  <Image src={`/icons/tableau-logo.png`} sx={{"width": "50%", "height": "50%"}}/>
</VStack>
  <VStack sx={{"width": "25%"}}>
  <Image src={`/icons/grafana-logo.png`} sx={{"width": "40%", "height": "40%"}}/>
</VStack>
</HStack>
</Box>
</HStack>
  <HStack sx={{"height": "10em", "width": "100%", "borderRadius": "1em", "border": "1px solid #FF0080"}}>
  <VStack sx={{"width": "20%"}}>
  <Heading sx={{"fontSize": "1.5em", "textAlign": "center", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "bgClip": "text"}}>
  {`Python packages`}
</Heading>
</VStack>
  <Box sx={{"width": "75%"}}>
  <HStack>
  <VStack sx={{"width": "14.2%"}}>
  <Image src={`/icons/pandas-logo.png`}/>
</VStack>
  <VStack sx={{"width": "14.2%"}}>
  <Image src={`/icons/scipy-logo.png`}/>
</VStack>
  <VStack sx={{"width": "14.2%"}}>
  <Image src={`/icons/numpy-logo.png`}/>
</VStack>
  <VStack sx={{"width": "14.2%"}}>
  <Image src={`/icons/matplotlib-logo.png`}/>
</VStack>
  <VStack sx={{"width": "14.2%"}}>
  <Image src={`/icons/tensorflow-logo.png`}/>
</VStack>
  <VStack sx={{"width": "14.2%"}}>
  <Image src={`/icons/sklearn-logo.png`}/>
</VStack>
  <VStack sx={{"width": "14.2%"}}>
  <Image src={`/icons/xgboost-logo.png`}/>
</VStack>
</HStack>
</Box>
</HStack>
  <HStack sx={{"height": "10em", "width": "100%", "borderRadius": "1em", "border": "1px solid #FF0080"}}>
  <VStack sx={{"width": "20%"}}>
  <Heading sx={{"fontSize": "1.5em", "textAlign": "center", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "bgClip": "text"}}>
  {`Databases`}
</Heading>
</VStack>
  <Box sx={{"width": "75%"}}>
  <HStack>
  <VStack sx={{"width": "33%"}}>
  <Image src={`/icons/influxdb-logo.png`}/>
</VStack>
  <VStack sx={{"width": "33%"}}>
  <Image src={`/icons/mongodb-logo.png`} sx={{"width": "70%", "height": "70%"}}/>
</VStack>
  <VStack sx={{"width": "33%"}}>
  <Image src={`/icons/mysql-logo.png`} sx={{"width": "70%", "height": "70%"}}/>
</VStack>
</HStack>
</Box>
</HStack>
  <HStack sx={{"height": "10em", "width": "100%", "borderRadius": "1em", "border": "1px solid #FF0080"}}>
  <VStack sx={{"width": "20%"}}>
  <Heading sx={{"fontSize": "1.5em", "textAlign": "center", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "bgClip": "text"}}>
  {`Deployment`}
</Heading>
</VStack>
  <Box sx={{"width": "75%"}}>
  <HStack>
  <VStack sx={{"width": "33%"}}>
  <Image src={`/icons/portainer-logo.png`} sx={{"width": "70%", "height": "70%"}}/>
</VStack>
  <VStack sx={{"width": "33%"}}>
  <Image src={`/icons/docker-logo.png`} sx={{"width": "70%", "height": "70%"}}/>
</VStack>
  <VStack sx={{"width": "33%"}}>
  <Image src={`/icons/kubernetes-logo.png`} sx={{"width": "70%", "height": "70%"}}/>
</VStack>
</HStack>
</Box>
</HStack>
</VStack>
</TabPanel>
  <TabPanel>
  <VStack>
  <HStack sx={{"height": "10em", "width": "100%", "borderRadius": "1em", "border": "1px solid #FF0080"}}>
  <VStack sx={{"width": "33%"}}>
  <Heading sx={{"fontSize": "1.5em", "textAlign": "center", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "bgClip": "text"}}>
  {`Calculator`}
</Heading>
</VStack>
  <VStack sx={{"width": "33%"}}>
  <Text sx={{"padding": "1em", "borderRadius": "5px", "marginY": "0.25em", "display": "inline-block", "fontFamily": "Hack Nerd Font Mono", "fontSize": "15px"}}>
  {`A simple example of a calculator showing how I usually work in Python.`}
</Text>
</VStack>
  <VStack sx={{"width": "33%", "centerContent": true}}>
  <Link as={NextLink} href={`https://github.com/BortPablo/calculator-test`} isExternal={true}>
  <Button sx={{"borderRadius": "1em", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "opacity": "0.8", "_hover": {"background": "white", "boxShadow": "0 0 5px 5px #FF0080"}}}>
  <Image src={`/icons/GitHub_Logo.png`} sx={{"width": "100%", "height": "100%"}}/>
</Button>
</Link>
</VStack>
</HStack>
  <HStack sx={{"height": "10em", "width": "100%", "borderRadius": "1em", "border": "1px solid #FF0080"}}>
  <VStack sx={{"width": "33%"}}>
  <Heading sx={{"fontSize": "1.5em", "textAlign": "center", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "bgClip": "text"}}>
  {`Poker`}
</Heading>
</VStack>
  <VStack sx={{"width": "33%"}}>
  <Text sx={{"padding": "1em", "borderRadius": "5px", "marginY": "0.25em", "display": "inline-block", "fontFamily": "Hack Nerd Font Mono", "fontSize": "15px"}}>
  {`Personal project concerning probabilities in poker (Texas Hold'em).`}
</Text>
</VStack>
  <VStack sx={{"width": "33%"}}>
  <Link as={NextLink} href={`https://github.com/BortPablo/poker`} isExternal={true}>
  <Button sx={{"borderRadius": "1em", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "opacity": "0.8", "_hover": {"background": "white", "boxShadow": "0 0 5px 5px #FF0080"}}}>
  <Image src={`/icons/GitHub_Logo.png`} sx={{"width": "100%", "height": "100%"}}/>
</Button>
</Link>
</VStack>
</HStack>
  <HStack sx={{"height": "10em", "width": "100%", "borderRadius": "1em", "border": "1px solid #FF0080"}}>
  <VStack sx={{"width": "33%"}}>
  <Heading sx={{"fontSize": "1.5em", "textAlign": "center", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "bgClip": "text"}}>
  {`Turbine predictive maintenance`}
</Heading>
</VStack>
  <VStack sx={{"width": "33%"}}>
  <Text sx={{"padding": "1em", "borderRadius": "5px", "marginY": "0.25em", "display": "inline-block", "fontFamily": "Hack Nerd Font Mono", "fontSize": "15px"}}>
  {`Personal project improving methodology and models of master thesis for turbine predictive maintenance.`}
</Text>
</VStack>
  <VStack sx={{"width": "33%"}}>
  <Link as={NextLink} href={`https://github.com/BortPablo/turbine_predictive_maintenance`} isExternal={true}>
  <Button sx={{"borderRadius": "1em", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "opacity": "0.8", "_hover": {"background": "white", "boxShadow": "0 0 5px 5px #FF0080"}}}>
  <Image src={`/icons/GitHub_Logo.png`} sx={{"width": "100%", "height": "100%"}}/>
</Button>
</Link>
</VStack>
</HStack>
  <HStack sx={{"height": "10em", "width": "100%", "borderRadius": "1em", "border": "1px solid #FF0080"}}>
  <VStack sx={{"width": "33%"}}>
  <Heading sx={{"fontSize": "1.5em", "textAlign": "center", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "bgClip": "text"}}>
  {`Reflex portfolio`}
</Heading>
</VStack>
  <VStack sx={{"width": "33%"}}>
  <Text sx={{"padding": "1em", "borderRadius": "5px", "marginY": "0.25em", "display": "inline-block", "fontFamily": "Hack Nerd Font Mono", "fontSize": "15px"}}>
  {`Project showcasing this portfolio structure with Reflex package.`}
</Text>
</VStack>
  <VStack sx={{"width": "33%"}}>
  <Link as={NextLink} href={`https://github.com/BortPablo/reflex_portfolio`} isExternal={true}>
  <Button sx={{"borderRadius": "1em", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "opacity": "0.8", "_hover": {"background": "white", "boxShadow": "0 0 5px 5px #FF0080"}}}>
  <Image src={`/icons/GitHub_Logo.png`} sx={{"width": "100%", "height": "100%"}}/>
</Button>
</Link>
</VStack>
</HStack>
</VStack>
</TabPanel>
</TabPanels>
</Tabs>
  <Container centerContent={true}>
  <Text sx={{"padding": "1em", "borderRadius": "5px", "marginY": "0.25em", "display": "inline-block", "fontFamily": "Hack Nerd Font Mono", "fontSize": "15px"}}>
  {`Feel free to get in touch with me:`}
</Text>
  <ButtonGroup>
  <Link as={NextLink} href={`mailto:pablobort98@gmail.com`}>
  <Button sx={{"borderRadius": "1em", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "opacity": "0.8", "_hover": {"background": "white", "boxShadow": "0 0 5px 5px #FF0080"}}}>
  <Image src={`/icons/email.png`} sx={{"width": "100%", "height": "100%"}}/>
</Button>
</Link>
  <Link as={NextLink} href={`https://www.linkedin.com/in/pablo-bort-gomez/`} isExternal={true}>
  <Button sx={{"borderRadius": "1em", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "opacity": "0.8", "_hover": {"background": "white", "boxShadow": "0 0 5px 5px #FF0080"}}}>
  <Image src={`/icons/icons8-linkedin.svg`} sx={{"width": "100%", "height": "100%"}}/>
</Button>
</Link>
  <Link as={NextLink} href={`https://github.com/BortPablo`} isExternal={true}>
  <Button sx={{"borderRadius": "1em", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "opacity": "0.8", "_hover": {"background": "white", "boxShadow": "0 0 5px 5px #FF0080"}}}>
  <Image src={`/icons/github-mark.svg`} sx={{"width": "100%", "height": "100%"}}/>
</Button>
</Link>
  <Link as={NextLink} href={`/es`}>
  <Button sx={{"borderRadius": "1em", "bgGradient": "linear(to-l, #7928CA, #FF0080)", "opacity": "0.8", "_hover": {"background": "white", "boxShadow": "0 0 5px 5px #FF0080"}}}>
  <Text sx={{"padding": "1em", "borderRadius": "5px", "marginY": "0.25em", "display": "inline-block", "fontFamily": "Hack Nerd Font Mono", "fontSize": "15px"}}>
  {`EN`}
</Text>
  <ArrowForwardIcon/>
  <Text sx={{"padding": "1em", "borderRadius": "5px", "marginY": "0.25em", "display": "inline-block", "fontFamily": "Hack Nerd Font Mono", "fontSize": "15px"}}>
  {`ES`}
</Text>
</Button>
</Link>
</ButtonGroup>
</Container>
</VStack>
  <NextHead>
  <title>
  {`Pablo Bort | Portfolio | EN`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
