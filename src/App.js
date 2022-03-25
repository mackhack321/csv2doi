import { Router } from "@reach/router";
import Help from "./components/Help";
import Navbar from "./components/Navbar";
import Radio from "./components/Radio";

function App() {
  return (
    <div className="h-screen bg-gray-100">
      <div className="">
        <Navbar />
        <div className="">
          <Router primary={false}>
            <Radio path="/" default />
            <Help path="help" />
          </Router>
        </div>
      </div>
    </div>
  );
}

export default App;
