import { useState } from "react";

function Test() {
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [response, setResponse] = useState("no response yet");

  const handleSubmit = async (e) => {
    e.preventDefault();
    let res = await fetch("http://localhost:5000/greeter", {
      method: "POST",
      mode: "cors",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: name,
        age: age,
      }),
    });

    let json = await res.json();
    setResponse(json.response);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={name}
          placeholder="Name"
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="text"
          value={age}
          placeholder="age"
          onChange={(e) => setAge(e.target.value)}
        />

        <button type="submit">Greet me</button>

        <p>{response}</p>
      </form>
    </div>
  );
}

export default Test;
