FROM continuumio/miniconda:latest

WORKDIR /home/docker_prediction_api

COPY . ./

RUN chmod +x boot.sh

RUN conda env create -f environment.yml

RUN echo "source activate fypenv" > ~/.bashrc
ENV PATH /opt/conda/envs/fypenv/bin:$PATH

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]