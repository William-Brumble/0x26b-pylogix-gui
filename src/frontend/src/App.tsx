// @ts-ignore
import React, { useEffect, useState } from "react";

import "./App.css";

import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { Separator } from "./components/ui/separator";
import { Input } from "./components/ui/input";
import { Checkbox } from "./components/ui/checkbox";
import { Label } from "./components/ui/label";
import { Button } from "./components/ui/button";

// TODO: Create interfaces for the handler events.

function App() {
  const [token, setToken] = useState("");
  const port = window.location.port;

  useEffect(() => {
    setToken(window?.pywebview?.token);
  }, []);

  const handleConnect = async (e: any) => {
    e.preventDefault();
    const response = await fetch(`http://localhost:${port}/connect`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        token: token,
        ip_address: e.target.ip.value,
        slot: parseInt(e.target.slot.value),
        timeout: parseInt(e.target.timeout.value),
        Micro800: e.target.micro800.checked,
      }),
    });
    const data = await response.json();
    console.log(data);
  };

  const handleClose = async (e: any) => {
    e.preventDefault();
    const response = await fetch(`http://localhost:${port}/close`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        token: token,
      }),
    });
    const data = await response.json();
    console.log(data);
  };

  const handleDiscover = async (e: any) => {
    e.preventDefault();
    const response = await fetch(`http://localhost:${port}/discover`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        token: token,
      }),
    });
    const data = await response.json();
    console.log(data);
  };

  const handleGetModuleProperties = async (e: any) => {
    e.preventDefault();
    const response = await fetch(
      `http://localhost:${port}/get-module-properties`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          token: token,
          slot: parseInt(e.target.slot.value),
        }),
      }
    );
    const data = await response.json();
    console.log(data);
  };

  const handleGetDeviceProperties = async (e: any) => {
    e.preventDefault();
    const response = await fetch(
      `http://localhost:${port}/get-device-properties`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          token: token,
        }),
      }
    );
    const data = await response.json();
    console.log(data);
  };

  const handleGetConnectionSize = async (e: any) => {
    e.preventDefault();
    const response = await fetch(
      `http://localhost:${port}/get-connection-size`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          token: token,
        }),
      }
    );
    const data = await response.json();
    console.log(data);
  };

  const handleSetConnectionSize = async (e: any) => {
    e.preventDefault();
    const response = await fetch(
      `http://localhost:${port}/set-connection-size`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          token: token,
          connection_size: parseInt(e.target.connectionSize.value),
        }),
      }
    );
    const data = await response.json();
    console.log(data);
  };

  const handleRead = async (e: any) => {
    e.preventDefault();
    const response = await fetch(`http://localhost:${port}/read`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        token: token,
        tag: e.target.tag.value,
        count: parseInt(e.target.count.value),
        datatype: parseInt(e.target.datatype.value),
      }),
    });
    const data = await response.json();
    console.log(data);
  };

  const handleWrite = async (e: any) => {
    e.preventDefault();
    const response = await fetch(`http://localhost:${port}/write`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        token: token,
        tag: e.target.tag.value,
        value: Number(e.target.value.value),
        datatype: parseInt(e.target.datatype.value),
      }),
    });
    const data = await response.json();
    console.log(data);
  };

  const handleGetPlcTime = async (e: any) => {
    e.preventDefault();
    const response = await fetch(`http://localhost:${port}/get-plc-time`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        token: token,
        raw: e.target.raw.checked,
      }),
    });
    const data = await response.json();
    console.log(data);
  };

  const handleSetPlcTime = async (e: any) => {
    e.preventDefault();
    const response = await fetch(`http://localhost:${port}/set-plc-time`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        token: token,
      }),
    });
    const data = await response.json();
    console.log(data);
  };

  const handleGetProgramTagList = async (e: any) => {
    e.preventDefault();
    const response = await fetch(
      `http://localhost:${port}/get-program-tag-list`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          token: token,
          program_name: e.target.programName.value,
        }),
      }
    );
    const data = await response.json();
    console.log(data);
  };

  const handleGetProgramsList = async (e: any) => {
    e.preventDefault();
    const response = await fetch(
      `http://localhost:${port}/get-programs-list`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          token: token,
        }),
      }
    );
    const data = await response.json();
    console.log(data);
  };

  const handleGetTagList = async (e: any) => {
    e.preventDefault();
    const response = await fetch(`http://localhost:${port}/get-tag-list`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        token: token,
        all_tags: e.target.allTags.checked,
      }),
    });
    const data = await response.json();
    console.log(data);
  };

  return (
    <div className="bg-background p-5">
      <h2 className="text-foreground mt-10 scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0">
        Manual Operation
      </h2>
      <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
        This particular section is designated exclusively for manual operation,
        primarily intended to facilitate the testing of interprocess communication between the frontend and
        backend processes.
      </p>

      <Accordion type="single" collapsible>
        <AccordionItem value="item-1">
          <AccordionTrigger className="text-foreground">Connect</AccordionTrigger>
          <AccordionContent>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
              Instantiate a pylogix PLC object and establish a connection with the target Programmable Logic Controller (PLC).
            </p>
            <form className="flex flex-col justify-start gap-3 p-1 m-1" onSubmit={handleConnect}>
              <div className="grid max-w-sm items-center gap-1.5">
                <Label
                  className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                  htmlFor="ip">
                  IP:
                </Label>
                <Input type="text" name="ip" placeholder="ip address" />
              </div>
              <div className="grid w-full max-w-sm items-center gap-1.5">
                <Label className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                  SLOT:
                </Label>
                <Input type="number" name="slot" placeholder="slot" />
              </div>
              <div className="grid w-full max-w-sm items-center gap-1.5">
                <Label className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                  TIMEOUT:
                </Label>
                <Input type="number" name="timeout" placeholder="timeout" />
              </div>
              <div className="flex w-full items-center space-x-2 text-foreground pb-4">
                <Checkbox name="micro800" />
                <Label
                  htmlFor="micro800"
                  className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                  MICRO800
                </Label>
              </div>
              <Button className="w-full max-w-sm" type="submit" value="Submit">SUBMIT</Button>
            </form>
          </AccordionContent>
        </AccordionItem>
      </Accordion>

      <Separator />

      <Accordion type="single" collapsible>
        <AccordionItem value="item-1">
          <AccordionTrigger className="text-foreground">Close</AccordionTrigger>
          <AccordionContent>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
              Terminate the connection to the Programmable Logic Controller (PLC).
            </p>
            <form className="flex flex-col justify-start gap-3 p-1 m-1" onSubmit={handleClose}>
              <Button className="w-full max-w-sm" type="submit" value="Submit">SUBMIT</Button>
            </form>
          </AccordionContent>
        </AccordionItem>
      </Accordion>

      <Separator />

      <Accordion type="single" collapsible>
        <AccordionItem value="item-1">
          <AccordionTrigger className="text-foreground">Discover</AccordionTrigger>
          <AccordionContent>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
              Perform a network-wide query to discover all the EIP (EtherNet/IP)
              devices present on the network. The function returns a Response
              class instance containing the attributes: .TagName, .Value, and .Status.
            </p>
            <form className="flex flex-col justify-start gap-3 p-1 m-1" onSubmit={handleDiscover}>
              <Button className="w-full max-w-sm" type="submit" value="Submit">SUBMIT</Button>
            </form>
          </AccordionContent>
        </AccordionItem>
      </Accordion>

      <Separator />

      <Accordion type="single" collapsible>
        <AccordionItem value="item-1">
          <AccordionTrigger className="text-foreground">Get module properties</AccordionTrigger>
          <AccordionContent>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
              Retrieve the properties of the module located in the specified slot.
              The function returns a Response class instance with the attributes:
              .TagName, .Value, and .Status.
            </p>
            <form
              className="flex flex-col justify-start gap-3 p-1 m-1"
              onSubmit={handleGetModuleProperties}
            >
              <div className="grid w-full max-w-sm items-center gap-1.5 pb-4">
                <Label
                  className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                  htmlFor="slot">
                  SLOT:
                </Label>
                <Input type="number" name="slot" placeholder="slot" />
              </div>
              <Button className="w-full max-w-sm" type="submit" value="Submit">SUBMIT</Button>
            </form>
          </AccordionContent>
        </AccordionItem>
      </Accordion>

      <Separator />

      <Accordion type="single" collapsible>
        <AccordionItem value="item-1">
          <AccordionTrigger className="text-foreground">Get device properties</AccordionTrigger>
          <AccordionContent>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
              Retrieve the device properties of a device located at the specified IP address.
              The function returns a Response class instance with the attributes: .TagName, .Value, and .Status.
            </p>
            <form
              className="flex flex-col justify-start gap-3 p-1 m-1"
              onSubmit={handleGetDeviceProperties}
            >
              <Button className="w-full max-w-sm" type="submit" value="Submit">SUBMIT</Button>
            </form>
          </AccordionContent>
        </AccordionItem>
      </Accordion>

      <Separator />

      <Accordion type="single" collapsible>
        <AccordionItem value="item-1">
          <AccordionTrigger className="text-foreground">Get connection size</AccordionTrigger>
          <AccordionContent>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
              The "getConnectionSize" function retrieves and returns the
              current connection size parameter value. It provides access
              to the configured connection size setting, determining the
              size of the established connection. Call this function to
              access the specific connection size value set for your system's requirements.
            </p>
            <form className="flex flex-col justify-start gap-3 p-1 m-1" onSubmit={handleGetConnectionSize}>
              <Button className="w-full max-w-sm" type="submit" value="Submit">SUBMIT</Button>
            </form>
          </AccordionContent>
        </AccordionItem>
      </Accordion>

      <Separator />

      <Accordion type="single" collapsible>
        <AccordionItem value="item-1">
          <AccordionTrigger className="text-foreground">Set connection size</AccordionTrigger>
          <AccordionContent>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
              Please ensure to appropriately configure the "ConnectionSize" parameter prior to
              initiating the first call that necessitates the use of "conn.connect()".
              By default, the system attempts a Large Forward Open followed by a Small Forward Open.
              In case an Explicit (Unconnected) session is utilized, a sensible default option will
              be automatically selected.
            </p>
            <form className="flex flex-col justify-start gap-3 p-1 m-1" onSubmit={handleSetConnectionSize}>
              <div className="grid w-full max-w-sm items-center gap-1.5 pb-4">
                <Label
                  htmlFor="connectionSize"
                  className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                  CONNECTION SIZE:
                </Label>
                <Input type="number" name="connectionSize" placeholder="connection size" />
              </div>
              <Button className="w-full max-w-sm" type="submit" value="Submit">SUBMIT</Button>
            </form>
          </AccordionContent>
        </AccordionItem>
      </Accordion>

      <Separator />

      <Accordion type="single" collapsible>
        <AccordionItem value="item-1">
          <AccordionTrigger className="text-foreground">Read</AccordionTrigger>
          <AccordionContent>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
              The function offers two reading options: retrieving a single tag
              or an array of tags. It returns a Response instance with attributes
              such as .TagName, .Value, and .Status, providing relevant read
              operation information. Note that only single tag retrieval is
              currently supported; array retrieval is not implemented.
            </p>
            <form className="flex flex-col justify-start gap-3 p-1 m-1" onSubmit={handleRead}>
              <div className="grid w-full max-w-sm items-center gap-1.5">
                <Label
                  htmlFor="tag"
                  className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                  TAG:
                </Label>
                <Input type="text" name="tag" placeholder="tag" />
              </div>
              <div className="grid w-full max-w-sm items-center gap-1.5">
                <Label
                  htmlFor="count"
                  className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                  COUNT:
                </Label>
                <Input type="number" name="count" placeholder="count" />
              </div>
              <div className="grid w-full max-w-sm items-center gap-1.5 pb-4">
                <Label
                  htmlFor="datatype"
                  className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                  DATATYPE:
                </Label>
                <Select name="datatype">
                  <SelectTrigger className="text-foreground w-full max-w-sm">
                    <SelectValue placeholder="Datatype" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value={"0xc1"}>BOOL</SelectItem>
                    <SelectItem value={"0xc2"}>SINT</SelectItem>
                    <SelectItem value={"0xc3"}>INT</SelectItem>
                    <SelectItem value={"0xc4"}>DINT</SelectItem>
                    <SelectItem value={"0xca"}>REAL</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              <Button className="w-full max-w-sm" type="submit" value="Submit">SUBMIT</Button>
            </form>
          </AccordionContent>
        </AccordionItem>
      </Accordion>

      <Separator />

      <Accordion type="single" collapsible>
        <AccordionItem value="item-1">
          <AccordionTrigger className="text-foreground">Write</AccordionTrigger>
          <AccordionContent>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
              This function offers two writing options:
              generating a single tag or an array. The output is a Response class
              instance (.TagName, .Value, .Status). Note that only single value
              writing is currently supported; array writing is not implemented.
            </p>
            <form className="flex flex-col justify-start gap-3 p-1 m-1" onSubmit={handleWrite}>
              <div className="grid w-full max-w-sm items-center gap-1.5">
                <Label
                  htmlFor="tag"
                  className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                  TAG:
                </Label>
                <Input type="number" name="tag" placeholder="tag" />
              </div>
              <div className="grid w-full max-w-sm items-center gap-1.5">
                <Label
                  htmlFor="value"
                  className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                  VALUE:
                </Label>
                <Input type="number" name="value" placeholder="value" />
              </div>
              <div className="grid w-full max-w-sm items-center gap-1.5 pb-4">
                <Label
                  htmlFor="datatype"
                  className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                  DATATYPE:
                </Label>
                <Select name="datatype">
                  <SelectTrigger className="text-foreground w-full max-w-sm">
                    <SelectValue placeholder="Datatype" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value={"0xc1"}>BOOL</SelectItem>
                    <SelectItem value={"0xc2"}>SINT</SelectItem>
                    <SelectItem value={"0xc3"}>INT</SelectItem>
                    <SelectItem value={"0xc4"}>DINT</SelectItem>
                    <SelectItem value={"0xca"}>REAL</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              <Button className="w-full max-w-sm" type="submit" value="Submit">SUBMIT</Button>
            </form>
          </AccordionContent>
        </AccordionItem>
      </Accordion>

      <Separator />

      <Accordion type="single" collapsible>
        <AccordionItem value="item-1">
          <AccordionTrigger className="text-foreground">Get plc time</AccordionTrigger>
          <AccordionContent>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
              Retrieve the controller clock time and obtain it in a human-readable format
              (default) or in raw format if the raw parameter is set to True.
              <br />
              The function returns an instance of the Response class, which includes the
              following attributes: .TagName, .Value, and .Status.
            </p>
            <form className="flex flex-col justify-start gap-3 p-1 m-1" onSubmit={handleGetPlcTime}>
              <div className="flex w-full items-center space-x-2 text-foreground pb-4">
                <Checkbox name="raw" />
                <Label
                  htmlFor="raw"
                  className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                  RAW
                </Label>
              </div>
              <Button className="w-full max-w-sm" type="submit" value="Submit">SUBMIT</Button>
            </form>
          </AccordionContent>
        </AccordionItem>
      </Accordion>

      <Separator />

      <Accordion type="single" collapsible>
        <AccordionItem value="item-1">
          <AccordionTrigger className="text-foreground">Set plc time</AccordionTrigger>
          <AccordionContent>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
              This function is utilized to set the controller clock time.
              <br />
              Upon execution, the function returns an instance of the Response class,
              which encompasses the following attributes: .TagName, .Value, and .Status.
            </p>
            <form className="flex flex-col justify-start gap-3 p-1 m-1" onSubmit={handleSetPlcTime}>
              <Button className="w-full max-w-sm" type="submit" value="Submit">SUBMIT</Button>
            </form>
          </AccordionContent>
        </AccordionItem>
      </Accordion>

      <Separator />

      <Accordion type="single" collapsible>
        <AccordionItem value="item-1">
          <AccordionTrigger className="text-foreground">Get program tag list</AccordionTrigger>
          <AccordionContent>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
              Retrieve a program tag list from the PLC using the programName parameter
              ("Program:ExampleProgram"). The function returns a Response class
              instance (.TagName, .Value, .Status).
            </p>
            <form className="flex flex-col justify-start gap-3 p-1 m-1" onSubmit={handleGetProgramTagList}>
              <div className="grid w-full max-w-sm items-center gap-1.5 pb-4">
                <Label
                  htmlFor="programName"
                  className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                  PROGRAM NAME:
                </Label>
                <Input type="number" name="programName" placeholder="program name" />
              </div>
              <Button className="w-full max-w-sm" type="submit" value="Submit">SUBMIT</Button>
            </form>
          </AccordionContent>
        </AccordionItem>
      </Accordion>

      <Separator />

      <Accordion type="single" collapsible>
        <AccordionItem value="item-1">
          <AccordionTrigger className="text-foreground">Get programs list</AccordionTrigger>
          <AccordionContent>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
              Retrieve a program names list from the PLC. Perform a sanity check to
              verify if the programNames parameter is empty, and then execute the
              _getTagList function. The function returns a Response class instance
              (.TagName, .Value, .Status).
            </p>
            <form className="flex flex-col justify-start gap-3 p-1 m-1" onSubmit={handleGetProgramsList}>
              <Button className="w-full max-w-sm" type="submit" value="Submit">SUBMIT</Button>
            </form>
          </AccordionContent>
        </AccordionItem>
      </Accordion>

      <Separator />

      <Accordion type="single" collapsible>
        <AccordionItem value="item-1">
          <AccordionTrigger className="text-foreground">Get tag list</AccordionTrigger>
          <AccordionContent>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
              Retrieve the tag list from the PLC, with the optional parameter allTags.
              If allTags is set to False, only controller tags are returned; otherwise,
              both controller tags and program tags are returned. The function returns
              a Response class instance (.TagName, .Value, .Status).
            </p>
            <form className="flex flex-col justify-start gap-3 p-1 m-1" onSubmit={handleGetTagList}>
              <div className="flex w-full items-center space-x-2 text-foreground pb-4">
                <Checkbox name="allTags" />
                <Label
                  htmlFor="allTags"
                  className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                  ALL TAGS
                </Label>
              </div>
              <Button className="w-full max-w-sm" type="submit" value="Submit">SUBMIT</Button>
            </form>
          </AccordionContent>
        </AccordionItem>
      </Accordion>
    </div>
  );
}

export default App;
