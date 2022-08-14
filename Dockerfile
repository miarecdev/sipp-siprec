FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive


RUN apt-get update \
  && apt-get install -y \
    curl \
    build-essential cmake \
    libssl-dev \
    libpcap-dev \
    libsctp-dev \
    libncurses5-dev \
    libgsl-dev \
    # cleanup
    && apt-get clean && rm -rf /var/lib/apt/lists/*


# Download, build and install sipp
RUN curl -LO https://github.com/SIPp/sipp/releases/download/v3.6.1/sipp-3.6.1.tar.gz \
  && tar -xzf /sipp-3.6.1.tar.gz \
  && rm *.tar.gz \
  && cd /sipp-3.6.1 \
  && cmake . -DUSE_GSL=1 -DUSE_PCAP=1 -DUSE_SSL=1 -DUSE_SCTP=1 \
  && make install \
  && rm -rf /sipp-3.6.1

# Add scenario files into the container
ADD scenarios /sipp/scenarios
ADD audio_alaw_2h.wav /sipp/
ADD audio_alaw.wav /sipp/
ADD g711a.pcap /sipp/
ADD g722.pcap /sipp/

WORKDIR /sipp

ENTRYPOINT ["sipp"]
