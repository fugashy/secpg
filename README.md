# security_playground

情報通信の際に考慮すべき機密性を支える技術について体感するためのパッケージです．

Package for experiencing technologies that support confidentiality considerations during information communication.

##  コンテンツ(予定)

- 共通鍵暗号方式

- 公開鍵暗号方式

- HTTPS

- PKI

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
  openssl rand -base64 32 > key.txt
  ```

- 送信者の起動

  一定周期でメッセージを受信者に送信します

  ```bash
  secpg aes send --ipaddr 127.0.0.1 --port 48273
  ```

- 受信者の起動

  受信したメッセージを表示します

  ```bash
  secpg aes recv --port 48273
  ```
