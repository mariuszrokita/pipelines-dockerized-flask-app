class Config:
    DEBUG = False
    TEXT_TO_DISPLAY = 'Today is a wonderful day!'

class DevelopmentConfig(Config):
    TEXT_TO_DISPLAY = 'Text set by development config'

class ProductionConfig(Config):
    TEXT_TO_DISPLAY = 'Text set by production config'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig    
}