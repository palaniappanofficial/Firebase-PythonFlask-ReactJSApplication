import React,{useState,useEffect} from "react";
import './App.css';

function App() {
  const [welcomevariable, welcomefunction] = useState(0);

  useEffect(() => {
    fetch('/palani').then(res => res.json()).then(data => {
      welcomefunction(data.text);

    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">

        Welcome to the Firebase-Flask-React Environment

        <p>{welcomevariable}</p>
      </header>
    </div>
  );
}

export default App;
