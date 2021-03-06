FROM python:3.8
COPY ./ /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["gunicorn", "simple_stripe.wsgi", "-b", "0.0.0.0:8000"]