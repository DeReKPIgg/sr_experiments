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
    git 
    
RUN apt-get install -y --no-install-recommends \ 
    openssh-server && \ 
    useradd -m -s /bin/bash "derekct" && \
    echo "derekct:$ssh_pwd" >> ~/passwdfile && \
    chpasswd -c SHA512 < ~/passwdfile && \
    rm ~/passwdfile && \
    sed -i "s/#Port.*/Port 22/" /etc/ssh/sshd_config && \
    sed -i "s/#PermitRootLogin.*/PermitRootLogin yes/" /etc/ssh/sshd_config && \
    sed -i "s/#PasswordAuthentication.*/PasswordAuthentication yes/" /etc/ssh/sshd_config && \
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
EXPOSE 2222
# A common practice is to leave it open for user-defined commands, but you can set a default shell.
EXPOSE 22

ENTRYPOINT service ssh restart && bash




# sudo docker run -id \
#     --gpus all \
#     --name sr_260115 \
#     -v /home/derekpigg:/root \
#     -e DISPLAY=$DISPLAY \
#     -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
#     -v ~/.Xauthority:/root/.Xauthority:rw \
#     -e XAUTHORITY=/tmp/.Xauthority \
#     sr_image tail -f /dev/null


# passwd root
# sed -i 's/#Port 22/Port 726/' /etc/ssh/sshd_config
# sed -i 's/Port 22/Port 726/' /etc/ssh/sshd_config

# # 3. Start the SSH service
# service ssh restart
# ssh root@localhost -p 726