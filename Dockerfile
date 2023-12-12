FROM python:3.10-alpine3.19

RUN echo "Dependencies installation"

COPY requirements.txt requirements.txt

RUN apk add --no-cache gcc musl-dev python3-dev linux-headers

RUN pip3 install -r requirements.txt

COPY src/ src/

RUN apk add --no-cache bash

CMD [ "bash" ]