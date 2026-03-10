import sqlite3
from pathlib import Path
from typing import Optional

DB_PATH = Path(__file__).resolve().parents[2] / "lifepath.db"


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS journal_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            text_masked TEXT NOT NULL,
            raw_hash TEXT NOT NULL,
            mood TEXT,
            goal TEXT,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS audit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            action TEXT NOT NULL,
            privacy_proof TEXT,
            payload_hash TEXT,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """
    )

    conn.commit()
    conn.close()


def create_user(email: str, password_hash: str) -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (email, password_hash) VALUES (?, ?)", (email, password_hash))
    conn.commit()
    user_id = cur.lastrowid
    conn.close()
    return int(user_id)


def get_user_by_email(email: str) -> Optional[dict]:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = ?", (email,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def get_user_by_id(user_id: int) -> Optional[dict]:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def create_journal_entry(user_id: int, text_masked: str, raw_hash: str, mood: Optional[str], goal: Optional[str]) -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO journal_entries (user_id, text_masked, raw_hash, mood, goal) VALUES (?, ?, ?, ?, ?)",
        (user_id, text_masked, raw_hash, mood, goal),
    )
    conn.commit()
    row_id = cur.lastrowid
    conn.close()
    return int(row_id)


def list_journal_entries(user_id: int, limit: int = 20, offset: int = 0) -> list[dict]:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, text_masked, mood, goal, created_at FROM journal_entries WHERE user_id = ? ORDER BY id DESC LIMIT ? OFFSET ?",
        (user_id, limit, offset),
    )
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def count_journal_entries(user_id: int) -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(1) as cnt FROM journal_entries WHERE user_id = ?", (user_id,))
    row = cur.fetchone()
    conn.close()
    return int(row["cnt"]) if row else 0


def create_audit_log(user_id: Optional[int], action: str, privacy_proof: Optional[str], payload_hash: Optional[str]) -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO audit_logs (user_id, action, privacy_proof, payload_hash) VALUES (?, ?, ?, ?)",
        (user_id, action, privacy_proof, payload_hash),
    )
    conn.commit()
    row_id = cur.lastrowid
    conn.close()
    return int(row_id)
