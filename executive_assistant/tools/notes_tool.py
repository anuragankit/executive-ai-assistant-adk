import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "orion_memory.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            note TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


init_db()


def remember_note(note: str) -> str:
    """
    Stores an important note permanently.
    """

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO notes (note) VALUES (?)",
        (note,)
    )

    conn.commit()
    conn.close()

    return f"I'll remember this: {note}"


def recall_notes() -> str:
    """
    Returns all remembered notes.
    """

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT note FROM notes"
    )

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return "I don't remember anything yet."

    result = "\n".join(
        f"• {row[0]}" for row in rows
    )

    return result