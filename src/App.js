import Navbar from "./components/Navbar";
import Radio from "./components/Radio";

function App() {
  return (
    <div className="flex bg-gray-100">
      <div className="">
        <Navbar />
        <div className="">
          <Radio />
        </div>
      </div>
    </div>
  );
}

export default App;
