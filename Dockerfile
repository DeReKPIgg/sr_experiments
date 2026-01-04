# Use a Python base image (e.g., Debian slim) as it already includes Python and pip
FROM python:3.12-slim

# We update the package lists and install iverilog and git
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    cmake \
    libgl1 \
    libglib2.0-0 \
    libgtk2.0-dev pkg-config \
    libxcb-cursor0 \
    build-essential \
    git && \ 
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    numpy \
    scipy \
    opencv-python \
    opencv-python-headless \
    opencv-contrib-python

WORKDIR /root

# Standard port for your Python app
EXPOSE 8000

# Standard port for TensorBoard
EXPOSE 6006

# Standard port for Streamlit (if you use it)
EXPOSE 8501

# 5. Set the default command or entrypoint
# A common practice is to leave it open for user-defined commands, but you can set a default shell.
CMD ["/bin/bash"]