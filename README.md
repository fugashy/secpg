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

- 公開鍵と秘密鍵の生成

  ```bash
  secpg genkey rsa
  ```

- コンテナプロセスの起動

  ```bash
  cd composes/skes
  docker compose up

  > pkcs-client-1  |           msg: hello encryption !
  > pkcs-client-1  | encrypted msg: b'\x970^n\x84\x91\x17\x0eB\xaaJ\x0c\xb3\xe7i\x08\xd9%2Mm\xae\xa7\x06VN:pC\x0e\xfe\xef\x84~]\x8f\xd8[\x9b\xe2.\xfc\xf3\n\xd6\xd3.\xad\r\xbd\xe8?S\xa3\x14`\x18G\xf2\xc5#\xbe\x97\xf3\xc8\xd7\xc7-\xedw\x84j\xff\xf6\xcby\xd5\xc0\x1c\x8e\xa8>\xc6\x0f[\xb6HX\xcd\x9ak\xcd1\x80\x1c\xd8~\x95\xfdq\xbc\xfd\xc8\t\x15\x07\xc9\xe2\x1e\xf3\x19\xda9\x1dl\xa2\xe9\xb7\x07\xf7a\xe4\x98\xa1\xafN\x15&/G\xc4\xee\xc3\xeb\x97v\x8a\xb1\x15e4\xc6\x80\x17)\x18\x96\x94\x9b\xcc{\x97\xe0 \x82\x00\xef\xd6`\xb3\xcfe\xf2\x94\x9a+=\xf9x\xae\xcb\xb4\x97\x81@b\xd2\xa2C/\x0b\xea\x8e\xff\x922\xc7\xd94O\xc3*\x05.\xb7MZ1P\x8c\x03\xf3p\x1f\xfd\x1b;S\x86\xd6\x07\xdc\xd9\xb2\x910\xbf`}{\xa3\xcb\x1a"\xabk\x1b\xe0{\x90(\xd4&\t\xc0\xbb\xb1C\x13u-8\xde\x88\xb7t\xf2b\'\x14\xa3\x01.y8"'
  ...
  > pkcs-server-1  | msg from ('172.16.112.3', 56545):
  > pkcs-server-1  | hello encryption !
  > pkcs-server-1  | encrypted from ('172.16.112.3', 56545):
  > pkcs-server-1  | b"\xa1\xc2$\xb6o\xa4\t\xda\xd8\xa9\x08\x07\xc1\xd6,\x08\xd0\xbd\x1e1\\H\x00\xcdb'b\xdd@\x08\xd1-\x02\xb7\x95\xe3P\xe8Cs4\xa4\xb9T\xeft\xf5.T\xce(\xff\xc63.\xfe<\xb1\xa9,\xd8\xbf\xed\xe5\xf6z\xbf>\x93\x95\xee\xeb\xca\xcd\xd8Z\xbb\xf2\xc8\xcd\xfc\xe2\x0b\xd3\xa7<\xd5\xfe$%\x1cZ?\xaf\x8b\xe6\xaf\xd7\x1ai\xda\xd9\xe2\x84\n\xcfRp\x1c*\xca\x8f\xe5;rQ!\xb5O\x8a\x0bR\x00[\xa8\xf8\x9di\x86e\x93k\x89\x97\xb5\xc7,AS7/\x1ad\x1e\xb6l\x12.\xafL\x88\xab\xfc\xd1\x89\x15\x1a\t\x8c\x8f-t\xe2\xe3<\xa0`4\xca\xe5\xa3\\J!\xfb\x1d\x13g\xdd:cs\xb3\xfb.\xa0\x95\x00eU\x96\xf10o\xcdn\xd6\xa0\xb3\x1e\xb9A\xa2\x8f\xa1\xb8\xf8W{\xb0\x902\x07\xd6\x9cV\xb7-g\xb9\xb9\x9c\x92Q\xc9\xf6\xcbJB\xfb\xeb8z\n\xdb\xae\x18i\xbe\xe9]zY/\xc6\x82\x9a\xf7]F\xcb\x11_\x1b6<"
  ...
  ```
