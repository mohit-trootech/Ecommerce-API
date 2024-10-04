from django.utils.translation import gettext_noop as _
from enum import Enum
from dotenv import dotenv_values


# Settings Constants
# =====================================================
class Settings(Enum):
    ROOT_URL = "ecommerce.urls"
    TEMPLATE = "templates"
    STATIC_URL = "static/"
    STATICFILES_DIRS = "templates/static/"
    STATIC_ROOT = "assets/"
    MEDIA_URL = "media/"
    MEDIA_ROOT = "media/"
    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "Asia/Kolkata"
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
    DEBUG_TOOLBAR_IP = "127.0.0.1"
    CACHE_TABLE_NAME = "cache_table"


# Model Choices
# =====================================================
class ModelChoices(Enum):
    MALE = _("Male")
    MALE_TEXT = "M"
    FEMALE = _("Female")
    FEMALE_TEXT = "F"
    OTHER = _("Other")
    OTHER_TEXT = "O"
    GENDER_CHOICE = (
        (MALE_TEXT, MALE),
        (FEMALE_TEXT, FEMALE),
        (OTHER_TEXT, OTHER),
    )


# Custom Exceptions Messages Constants
# =====================================================
class CustomExceptionMessages(Enum):
    CATEGORY_GET_EXCEPTION = "Categories not available, please check the internet connection or contact API owner"
    USER_NOT_AVAILABLE = "User not Available"


# Admin Action Description
# =====================================================
class AdminAction(Enum):
    USER_ADMIN_STATUS_UNACTIVE_DESCRIPTION = _("Mark Selected Items Unactive")
    USER_ADMIN_STATUS_ACTIVE_DESCRIPTION = _("Mark Selected Items Active")
    USER_INACTIVE_SUCCESS_MESSAGE = _("%d users were successfully been inactive.")
    USER_ACTIVE_SUCCESS_MESSAGE = _("%d users were successfully been active.")
    STATUS_INACTIVE = False
    STATUS_ACTIVE = True


# Error Messages
# =====================================================
class Errors(Enum):
    INVALID_JSON = _("Invalid JSON data")
    LOGIN_ERROR = _("Failed to Login Try Again with Correct Credentials")
    PASSWORD_NOT_MATCH = _("Please Check Passwords are Not Matching")
    UNIQUE_USER_ERROR = _("User with Same Username or Password Already Exists")
    TERMS_NOT_ACCEPTED = _("Please Accept Terms and Conditions")


# Success Messages
# =====================================================
class Success(Enum):
    REGISTERED = _("User Added Successfully")
    USER_404 = _("User Does Not Exists")
    USER_UPDATED = _("User updated successfully")
    LOGGED_IN = _("Logged in Successfully")
    SIGNED_UP = _("User Registered Successfully")
    LOGGED_OUT = _("User Logged Out Successfully")
    FORCE_LOGGED_OUT = _("User Logged Out Successfully from all Sessions")
    PROFILE_UPDATED = _("Profile Updated Successfully")
    NEWSLETTER_SUCCESS = _("Newsletter Subscribed Successfully")
    API_KEY_UPDATED = _("API Key Updated Successfully")


# Templates Name
# =====================================================
class Templates(Enum):
    INDEX = "ecommerce/home.html"
    ABOUT = "ecommerce/about.html"
    TERMS = "ecommerce/terms.html"
    PROFILE = "accounts/profile.html"
    LOGIN = "accounts/login.html"
    SIGNUP = "accounts/signup.html"
    STORE = "store/index.html"
    PRODUCT_ADD = "store/add-product.html"
    CART = "store/cart.html"
    WISHLIST = "store/wishlist.html"
    PRODUCT = "store/product-page.html"


# Urls Path & Reverse
# =====================================================
class Urls(Enum):
    HOME = "index"
    ABOUT = "about"
    TERMS = "terms"
    STORE = "store"
    SCHEMA_REVERSE = "schema"
    LOGIN_REVERSE = "login"
    LOGIN = "/accounts/login/"
    LOGOUT_REVERSE = "logout"
    FORCE_LOGOUT_REVERSE = "force-logout"
    REGISTER_REVERSE = "signup"
    PROFILE_REVERSE = "profile"
    PROFILE_URL = "/accounts/profile/{pk}"
    API_REVERSE = "api"
    ADD_PRODUCT = "product-add"
    CART = "cart"
    WISHLIST = "wishlist"
    PRODUCT = "product"


# Operation Type Names
# =====================================================
class OperationType(Enum):
    ADD = "add"
    REMOVE = "remove"
    UPDATE = "update"


# Serializers Variable Names
# =====================================================
class SerializersConstants(Enum):
    PRODUCTS_REQUIRED = "Products are required"
    CATEGORY_NOT_EXIST = "Category does not exist with the given ID"
    IMAGES_REQUIRED = "Images are Required"
    PRODUCT_NOT_EXIST = "Products does not exist with the given ID"
    OPERATION_REQUIRED = "Please Choose Operation"


# Forms Constants Dictionary
# =====================================================
FORM_LABELS = {
    "first_name": "Enter First Name",
    "last_name": "Enter Last Name",
    "username": "Enter Username",
    "email": "Enter Email",
    "password": "Enter Password",
}


class FormLabel(Enum):
    TITLE = _("Title")
    DESCRIPTION = _("Description")
    PRICE = _("Price")
    STOCK = _("Stock")
    CATEGORY = _("Category")
    IMAGE_1 = _("Image 1")
    IMAGE_2 = _("Image 2")
    IMAGE_3 = _("Image 3")
    IMAGE_4 = _("Image 4")


# Email Configurations
# =====================================================
class EmailConfig(Enum):
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    PORT_465 = 465
    PORT_587 = 587


# Request KEY
# =====================================================
class RequestKey(Enum):
    pass


# Response KEY
# =====================================================
class ResponseKey(Enum):
    pass


# Email Secret
# =====================================================
class EmailConstants(Enum):
    config = dotenv_values(".env")
    NEWSLETTER = _("QuickReads Newsletter Subscribed")
    HOST = config.get("EMAIL_HOST_USER")


# Other Constants
# =====================================================
EMPTY_STR = ""
UTF_8 = "utf-8"
FORM_CLASS = "input input-bordered w-full"
FORM_CLASS_FILE = "file-input file-input-bordered w-full"
TEXT_AREA = "textarea textarea-bordered textarea-lg w-full"
SELECT_CLASS = "select select-bordered w-full select-sm"
THEME_CHOICES = (
    ("light", "light"),
    ("dark", "dark"),
    ("cupcake", "cupcake"),
    ("bumblebee", "bumblebee"),
    ("emerald", "emerald"),
    ("corporate", "corporate"),
    ("synthwave", "synthwave"),
    ("retro", "retro"),
    ("cyberpunk", "cyberpunk"),
    ("valentine", "valentine"),
    ("halloween", "halloween"),
    ("garden", "garden"),
    ("forest", "forest"),
    ("aqua", "aqua"),
    ("lofi", "lofi"),
    ("pastel", "pastel"),
    ("fantasy", "fantasy"),
    ("wireframe", "wireframe"),
    ("black", "black"),
    ("luxury", "luxury"),
    ("dracula", "dracula"),
    ("cmyk", "cmyk"),
    ("autumn", "autumn"),
    ("business", "business"),
    ("acid", "acid"),
    ("lemonade", "lemonade"),
    ("night", "night"),
    ("coffee", "coffee"),
    ("winter", "winter"),
    ("dim", "dim"),
    ("nord", "nord"),
    ("sunset", "sunset"),
)
CATEGORY_GET = "http://127.0.0.1:8000/api/categories/"
TYPE_HTML = "text/html"
