import platform


class OSDetector():
    def __init__(self):
        self.os_name = platform.system()

    def get_database(self):
        if (self.os_name == "Linux"):
            db = {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': "mazimii1_magzine",
                "USER": "mazimii1_blog",
                "PASSWORD": "@mirAli89",
                "HOST": "localhost",
                'PORT': 5432
            }
        else:
            db = {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': "magzine",
                "USER": "postgres",
                "PASSWORD": "1482326",
                "HOST": "localhost",
                'PORT': 5432
            }
        return db
