import { useEffect, useMemo, useState } from "react";

type User = { id: number; email: string };
type JournalItem = { id: number; text_masked: string; mood?: string; goal?: string; created_at: string };

const API = "http://localhost:8000";

export function App() {
  const [mode, setMode] = useState<"login" | "register">("register");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [token, setToken] = useState(localStorage.getItem("lifepath_token") || "");

  const [text, setText] = useState("");
  const [mood, setMood] = useState("");
  const [goal, setGoal] = useState("");
  const [morningResult, setMorningResult] = useState("");

  const [wins, setWins] = useState("");
  const [blockers, setBlockers] = useState("");
  const [nextAction, setNextAction] = useState("");
  const [eveningResult, setEveningResult] = useState("");

  const [journal, setJournal] = useState<JournalItem[]>([]);
  const [msg, setMsg] = useState("");

  const authHeaders = useMemo(
    () => ({
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    }),
    [token]
  );

  useEffect(() => {
    if (!token) return;
    localStorage.setItem("lifepath_token", token);
    loadJournal(token);
  }, [token]);

  async function authSubmit() {
    setMsg("");
    const endpoint = mode === "register" ? "/api/auth/register" : "/api/auth/login";
    const res = await fetch(`${API}${endpoint}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });
    const data = await res.json();
    if (!res.ok || !data?.success) {
      setMsg(data?.detail || "认证失败");
      return;
    }
    setToken(data.token);
    setMsg("登录成功");
  }

  async function submitMorning() {
    setMsg("");
    const res = await fetch(`${API}/api/advice/morning`, {
      method: "POST",
      headers: authHeaders,
      body: JSON.stringify({ text, mood, goal }),
    });
    const data = await res.json();
    if (!res.ok || !data?.success) {
      setMsg(data?.detail || "请求失败");
      return;
    }
    setMorningResult(data.today_action);
    await loadJournal(token);
  }

  async function submitEvening() {
    setMsg("");
    const res = await fetch(`${API}/api/advice/evening`, {
      method: "POST",
      headers: authHeaders,
      body: JSON.stringify({ wins, blockers, next_action: nextAction }),
    });
    const data = await res.json();
    if (!res.ok || !data?.success) {
      setMsg(data?.detail || "请求失败");
      return;
    }
    setEveningResult(data.review);
    await loadJournal(token);
  }

  async function loadJournal(currentToken: string) {
    const res = await fetch(`${API}/api/advice/journal`, {
      headers: { Authorization: `Bearer ${currentToken}` },
    });
    const data = await res.json();
    if (data?.success) setJournal(data.items || []);
  }

  function logout() {
    localStorage.removeItem("lifepath_token");
    setToken("");
    setJournal([]);
  }

  if (!token) {
    return (
      <main className="wrap">
        <h1>仙人指路 · LifePath AI</h1>
        <p className="sub">Onboarding：先登录，再开始每日路径建议</p>
        <div className="tabs">
          <button className={mode === "register" ? "active" : ""} onClick={() => setMode("register")}>注册</button>
          <button className={mode === "login" ? "active" : ""} onClick={() => setMode("login")}>登录</button>
        </div>
        <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="邮箱" />
        <input value={password} onChange={(e) => setPassword(e.target.value)} placeholder="密码（至少8位）" type="password" />
        <button onClick={authSubmit}>{mode === "register" ? "创建账号" : "登录"}</button>
        {msg && <p className="msg">{msg}</p>}
      </main>
    );
  }

  return (
    <main className="wrap">
      <h1>仙人指路 · LifePath AI</h1>
      <p className="sub">晨间建议 + 晚间复盘（Phase 2）</p>

      <section className="panel">
        <h3>晨间：今日最优行动</h3>
        <textarea value={text} onChange={(e) => setText(e.target.value)} placeholder="今天最困扰的问题" />
        <input value={mood} onChange={(e) => setMood(e.target.value)} placeholder="心情（可选）" />
        <input value={goal} onChange={(e) => setGoal(e.target.value)} placeholder="目标（可选）" />
        <button onClick={submitMorning}>生成晨间建议</button>
        {morningResult && <div className="card">{morningResult}</div>}
      </section>

      <section className="panel">
        <h3>晚间：复盘总结</h3>
        <input value={wins} onChange={(e) => setWins(e.target.value)} placeholder="今天完成了什么" />
        <input value={blockers} onChange={(e) => setBlockers(e.target.value)} placeholder="主要阻塞" />
        <input value={nextAction} onChange={(e) => setNextAction(e.target.value)} placeholder="明日第一动作" />
        <button onClick={submitEvening}>生成晚间复盘</button>
        {eveningResult && <pre className="card pre">{eveningResult}</pre>}
      </section>

      <section className="panel">
        <div className="panel-head">
          <h3>最近记录（脱敏）</h3>
          <button onClick={logout}>退出</button>
        </div>
        <ul>
          {journal.map((j) => (
            <li key={j.id}>
              <p>{j.text_masked}</p>
              <small>{j.created_at}</small>
            </li>
          ))}
        </ul>
      </section>

      {msg && <p className="msg">{msg}</p>}
    </main>
  );
}
