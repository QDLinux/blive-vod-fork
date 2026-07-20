"""Native UI for the packaged application, which runs without a console."""

import queue
import logging
import sys
import threading
import tkinter as tk
from tkinter import messagebox, simpledialog


class _UiWriter:
    def __init__(self, app):
        self.app = app

    def write(self, text):
        if text:
            self.app.log(text)

    def flush(self):
        pass


class AppUi:
    def __init__(self):
        self._calls = queue.Queue()
        self._ready = threading.Event()
        self._root = None
        self._text = None
        threading.Thread(target=self._run, daemon=True).start()
        self._ready.wait(timeout=5)

    def _run(self):
        self._root = tk.Tk()
        self._root.title("B站直播点歌机")
        self._root.geometry("700x430")
        self._root.minsize(520, 320)
        self._root.protocol("WM_DELETE_WINDOW", self._on_close)
        frame = tk.Frame(self._root, padx=12, pady=12)
        frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(frame, text="B站直播点歌机", font=("Segoe UI", 14, "bold")).pack(anchor=tk.W)
        tk.Label(frame, text="后台监听正在运行，登录二维码会在浏览器中打开。", fg="#555").pack(anchor=tk.W, pady=(3, 8))
        self._text = tk.Text(frame, state=tk.DISABLED, wrap=tk.WORD, font=("Consolas", 10))
        self._text.pack(fill=tk.BOTH, expand=True)
        self._ready.set()
        self._root.after(50, self._process_calls)
        self._root.mainloop()

    def _process_calls(self):
        while True:
            try:
                fn, args, kwargs, result, done = self._calls.get_nowait()
            except queue.Empty:
                break
            try:
                result.append((True, fn(*args, **kwargs)))
            except Exception as exc:
                result.append((False, exc))
            finally:
                if done is not None:
                    done.set()
        if self._root is not None:
            self._root.after(50, self._process_calls)

    def _call(self, fn, *args, **kwargs):
        result = []
        done = threading.Event()
        self._calls.put((fn, args, kwargs, result, done))
        done.wait()
        ok, value = result[0]
        if not ok:
            raise value
        return value

    def log(self, text):
        self._calls.put((self._append_log, (str(text),), {}, [], None))

    def _append_log(self, message):
        if self._text is not None:
            self._text.configure(state=tk.NORMAL)
            self._text.insert(tk.END, message)
            self._text.see(tk.END)
            self._text.configure(state=tk.DISABLED)

    def ask_string(self, title, prompt):
        return self._call(simpledialog.askstring, title, prompt, parent=self._root)

    def ask_yes_no(self, title, prompt):
        return self._call(messagebox.askyesno, title, prompt, parent=self._root)

    def _on_close(self):
        self._root.destroy()
        # The asyncio listener runs on the main thread, so closing the UI must
        # end the process instead of leaving a windowless listener behind.
        import os
        os._exit(0)


def start_ui():
    app = AppUi()
    class _QuietUnknownCommand(logging.Filter):
        def filter(self, record):
            return not (
                record.name == "blivedm"
                and record.levelno < logging.ERROR
                and "unknown cmd=" in record.getMessage()
            )

    logging.getLogger("blivedm").addFilter(_QuietUnknownCommand())
    sys.stdout = _UiWriter(app)
    sys.stderr = _UiWriter(app)
    return app
