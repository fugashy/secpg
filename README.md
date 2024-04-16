# security_playground

情報通信の際に考慮すべき機密性を支える技術について体感するためのパッケージです．

Package for experiencing technologies that support confidentiality considerations during information communication.

##  コンテンツ

- 共通鍵暗号方式

  Symmetric Key Encryption Scheme (SKCS)

- 公開鍵暗号方式(now printing...)

- HTTPS(now printing...)

- PKI(now printing...)

## 動作確認環境

- Python 3.12

## インストール方法

- Localへのインストール

  ```bash
  pip install .
  ```

- Dockerイメージのビルド

  ```bash
  docker build -t secpg:latest .
  ```

## 共通鍵暗号方式

### 問題設定

- サーバとクライアントの二者がいます

- 両者の間で行われる通信を，第三者からわからないようにしたいです

- 暗号化・複合に際して，お互いに同じ鍵を用います

### コマンドライン上における使用方法

- 共通鍵の生成

  ```bash
  secpg genkey random
  ```

- 受信者の起動(Run the server)

  ```bash
  secpg skes server /tmp/random.txt
  ```

- 送信者の起動とメッセージの送信(Run the client then send messages)

  ```bash
  secpg skes client /tmp/random.txt

  >           msg: hello encryption !
  > encrypted msg: b'\xb1\xda\x1d\xf0\x1bU\x85v\x9cC\x9d\xfc\xc2\x99\x9b\xee\x19\xa2\xbe\x90\\\xb9\xf4\x9ar~\xbc%\xa4=\x98\x81\x8c\xf4;\x9e\x99\x06\xc8\x1e0\x89\xb0\x8a?\x8f\x9b\xa9'
  ```

  送信者を起動したターミナルにて下記のような出力が得られます

  ```bash
  encrypted from ('127.0.0.1', 53781):
  b'\xb1\xda\x1d\xf0\x1bU\x85v\x9cC\x9d\xfc\xc2\x99\x9b\xee\x19\xa2\xbe\x90\\\xb9\xf4\x9ar~\xbc%\xa4=\x98\x81\x8c\xf4;\x9e\x99\x06\xc8\x1e0\x89\xb0\x8a?\x8f\x9b\xa9'
  msg from ('127.0.0.1', 53781):
  hello encryption !
  ```

### DockerComposeを用いた使用方法

- 共通鍵の生成

  ```bash
  secpg genkey random
  ```

- コンテナプロセスの起動

  ```bash
  cd composes/skes
  docker compose up

  > skes-client-1  |           msg: hello encryption !
  > skes-client-1  | encrypted msg: b'\x13e\xf3A\xb4\xbe\xd4M<\x045\\cifH\xf2#\xa9\xe8|k\xb5\x1a\x9d\x9f\x07\xee\xce\x13\x99\xd9\xfe\xeftz\xc4\xe5\xf6w\xb1\x1e\xd4\xa9\x9b\xeaTk'
  > ...
  > skes-server-1  | encrypted from ('172.16.111.3', 57481):
  > skes-server-1  | b'\x99\xd7\x17\xeb\xf6<}x\xac\xe65_]\xd9\x03\x88\xf6\xca\xd7\xef<\x04\xe4`\xbe$&`;\xd1\xd1\xb8C\x99\x88>\xf5~\x0e\xa7hf\x04\xb4\x8b\x98U\xae'
  > skes-server-1  | msg from ('172.16.111.3', 57481):
  > skes-server-1  | hello encryption !
  > ...
  ```
