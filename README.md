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

```bash
pip install .
```

## 共通鍵暗号方式

### 問題設定

- サーバとクライアントの二者がいます

- 両者の間で行われる通信を，第三者からわからないようにしたいです

- 暗号化・複合に際して，お互いに同じ鍵を用います

### 使用方法

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
