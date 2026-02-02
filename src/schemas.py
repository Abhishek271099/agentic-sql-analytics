from pydantic import BaseModel

class InputQuery(BaseModel):
    query: str

class Response(BaseModel):
    response: str
    sql_query: str
    query: str


sale_schema = """
PushDate (datetime)
DATE_KEY (int)
STORE_KEY (int)
PRODUCT_KEY (int)
STORE_CODE (varchar)
OCCASION_CODE (varchar)
MODECODE (varchar)
REVENUE_CENTRE (varchar)
PROMO_CODE (varchar)
SUBSTITUE_PRODUCT_CODE (varchar)
SALE_TRANS_NO (varchar)
PRODUCT_CODE (varchar)
PARENT_PRODUCT_CODE (varchar)
ORDERMODE_CODE (varchar)
DAYPART_CODE (varchar)
TENDER_TYPE_CODE (varchar)
SALE_RET_QTY (float)
SALE_RET_VAL (float)
SALE_RET_VAL_AT_PRICE (float)
SALE_TOT_VAL_AT_PRICE (float)
SALE_TOT_QTY (float)
SALE_NET_VAL (float)
REFRESH_DATE (datetime)
COMBO_CODE (varchar)
DONATION_SALE_TOT_QTY (float)
DONATION_SALE_NET_VAL (float)
DONATION_SALE_TOT_VAL_AT_PRICE (float)
DELIVERY_CHANNEL (varchar)
HOUR (int)
TILL_NO (varchar)
Tender_Code (varchar)
Store_Date_Code (varchar)
Sale_Trans_Code (varchar)
Donation_Sale_Trans_Code (varchar)
Ret_Sale_Trans_Code (varchar)
IsOrderTable (bit)
UNITCOST (float)
ProductCost (float)
GrossProfit (float)
StoreSheetName (varchar)"""


dim_store_schema = """
STORE_CODE (int)
STORE_DESCRIPTION (varchar)
STORE_SHORT_NAME (varchar)
STORE_REGION (varchar)
STORE_CITY (varchar)
STORE_KEY (int)"""

dim_date_schema = """
DATE_KEY (int)
DATE_FLD (datetime)
MONTH_NAME (varchar)
WEEK_IN_YEAR (int)"""

product_dimension_schema = """
PRODUCT_CODE (int)
PRODUCT_NAME (varchar)
PRODUCT_CATEGORY (varchar)
PRODUCT_SUBCATEGORY (varchar)"""

