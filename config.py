import os 

class Config:
	NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
	ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
	NEWS_API_KEY = os.environ.get('fa5e9a55a55645f5a9bc581c1cdd8f99')
	SECRET_KEY = os.environ.get('najma')
	
@staticmethod
def init_app(app):
	pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}