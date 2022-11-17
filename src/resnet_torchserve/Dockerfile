FROM pytorch/torchserve:0.6.1-cpu

USER root
RUN apt-get update \
    && apt-get install -y wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER model-server
COPY src/resnet_torchserve/create_mar.sh .
RUN bash create_mar.sh

ENTRYPOINT ["torchserve", \
    "--start", "--foreground", \
    "--model-store", "model_store", \
    "--models", "resnet-18=resnet-18.mar"]
