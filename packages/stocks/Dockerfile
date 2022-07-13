FROM python:3.10



WORKDIR /srv/
RUN mkdir /data



COPY src /srv/monkeyfusion/stocks



RUN pip3 install cairosvg
RUN pip3 install numpy
RUN pip3 install colorcet



ENTRYPOINT ["python3", "-m", "monkeyfusion.stocks.main"]
