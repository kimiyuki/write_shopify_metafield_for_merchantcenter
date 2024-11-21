"""
メインスクリプト
Shopify商品のバリエーションメタフィールドを更新
"""

import shopify
import time
from config import *
from logger import setup_logger
import argparse

def init_shopify():
    """Shopify APIの初期化"""
    shop_url = f"https://{SHOP_URL}/admin/api/{API_VERSION}"
    shopify.ShopifyResource.set_site(shop_url)
    shopify.ShopifyResource.set_headers({'X-Shopify-Access-Token': ACCESS_TOKEN})

def get_products_from_collection(collection_id, limit=50, since_id=0, logger=None):
    """
    コレクションから商品を取得
    
    Args:
        collection_id (int): コレクションID
        limit (int): 1回のリクエストで取得する商品数
        since_id (int): この ID 以降の商品を取得
        logger (Logger): ロガーインスタンス
    """
    try:
        products = shopify.Product.find(
            collection_id=collection_id,
            limit=limit,
            since_id=since_id,
            status='active'
        )
        return products
    except Exception as e:
        logger.error(f"Error fetching products: {str(e)}")
        return []

def update_variant_metafield(variant, logger):
    """バリエーションのメタフィールドを更新"""
    try:
        metafield = shopify.Metafield({
            'namespace': 'mm-google-shopping',
            'key': 'custom_label_0',
            'value': METAFIELD_VALUE,
            'type': 'single_line_text_field'
        })
        variant.add_metafield(metafield)
        return True
    except Exception as e:
        logger.error(f"Error updating variant {variant.id}: {str(e)}")
        return False

def main(test_mode=True):
    logger = setup_logger()
    logger.info("Starting metafield update process")
    
    init_shopify()
    
    total_products = 0
    total_variants = 0
    success_variants = 0
    
    try:
        # 最初のページを取得
        products = shopify.Product.find(collection_id=COLLECTION_ID, limit=BATCH_SIZE)
        
        while True:
            if not products:
                break
                
            for product in products:
                total_products += 1
                logger.info(f"Processing product {product.id}: {product.title}")
                
                for variant in product.variants:
                    total_variants += 1
                    if update_variant_metafield(variant, logger):
                        success_variants += 1
                        logger.info(f"Updated variant {variant.id}")
                    
                    time.sleep(0.5)  # API制限を考慮
                
                if test_mode and total_products >= 1:
                    logger.info("Test mode completed")
                    break
            
            if test_mode and total_products >= 1:
                break
                
            # 次のページがあれば取得
            if products.has_next_page():
                products = products.next_page()
            else:
                break
    
    except Exception as e:
        logger.error(f"Error in main process: {str(e)}")
    
    logger.info(f"""
    Process completed:
    Total products processed: {total_products}
    Total variants processed: {total_variants}
    Successful updates: {success_variants}
    Failed updates: {total_variants - success_variants}
    """)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update Shopify variant metafields')
    parser.add_argument('--prod', action='store_true', help='Run in production mode')
    args = parser.parse_args()
    
    main(test_mode=not args.prod)
