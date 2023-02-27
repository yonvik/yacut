import string

SHORT_MAX_LEN = 16
RANDOM_LINK_LENGTH = 6
CHARACTERS_SET = string.ascii_letters + string.digits
REGULAR = r'^[a-zA-Z\d]*$'

URL_LINK = 'Ссылка, которую вы хотите сократить'
CUSTOM_URL_LINK = 'Желаемый адрес'
COMPLITE_LINK = 'Ссылка готова'
MISSING_ID = 'Указанный id не найден'
INVALID_URL_STR = 'Неправильный формат строки'
REQUIRED_FIELD = 'Данное поле обязательное'
SUMBIT = 'Создать'
EMPTY_REQUEST = 'Отсутствует тело запроса'
INVALID_SHORT_LINK = 'Указано недопустимое имя для короткой ссылки'
INVALID_CHARACTERS = ('Недопустимые символы. '
                      'Допустимые: латинские буквы и цифры')
INCORRECT_STRING_LENGTH = ('Длинна строки должна быть не длиннее '
                           '{limit} символов')
DUPLICATE_SHORT_LINK = 'Имя {short_link} уже занято{end}'
FIELDS_MISSING = '"{field}" является обязательным полем!'
INVALID_URL_FORMAT = '"{url}" невалидный URL'
