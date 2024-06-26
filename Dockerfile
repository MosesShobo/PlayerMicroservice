FROM python
WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "./services/players.py"]
STOPSIGNAL SIGINT