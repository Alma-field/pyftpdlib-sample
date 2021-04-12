# pyftpdlib サンプル

[pyftpdlib](https://github.com/giampaolo/pyftpdlib)を用いたサンプルFTPサーバーを構築します。

## 実行方法

### ライブラリのインストール
pipを使用する方法
```shell
pip install pyftpdlib
```

Gitを使用してGitHubからリポジトリのクローンを作成し、最新の開発バージョンをインストールすることもできます。

```shell
git clone https://github.com/giampaolo/pyftpdlib.git
cd pyftpdlib
pip install .
```

### ユーザーの追加
`users`フォルダーの下にユーザーの設定ファイルを配置します。
(サンプルは`users/user.json.sample`をご覧ください。)  
**設定ファイルの名前は何でも構いません。**  
設定内容

| 項目 | 説明 |
| ---- | ----------- |
| username | ユーザー名を指定します。 |
| password | パスワードを指定します。 |
| rootpath | ユーザーのパスを指定します。<br>(絶対パス) |

## 出典
 - [pyftpdlib](https://github.com/giampaolo/pyftpdlib)
 - [すぐ作ってすぐ壊せるFTPサーバーを立てる (Pythonで)](https://qiita.com/castaneai/items/8cb7cd3253275e7cf617)
