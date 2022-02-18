import { Router } from "@reach/router";
import About from "./components/About";
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
            <About path="about" />
          </Router>
        </div>
      </div>
    </div>
  );
}

export default App;
