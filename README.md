# secpg: Security Playground

情報通信の際に考慮すべき機密性を支える技術について体感するためのパッケージです．

Package for experiencing technologies that support confidentiality considerations during information communication.

## 1 コンテンツ

- 共通鍵暗号方式

  Symmetric Key Encryption Scheme (SKCS)

- 公開鍵暗号方式

  Public Key Crypto System (PKCS)

- HTTPS(now printing...)

- PKI(now printing...)

## 2 動作確認環境

- Python 3.12

## 3 インストール方法

### 3.1 Localへのインストール

  ```bash
  pip install .
  ```

### 3.2 Dockerイメージのビルド

  ```bash
  docker build -t secpg:latest .
  ```

## 4 共通鍵暗号方式

### 4.1 問題設定

- サーバとクライアントの二者がいます

- 両者の間で行われる通信を，第三者からわからないようにしたいです

- 暗号化・複合に際して，お互いに同じ鍵を用います

### 4.2 コマンドライン上における使用方法

- 共通鍵の生成

  ```bash
  secpg genkey random
  ```

- クライアントの起動とメッセージの送信(Run the client then send messages)

  ```bash
  secpg skes client /tmp/random.txt
  ```

- サーバの起動(Run the server)

  ```bash
  secpg skes server /tmp/random.txt
  ```

  下記のような出力が得られます

  ```bash
  encrypted from ('127.0.0.1', 53781):
  b'\xb1\xda\x1d\xf0\x1bU\x85v\x9cC\x9d\xfc\xc2\x99\x9b\xee\x19\xa2\xbe\x90\\\xb9\xf4\x9ar~\xbc%\xa4=\x98\x81\x8c\xf4;\x9e\x99\x06\xc8\x1e0\x89\xb0\x8a?\x8f\x9b\xa9'
  msg from ('127.0.0.1', 53781):
  hello encryption !
  ```

### 4.3 DockerComposeを用いた使用方法

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

## 5 公開鍵暗号方式

### 5.1 問題設定

- サーバとクライアントの二者がいます

- 両者の間で行われる通信を，第三者からわからないようにしたいです

- 暗号化・複合に際して，鍵は以下のように持って使用します

  - クライアントは公開鍵を使って暗号化

  - サーバは秘密鍵を使って複合

### 5.2 コマンドライン上における使用方法

- 公開鍵と秘密鍵の生成

  ```bash
  secpg genkey rsa
  ```

- クライアントの起動とメッセージの送信(Run the client then send messages)

  ```bash
  secpg pkcs client /tmp/rsa_pub.pem

  ```

- サーバの起動(Run the server)

  ```bash
  secpg pkcs server /tmp/rsa.pem
  ```

  下記のような出力が得られます

  ```bash
  encrypted from ('127.0.0.1', 54330):
  b'\xben\xdb\xea\xa6\xb4p\x16\xe7\xbb+\xebmd\xb6\xe3\x7f$\xe6\x06!\xda\x0e\nh\x95ZX\xa9\x01\x83Iz\x1e\x7f\xe0Z\x9cW`\xde\xb1\xd8Cm(\x8f]\x0f\xb1\xbfO\xfa\xa4\xa3\x93\xde\x16\x8b]g\xf6\x1e\x1a\xce\x08\xa6\xe0\x13U\x8e\xfa\n\x04\xf6\xb2\x03kUm\xe1\x18\xa0\xd1\x8d6k\xd7\xd4\x86\xea\xe90V(\xc3v&\xdd9b\x7fF\x92Yi\xedJ\x0b\xbfp\x8a\x88{o\x06\x12e\x96Gd=\xc1\xc4L\xa0\xbe6E\xd2\xea3\xee\xea\x16R\x05j\xc5 \x8f\x980\xf2\x8e\x02\xb4\x1c\xed\x96lO\x94\x1c\xbb)\x1e\xd9\xb3\xf1\xf9\xf0\x0f\xcb\xcbb\x1f\xe6\xc8Z\x9d\xc8\xfc@\x8fH\x97\x8fZ2N\x0f\xcc?\x8a\x01\x0f\x99\xf1?\x05U\x1b\x9d4o\xc9\x85\x8e\xc7b\x1a\x0eZ\xd9T;!\x9d\x0b\xac\xd3\x85\x93L\x0f\'\xb3@\x18\xa8~<\xb6\x0e\x86\xbd\xf8\xcf{mB\x9fZ\x93\xbb\xdf\xd2#\xa2\x99\xafZ\x00v"\xd7\x1bc\xd1\x1au\x1f\xb0=\xb3'
  msg from ('127.0.0.1', 54330):
  hello encryption !
  ```

### 5.3 DockerComposeを用いた使用方法
