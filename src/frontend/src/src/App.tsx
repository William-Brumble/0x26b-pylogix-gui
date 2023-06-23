// @ts-ignore
import React from 'react'
import './App.css'

// TODO: Create interfaces for the handler events.

function App() {

    const handleConnect = async (e: any)=>{
        e.preventDefault()
        const response = await fetch(`http://localhost:5000/connect`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                //token: window.pywebview.token,
                token: "test",
                ip_address: e.target.ip.value,
                slot: parseInt(e.target.slot.value),
                timeout: parseInt(e.target.timeout.value),
                Micro800: e.target.micro800.checked
            }),
        })
        const data = await response.json()
        console.log(data);
    }

    const handleClose = async (e: any)=>{
        e.preventDefault()
        const response = await fetch(`http://localhost:5000/close`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                //token: window.pywebview.token,
                token: "test",
            }),
        })
        const data = await response.json()
        console.log(data);
    }

    const handleDiscover = async (e: any)=>{
        e.preventDefault()
        const response = await fetch(`http://localhost:5000/discover`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                //token: window.pywebview.token,
                token: "test",
            }),

        })
        const data = await response.json()
        console.log(data);
    }

    const handleGetModuleProperties = async (e: any)=>{
        e.preventDefault()
        const response = await fetch(`http://localhost:5000/get-module-properties`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                //token: window.pywebview.token,
                token: "test",
                slot: parseInt(e.target.slot.value)
            }),
        })
        const data = await response.json()
        console.log(data);
    }

    const handleGetDeviceProperties = async (e: any)=>{
        e.preventDefault()
        const response = await fetch(`http://localhost:5000/get-device-properties`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                //token: window.pywebview.token,
                token: "test",
            }),
        })
        const data = await response.json()
        console.log(data);
    }

    const handleGetConnectionSize = async (e: any)=>{
        e.preventDefault()
        const response = await fetch(`http://localhost:5000/get-connection-size`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                //token: window.pywebview.token,
                token: "test",
            }),
        })
        const data = await response.json()
        console.log(data);
    }

    const handleSetConnectionSize = async (e: any)=>{
        e.preventDefault()
        const response = await fetch(`http://localhost:5000/set-connection-size`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                //token: window.pywebview.token,
                token: "test",
                connection_size: parseInt(e.target.connectionSize.value)
            }),
        })
        const data = await response.json()
        console.log(data);
    }

    const handleRead = async (e: any)=>{
        e.preventDefault()
        const response = await fetch(`http://localhost:5000/read`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                //token: window.pywebview.token,
                token: "test",
                tag: e.target.tag.value,
                count: parseInt(e.target.count.count),
                datatype: parseInt(e.target.datatype.value)
            }),
        })
        const data = await response.json()
        console.log(data);
    }

    const handleWrite = async (e: any)=>{
        e.preventDefault()
        const response = await fetch(`http://localhost:5000/write`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                //token: window.pywebview.token,
                token: "test",
                tag: e.target.tag.value,
                value: Number(e.target.value.value),
                datatype: parseInt(e.target.datatype.value)
            }),
        })
        const data = await response.json()
        console.log(data);
    }

    const handleGetPlcTime = async (e: any)=>{
        e.preventDefault()
        const response = await fetch(`http://localhost:5000/get-plc-time`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                //token: window.pywebview.token,
                token: "test",
                raw: e.target.raw.checked,
            }),
        })
        const data = await response.json()
        console.log(data);
    }

    const handleSetPlcTime = async (e: any)=>{
        e.preventDefault()
        const response = await fetch(`http://localhost:5000/set-plc-time`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                //token: window.pywebview.token,
                token: "test",
            }),
        })
        const data = await response.json()
        console.log(data);
    }

    const handleGetProgramTagList = async (e: any)=>{
        e.preventDefault()
        const response = await fetch(`http://localhost:5000/get-program-tag-list`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                //token: window.pywebview.token,
                token: "test",
                program_name: e.target.programName.value,
            }),
        })
        const data = await response.json()
        console.log(data);
    }

    const handleGetProgramsList = async (e: any)=>{
        e.preventDefault()
        const response = await fetch(`http://localhost:5000/get-programs-list`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                //token: window.pywebview.token,
                token: "test",
            }),
        })
        const data = await response.json()
        console.log(data);
    }

    const handleGetTagList = async (e: any)=>{
        e.preventDefault()
        const response = await fetch(`http://localhost:5000/get-tag-list`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                //token: window.pywebview.token,
                token: "test",
                all_tags: e.target.allTags.checked,
            }),
        })
        const data = await response.json()
        console.log(data);
    }

    return (
    <>
        <p>CONNECT</p>
        <form className="form-container" onSubmit={handleConnect}>
            <label>
                IP:
                <input type="text" name="ip" />
            </label>
            <label>
                SLOT:
                <input type="number" name="slot" />
            </label>
            <label>
                TIMEOUT:
                <input type="number" name="timeout" />
            </label>
            <label>
                MICRO800:
                <input type="checkbox" name="micro800" />
            </label>
            <input type="submit" value="Submit" />
        </form>

        <hr/>

        <p>CLOSE</p>
        <form className="form-container" onSubmit={handleClose}>
            <input type="submit" value="Submit" />
        </form>

        <hr/>

        <p>DISCOVER</p>
        <form className="form-container" onSubmit={handleDiscover}>
            <input type="submit" value="Submit" />
        </form>

        <hr/>

        <p>GET MODULE PROPERTIES</p>
        <form className="form-container" onSubmit={handleGetModuleProperties}>
            <label>
                SLOT:
                <input type="number" name="slot" />
            </label>
            <input type="submit" value="Submit" />
        </form>

        <hr/>

        <p>GET DEVICE PROPERTIES</p>
        <form className="form-container" onSubmit={handleGetDeviceProperties}>
            <input type="submit" value="Submit" />
        </form>

        <hr/>

        <p>GET CONNECTION SIZE</p>
        <form className="form-container" onSubmit={handleGetConnectionSize}>
            <input type="submit" value="Submit" />
        </form>

        <hr/>

        <p>SET CONNECTION SIZE</p>
        <form className="form-container" onSubmit={handleSetConnectionSize}>
            <label>
                CONNECTION SIZE:
                <input type="number" name="connectionSize" />
            </label>
            <input type="submit" value="Submit" />
        </form>

        <hr/>

        <p>READ</p>
        <form className="form-container" onSubmit={handleRead}>
            <label>
                TAG:
                <input type="text" name="tag" />
            </label>
            <label>
                COUNT:
                <input type="number" name="count" />
            </label>
            <label>
                DATATYPE:
                <input type="number" name="datatype" />
            </label>
            <input type="submit" value="Submit" />
        </form>

        <hr/>

        <p>WRITE</p>
        <form className="form-container" onSubmit={handleWrite}>
            <label>
                TAG:
                <input type="text" name="tag" />
            </label>
            <label>
                VALUE:
                <input type="number" name="value" step="0.01"/>
            </label>
            <label>
                DATATYPE:
                <input type="number" name="datatype" />
            </label>
            <input type="submit" value="Submit" />
        </form>

        <hr/>

        <p>GET PLC TIME</p>
        <form className="form-container" onSubmit={handleGetPlcTime}>
            <label>
                RAW:
                <input type="checkbox" name="raw" />
            </label>
            <input type="submit" value="Submit" />
        </form>

        <hr/>

        <p>SET PLC TIME</p>
        <form className="form-container" onSubmit={handleSetPlcTime}>
            <input type="submit" value="Submit" />
        </form>

        <hr/>

        <p>GET PROGRAM TAG LIST</p>
        <form className="form-container" onSubmit={handleGetProgramTagList}>
            <label>
                PROGRAM NAME:
                <input type="text" name="programName" />
            </label>
            <input type="submit" value="Submit" />
        </form>

        <hr/>

        <p>GET PROGRAMS LIST</p>
        <form className="form-container" onSubmit={handleGetProgramsList}>
            <input type="submit" value="Submit" />
        </form>

        <hr/>

        <p>GET TAG LIST</p>
        <form className="form-container" onSubmit={handleGetTagList}>
            <label>
                ALL TAGS:
                <input type="checkbox" name="allTags" />
            </label>
            <input type="submit" value="Submit" />
        </form>
    </>
  )
}

export default App
