import { useState } from "react";

export function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState<string>("");

  async function submit() {
    const res = await fetch("http://localhost:8000/api/advice/daily", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
    const data = await res.json();
    setResult(data?.today_action || "No suggestion yet");
  }

  return (
    <main className="wrap">
      <h1>???? ? LifePath AI</h1>
      <p className="sub">??????????????????MVP?</p>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="???????????????????????..."
      />
      <button onClick={submit}>??????</button>
      {result && <section className="card">{result}</section>}
    </main>
  );
}
