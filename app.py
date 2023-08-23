""" The application is developed by Kittipich "Luke" Aiumbhornsin
Created on August 6, 2023
temp blog app
Run file of the application """

from tempblog import createApp
from decouple import config as envar
from time import localtime
import pytz


# print(pytz.all_timezones)  # List out all the timezone available
envi = envar('ENVI', 'production')
match envi:

    case 'production':
        # for running gunicorn (in production)
        app = createApp()

    case _:
        # for dev
        if __name__ == '__main__':
            app = createApp()
            app.run(port=int(envar("PORT", 5500)),
                    debug=envar("DEBUG", True))
