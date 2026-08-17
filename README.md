# Task Manager API

大学生向けの課題管理APIです。PythonとFastAPIの学習を兼ねて開発しています。

## 現在の機能

- `GET /`：APIの動作確認メッセージを返す
- `GET /tasks`：サンプルの課題一覧を取得する
- `GET /docs`：APIドキュメントを表示する
- POST /tasks：新しい課題を登録する

## 使用技術

- Python 3.14
- FastAPI
- Uvicorn

## 起動方法

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
fastapi dev main.py
```

起動後、ブラウザで `http://127.0.0.1:8000` を開いてください。