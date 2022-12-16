import logo from './logo.svg';
import './App.css';
import QR from "./Images/QR.jpg";

function QR() {
  
  return (
    <div className="App">
      <div> <h1> QR code </h1> </div>
      <div>
      <img src= {QR} alt="QR code"/>
      </div>
      <div>
        <h2> <a 
        href={QR} Target="_blank" download> Download QR
        </a> </h2>
      </div>
    </div>
  );
}

export default QR;
