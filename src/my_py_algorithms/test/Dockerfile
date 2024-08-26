# ベースイメージとしてpython:3.11を使用
FROM python:3.11

# 作業ディレクトリを設定
WORKDIR /app

# 必要なPythonライブラリをインストールするためのrequirements.txtファイルをコピー
COPY requirements.txt .

# Pythonライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# コンテナ実行時に実行するコマンド
CMD ["python", "main.py"]