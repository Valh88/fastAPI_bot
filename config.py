from loguru import logger
import sys

bot_token = '5609241017:AAEvJrXclo5G7kWD7gcJea4H488eq9-eQjA'

tg_admin_id = 5076974968

api_url = " http://127.0.0.1:8000"

SECRET_KEY = 'b24a1ef62ea82aee48951f9d40358adc89636d8bdbb553be95ae4721c03ff2b1'
# openssl rand -hex 32

ALGORITHM = 'HS256'

username = 'admin'

password = '$2b$12$T9LUOmZ.N/QRmR7rq5KhEecFlcg24/oMLuvrPKfKdXkA4TOnlBpK6'


username2 = 'user'

password2 = '$2b$12$TaXjJ.AEaPo5zE2ySkXXnO9mvk7weyyk3Dc1CxjccB6nW05WhWhHe'

logger.add('logs.log', level='DEBUG', rotation='100 MB', compression='zip')
logger.debug('Error')
logger.info('Information message')
logger.warning('Warning')
