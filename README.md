# Shopify バリエーション メタフィールド更新ツール

## 概要
Shopify商品のバリエーションに対して、Google Shopping用のメタフィールドを一括で更新するツールです。

## 前提条件
- Python 3.8以上
- Shopify Admin API アクセス権限
  - `write_products`
  - `write_product_listings`
  - `write_metaobjects`
  - `write_metaobject_definitions`

## 設定
- `src/config.py` ファイルを編集して、Shopifyの認証情報や定数を設定します。


## 使用方法

### テストモード（1商品のみ処理）
```bash
python src/main.py
```
### 本番モード（全商品を処理）
```bash
python src/main.py --prod
```

## メタフィールド仕様
- namespace: `mm-google-shopping`
- key: `custom_label_0`
- type: `single_line_text_field`

## ログ
実行ログは `logs/` ディレクトリに出力されます。
- 処理された商品数
- 更新されたバリエーション数
- エラー情報（発生時）

## 注意事項
- 本番モードで実行する前に、必ずテストモードで動作確認を行ってください
- Shopify API制限に注意してください
- 大量の商品を処理する場合は、時間がかかる可能性があります

## トラブルシューティング
エラーが発生した場合は、ログファイルを確認してください。主な対処方法：
1. API権限の確認
2. アクセストークンの有効性確認
3. ネットワーク接続の確認
