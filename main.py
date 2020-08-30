# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from celery_config.celery_workers import *
import datetime
def main(date):
    # Use a breakpoint in the code line below to debug your script.
    print(date)
    celeryapp.tasks['task1'].delay(date)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(datetime.datetime.now())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
