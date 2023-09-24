FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY getElevations.py ./

COPY entrypoint.sh ./
RUN ls -l  # For debugging
RUN chmod +x entrypoint.sh
RUN ls -l  # For debugging

ENTRYPOINT ["./entrypoint.sh"]