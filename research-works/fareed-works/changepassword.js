import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <h1> Settings </h1>
      <h2> Change Password </h2> <br />
      <form>
        <h4>
  <label>
    Current Password:
    <input type="password" name="cpassword" />
  </label> <br /> <br />
  <label>
    New Password:
    <input type="password" name="npassword" />
  </label> <br /> <br />
  <label>
    Confirm Password:
    <input type="password" name="cmpassword" />
    </label>
    </h4> </form>
    </div>
  );
}

export default App;