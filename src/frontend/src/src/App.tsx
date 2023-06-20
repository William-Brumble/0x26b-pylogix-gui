import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

    const test = async ()=> {
      const response = await fetch('/do/stuff', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({
              token: window.pywebview.token
          }),
          cache: 'default'
      })
        console.log(response);
    }

  return (
    <>
      <div>
          <button type="button" onClick={test}>Test Fetch!</button>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
