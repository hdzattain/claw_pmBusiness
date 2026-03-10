import { useEffect, useMemo, useState } from "react";

type JournalItem = { id: number; text_masked: string; mood?: string; goal?: string; created_at: string };
type JournalPagination = { limit: number; offset: number; total: number; has_more: boolean };
type TaskItem = { id: string; title: string; done: boolean };

const API = "http://localhost:8000";
const PAGE_SIZE = 10;

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
  const [pagination, setPagination] = useState<JournalPagination | null>(null);

  const [boardInput, setBoardInput] = useState("");
  const [showGuide, setShowGuide] = useState(() => localStorage.getItem("lifepath_hide_guide") !== "1");
  const [tasks, setTasks] = useState<TaskItem[]>(() => {
    try {
      const raw = localStorage.getItem("lifepath_tasks");
      return raw ? JSON.parse(raw) : [];
    } catch {
      return [];
    }
  });

  const [msg, setMsg] = useState("");
  const [authLoading, setAuthLoading] = useState(false);
  const [morningLoading, setMorningLoading] = useState(false);
  const [eveningLoading, setEveningLoading] = useState(false);
  const [journalLoading, setJournalLoading] = useState(false);

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
    void loadJournal({ tokenValue: token, offset: 0, append: false });
  }, [token]);

  useEffect(() => {
    localStorage.setItem("lifepath_tasks", JSON.stringify(tasks));
  }, [tasks]);

  async function parseJsonSafe(res: Response) {
    try {
      return await res.json();
    } catch {
      return null;
    }
  }

  function getErrorMessage(data: any, fallback: string) {
    return data?.error?.message || data?.detail || fallback;
  }

  function formatTime(ts: string) {
    const d = new Date(ts);
    if (Number.isNaN(d.getTime())) return ts;
    return d.toLocaleString("zh-CN", { hour12: false });
  }

  function validateAuthForm() {
    if (!email.trim()) return "请输入邮箱";
    if (password.length < 8) return "密码至少8位";
    return "";
  }

  async function authSubmit() {
    const validationMsg = validateAuthForm();
    if (validationMsg) {
      setMsg(validationMsg);
      return;
    }

    setMsg("");
    setAuthLoading(true);
    const endpoint = mode === "register" ? "/api/auth/register" : "/api/auth/login";

    try {
      const res = await fetch(`${API}${endpoint}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: email.trim(), password }),
      });
      const data = await parseJsonSafe(res);
      if (!res.ok || !data?.success) {
        setMsg(getErrorMessage(data, "认证失败"));
        return;
      }
      setToken(data.token);
      setMsg("登录成功");
    } catch {
      setMsg("网络异常，请稍后再试");
    } finally {
      setAuthLoading(false);
    }
  }

  async function submitMorning() {
    if (!text.trim()) {
      setMsg("请先输入今日问题");
      return;
    }

    setMsg("");
    setMorningLoading(true);

    try {
      const res = await fetch(`${API}/api/advice/morning`, {
        method: "POST",
        headers: authHeaders,
        body: JSON.stringify({ text: text.trim(), mood: mood.trim(), goal: goal.trim() }),
      });
      const data = await parseJsonSafe(res);

      if (res.status === 401) {
        setMsg("登录已过期，请重新登录");
        logout();
        return;
      }

      if (!res.ok || !data?.success) {
        setMsg(getErrorMessage(data, "请求失败"));
        return;
      }

      setMorningResult(data.today_action);
      setText("");
      await loadJournal({ tokenValue: token, offset: 0, append: false });
    } catch {
      setMsg("网络异常，请稍后再试");
    } finally {
      setMorningLoading(false);
    }
  }

  async function submitEvening() {
    if (!wins.trim() || !blockers.trim() || !nextAction.trim()) {
      setMsg("请完整填写晚间复盘三项");
      return;
    }

    setMsg("");
    setEveningLoading(true);

    try {
      const res = await fetch(`${API}/api/advice/evening`, {
        method: "POST",
        headers: authHeaders,
        body: JSON.stringify({ wins: wins.trim(), blockers: blockers.trim(), next_action: nextAction.trim() }),
      });
      const data = await parseJsonSafe(res);

      if (res.status === 401) {
        setMsg("登录已过期，请重新登录");
        logout();
        return;
      }

      if (!res.ok || !data?.success) {
        setMsg(getErrorMessage(data, "请求失败"));
        return;
      }

      setEveningResult(data.review);
      setWins("");
      setBlockers("");
      setNextAction("");
      await loadJournal({ tokenValue: token, offset: 0, append: false });
    } catch {
      setMsg("网络异常，请稍后再试");
    } finally {
      setEveningLoading(false);
    }
  }

  async function loadJournal({ tokenValue, offset, append }: { tokenValue: string; offset: number; append: boolean }) {
    setJournalLoading(true);
    try {
      const res = await fetch(`${API}/api/advice/journal?limit=${PAGE_SIZE}&offset=${offset}`, {
        headers: { Authorization: `Bearer ${tokenValue}` },
      });
      const data = await parseJsonSafe(res);

      if (res.status === 401) {
        setMsg("登录已过期，请重新登录");
        logout();
        return;
      }

      if (!data?.success) {
        setMsg(getErrorMessage(data, "加载记录失败"));
        return;
      }

      setJournal((prev) => (append ? [...prev, ...(data.items || [])] : data.items || []));
      setPagination(data.pagination || null);
    } finally {
      setJournalLoading(false);
    }
  }

  function addTask() {
    const title = boardInput.trim();
    if (!title) {
      setMsg("请输入任务内容");
      return;
    }
    setTasks((prev) => [{ id: `${Date.now()}`, title, done: false }, ...prev]);
    setBoardInput("");
  }

  function closeGuideForever() {
    localStorage.setItem("lifepath_hide_guide", "1");
    setShowGuide(false);
  }

  function toggleTask(taskId: string) {
    setTasks((prev) => prev.map((t) => (t.id === taskId ? { ...t, done: !t.done } : t)));
  }

  function deleteTask(taskId: string) {
    setTasks((prev) => prev.filter((t) => t.id !== taskId));
  }

  function logout() {
    localStorage.removeItem("lifepath_token");
    setToken("");
    setJournal([]);
    setPagination(null);
  }

  if (!token) {
    return (
      <main className="wrap">
        <h1>仙人指路 · LifePath AI</h1>
        <p className="sub">Onboarding：先登录，再开始每日路径建议</p>
        <div className="tabs">
          <button className={mode === "register" ? "active" : ""} onClick={() => setMode("register")}>
            注册
          </button>
          <button className={mode === "login" ? "active" : ""} onClick={() => setMode("login")}>
            登录
          </button>
        </div>
        <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="邮箱" />
        <input value={password} onChange={(e) => setPassword(e.target.value)} placeholder="密码（至少8位）" type="password" />
        <button onClick={authSubmit} disabled={authLoading}>
          {authLoading ? "处理中..." : mode === "register" ? "创建账号" : "登录"}
        </button>
        {msg && <p className="msg">{msg}</p>}
      </main>
    );
  }

  return (
    <main className="wrap">
      <h1>仙人指路 · LifePath AI</h1>
      <p className="sub">晨间建议 + 晚间复盘（Phase 2）</p>

      {showGuide && (
        <section className="panel guide">
          <div className="panel-head">
            <h3>新手引导（看完1分钟就会用）</h3>
            <button className="secondary" onClick={closeGuideForever}>我知道了</button>
          </div>
          <ol className="guide-list">
            <li><b>第一步：晨间建议</b> —— 在“今天最困扰的问题”里写一句话，点“生成晨间建议”。</li>
            <li><b>第二步：执行任务</b> —— 把建议拆成1~3个小任务，放到“今日任务看板”。</li>
            <li><b>第三步：晚间复盘</b> —— 晚上填“完成了什么 / 卡在哪里 / 明早先做什么”。</li>
            <li><b>第四步：看记录</b> —— 在“最近记录”里回看自己连续进步。</li>
          </ol>
          <p className="sub">小技巧：每次只做一个25分钟小动作，最容易坚持。</p>
        </section>
      )}

      <section className="panel">
        <h3>晨间：今日最优行动</h3>
        <textarea value={text} onChange={(e) => setText(e.target.value)} placeholder="今天最困扰的问题" />
        <input value={mood} onChange={(e) => setMood(e.target.value)} placeholder="心情（可选）" />
        <input value={goal} onChange={(e) => setGoal(e.target.value)} placeholder="目标（可选）" />
        <button onClick={submitMorning} disabled={morningLoading}>
          {morningLoading ? "生成中..." : "生成晨间建议"}
        </button>
        {morningResult && <div className="card">{morningResult}</div>}
      </section>

      <section className="panel">
        <h3>晚间：复盘总结</h3>
        <input value={wins} onChange={(e) => setWins(e.target.value)} placeholder="今天完成了什么" />
        <input value={blockers} onChange={(e) => setBlockers(e.target.value)} placeholder="主要阻塞" />
        <input value={nextAction} onChange={(e) => setNextAction(e.target.value)} placeholder="明日第一动作" />
        <button onClick={submitEvening} disabled={eveningLoading}>
          {eveningLoading ? "生成中..." : "生成晚间复盘"}
        </button>
        {eveningResult && <pre className="card pre">{eveningResult}</pre>}
      </section>

      <section className="panel">
        <h3>今日任务看板</h3>
        <div className="task-input-row">
          <input value={boardInput} onChange={(e) => setBoardInput(e.target.value)} placeholder="添加一个今日任务（如：完善登录页提示）" />
          <button className="secondary" onClick={addTask}>添加</button>
        </div>
        {tasks.length === 0 ? (
          <div className="empty">还没有任务，先添加一条今天最关键的动作。</div>
        ) : (
          <ul>
            {tasks.map((t) => (
              <li key={t.id} className="task-item">
                <label>
                  <input type="checkbox" checked={t.done} onChange={() => toggleTask(t.id)} />
                  <span className={t.done ? "done" : ""}>{t.title}</span>
                </label>
                <button className="danger" onClick={() => deleteTask(t.id)}>删除</button>
              </li>
            ))}
          </ul>
        )}
      </section>

      <section className="panel">
        <div className="panel-head">
          <h3>最近记录（脱敏）</h3>
          <button onClick={logout}>退出</button>
        </div>
        {!journalLoading && journal.length === 0 ? (
          <div className="empty">还没有记录，先完成一次晨间建议或晚间复盘吧。</div>
        ) : (
          <ul>
            {journal.map((j) => (
              <li key={j.id}>
                <p>{j.text_masked}</p>
                <small>{formatTime(j.created_at)}</small>
              </li>
            ))}
          </ul>
        )}

        {pagination && (
          <div className="more-wrap">
            <small>
              已显示 {journal.length} / {pagination.total}
            </small>
            {pagination.has_more && (
              <button
                className="secondary"
                disabled={journalLoading}
                onClick={() =>
                  loadJournal({
                    tokenValue: token,
                    offset: journal.length,
                    append: true,
                  })
                }
              >
                {journalLoading ? "加载中..." : "加载更多"}
              </button>
            )}
          </div>
        )}
      </section>

      {msg && <p className="msg">{msg}</p>}
    </main>
  );
}
