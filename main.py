from reader import read_xls_csv
from headers import UserAgents
from scraper import Amazon
import time

from writer import GoogleSheet


def work():
    EXCEL_FILE: str = "keywords.xlsx"
    products_to_scrape = read_xls_csv(EXCEL_FILE)
    UA = UserAgents()
    '''
    "sku": row[0],
    "asin": row[1],
    "product_name": row[2],
    "keywords": [row[3], row[4], row[5]]
    '''
    google_sheet = GoogleSheet()
    amzn_products = []
    for product in products_to_scrape:
        ua_header = {
            'User-Agent': UA.getRandomUA()
        }
        keywords = [product["keyword1"], product["keyword2"], product["keyword3"]]
        # print(ua_header)
        for keyword in keywords:
            product_details = Amazon.scrape(asin=product["asin"], product_name=product["product_name"],
                                            keyword=keyword,
                                            headers=ua_header
                                            )
            amzn_products.append(product_details)

    print(amzn_products)
    for amzn_product in amzn_products:
        a = google_sheet.writeLineToSheet(amzn_product)
        print(a)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    work()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
