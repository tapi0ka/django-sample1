FROM python:3

WORKDIR /usr/src/app

# apt-key add したときにwarningを出さない
ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
  && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
  google-chrome-stable \
  default-libmysqlclient-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN google-chrome --version | perl -pe 's/([^0-9]+)([0-9]+\.[0-9]+).+/$2/g' > chrome-version
RUN pip install chromedriver-binary~=`cat chrome-version` && rm chrome-version

