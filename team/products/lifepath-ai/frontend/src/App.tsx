import { useEffect, useMemo, useState } from "react";

type User = { id: number; email: string };
type JournalItem = { id: number; text_masked: string; mood?: string; goal?: string; created_at: string };

const API = "http://localhost:8000";

export function App() {
  const [mode, setMode] = useState<"login" | "register">("register");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [token, setToken] = useState(localStorage.getItem("lifepath_token") || "");
  const [user, setUser] = useState<User | null>(null);

  const [text, setText] = useState("");
  const [mood, setMood] = useState("");
  const [goal, setGoal] = useState("");
  const [result, setResult] = useState("");
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
    setUser(data.user);
    setMsg("登录成功");
  }

  async function submitAdvice() {
    setMsg("");
    const res = await fetch(`${API}/api/advice/daily`, {
      method: "POST",
      headers: authHeaders,
      body: JSON.stringify({ text, mood, goal }),
    });
    const data = await res.json();
    if (!res.ok || !data?.success) {
      setMsg(data?.detail || "请求失败");
      return;
    }
    setResult(data.today_action);
    await loadJournal(token);
  }

  async function loadJournal(currentToken: string) {
    const res = await fetch(`${API}/api/advice/journal`, {
      headers: {
        Authorization: `Bearer ${currentToken}`,
      },
    });
    const data = await res.json();
    if (data?.success) setJournal(data.items || []);
  }

  function logout() {
    localStorage.removeItem("lifepath_token");
    setToken("");
    setUser(null);
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
      <p className="sub">输入困扰，生成今日最优行动建议</p>

      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="例如：我在考虑转行产品经理，但不知道从哪里开始..."
      />
      <input value={mood} onChange={(e) => setMood(e.target.value)} placeholder="心情（可选）" />
      <input value={goal} onChange={(e) => setGoal(e.target.value)} placeholder="目标（可选）" />
      <button onClick={submitAdvice}>生成今日建议</button>

      {result && <section className="card">{result}</section>}

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
