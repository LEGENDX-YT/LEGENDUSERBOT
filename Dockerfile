FROM ITS-LEGENDX/LEGENDBOT:slim-buster

#clonning repo 

RUN git clone https://github.com/ITS-LEGENDX/LEGENDUSERBOT.git /root/Legendbot

#working directory 
WORKDIR /root/Legendbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/Legendbot/bin:$PATH"

CMD ["python3","-m","Legendbot"]
