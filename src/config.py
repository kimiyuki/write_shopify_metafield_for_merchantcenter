"""
設定ファイル
Shopifyの認証情報や定数を管理
"""
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

SHOP_URL = os.getenv('SHOP_URL')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
API_VERSION = os.getenv('API_VERSION', '2024-10')

# 更新対象の設定
COLLECTION_ID = os.getenv('COLLECTION_ID')
METAFIELD_VALUE = os.getenv('METAFIELD_VALUE')
BATCH_SIZE = int(os.getenv('BATCH_SIZE', '50'))