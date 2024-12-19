FROM quay.io/jupyter/base-notebook

# RUN pip install networkx numpy matplotlib

# To avoid reinstalling all the packages whenever is needed to add something
RUN pip install networkx==3.4.2
RUN pip install numpy
RUN pip install matplotlib
RUN pip install scipy