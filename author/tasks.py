from blog_rest.celery import app
import time

@app.task(name='send vrified message')
def verified_by_phone(i):
    time.sleep(5)
    return i
