import yaml
import os

# FPATH='src\\config\\config.yml'

path_current_directory = os.path.dirname(os.path.abspath(__file__))
FPATH = os.path.join(path_current_directory, "config.yml")


class Config:

    ADMIN_CHOICE = None
    CUSTOMER_CHOICE = None
    WELCOME_STRING = None
    DB_NAME = None
    ASK_FOR_LOGIN_SIGNUP = None
    ENTER_VALID_PROMPT = None
    SIGNUP_SUCCESS = None
    CREDENTIAL_WARNING = None
    LOGIN_SUCCESS = None
    ADMIN_ROLE_CHOICE = None
    PWD_WARNING = None
    ENTER_WALLET_AMOUNT = None
    ASK_FOR_PWD = None
    ASK_FOR_NAME = None
    ATTEMPTS_LEFT_WARNING = None
    ASK_FOR_EMAIL = None
    ADD_AMOUNT_TO_WALLET = None
    ASK_FOR_UPDATE = None
    UPDATE_PRODUCT_PROMPT = None
    ASK_PROD_NAME = None
    ASK_PROD_PRICE = None
    ASK_PROD_QUAN = None
    ENTER_NEW_PROD_NAME = None
    ENTER_NEW_PROD_QUAN = None
    ENTER_NEW_PROD_PRICE = None
    ASK_PROD_ID = None
    SELECT_VALID_PRODUCT = None
    SELECT_PRODUCT_PROMPT = None
    ASK_TO_PLACE_ORDER = None
    O_ID = None
    WALLET_MONEY = None
    ITEMS_REMAIN = None
    ADD_SUFFICIENT_MONEY = None
    PROD_DOES_NOT_EXIST = None

    @classmethod
    def load(cls):
        with open(FPATH, "r") as f:
            data = yaml.safe_load(f)
            cls.ADMIN_CHOICE = data["admin_prompt"]
            cls.CUSTOMER_CHOICE = data["customer_prompt"]
            cls.WELCOME_STRING = data["welcome"]
            cls.DB_NAME = data["database_name"]
            cls.ASK_FOR_LOGIN_SIGNUP = data["ask_for_login_signup"]
            cls.ENTER_VALID_PROMPT = data["enter_valid_prompt"]
            cls.SIGNUP_SUCCESS = data["signup_success"]
            cls.CREDENTIAL_WARNING = data["credential_warning"]
            cls.LOGIN_SUCCESS = data["login_success"]
            cls.ADMIN_ROLE_CHOICE = data["admin_role_choice"]
            cls.PWD_WARNING = data["pwd_warning"]
            cls.ENTER_WALLET_AMOUNT = data["enter_wallet_amount"]
            cls.ASK_FOR_PWD = data["ask_for_pwd"]
            cls.ASK_FOR_NAME = data["ask_for_name"]
            cls.ATTEMPTS_LEFT_WARNING = data["attempts_left_warning"]
            cls.ASK_FOR_EMAIL = data["ask_for_email"]
            cls.ADD_AMOUNT_TO_WALLET = data["add_amount_to_wallet"]
            cls.ASK_FOR_UPDATE = data["ask_for_update"]
            cls.UPDATE_PRODUCT_PROMPT = data["update_product_prompt"]
            cls.ASK_PROD_NAME = data["ask_prod_name"]
            cls.ASK_PROD_PRICE = data["ask_prod_price"]
            cls.ASK_PROD_QUAN = data["ask_prod_quan"]
            cls.ENTER_NEW_PROD_NAME = data["enter_new_prod_name"]
            cls.ENTER_NEW_PROD_QUAN = data["enter_new_prod_quan"]
            cls.ENTER_NEW_PROD_PRICE = data["enter_new_prod_price"]
            cls.ASK_PROD_ID = data["ask_prod_id"]
            cls.SELECT_VALID_PRODUCT = data["select_valid_product"]
            cls.SELECT_PRODUCT_PROMPT = data["select_product_prompt"]
            cls.ASK_TO_PLACE_ORDER = data["ask_to_place_order"]
            cls.O_ID = data["o_id"]
            cls.WALLET_MONEY = data["wallet_money"]
            cls.ITEMS_REMAIN = data["items_remain"]
            cls.ADD_SUFFICIENT_MONEY = data["add_sufficient_money"]
            cls.PROD_DOES_NOT_EXIST = data["prod_does_not_exist"]


Config.load()
