"""
ログ設定ファイル
処理の進捗と結果を記録
"""

import logging
from datetime import datetime
import os

def setup_logger():
    # logsディレクトリが存在しない場合は作成
    os.makedirs('logs', exist_ok=True)
    
    logger = logging.getLogger('shopify_update')
    logger.setLevel(logging.INFO)
    
    # ファイル出力の設定
    file_handler = logging.FileHandler(f'logs/update_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
    file_handler.setLevel(logging.INFO)
    
    # コンソール出力の設定
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # フォーマットの設定
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger
