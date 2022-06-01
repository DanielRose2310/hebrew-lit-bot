import { useEffect } from 'react';
import './App.css';

function App() {
useEffect(() => {
  const goGetIt = async () => {
    const response = await fetch(process.env.REACT_APP_BACKEND_URL+'brenner', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    });
    const myJson = await response.json(); //extract JSON from the http response
    // do something with myJson
    console.log(myJson)
    
  }
  goGetIt()

}, [])

  
  return (
    <div className="App">
      <header className="App-header">
  
      </header>
    </div>
  );
}

export default App;
