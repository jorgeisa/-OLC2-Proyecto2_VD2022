FROM python:3.10-slim

WORKDIR /proyecto

COPY . .

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install Flask 
RUN pip install flask-cors
RUN pip install Jinja2==3.0.1
RUN pip install matplotlib
RUN pip install numpy
RUN pip install sklearn
RUN pip install scikit-learn
RUN pip install werkzeug
RUN pip install pandas


EXPOSE 5000

CMD [ "python", "app.py" ]