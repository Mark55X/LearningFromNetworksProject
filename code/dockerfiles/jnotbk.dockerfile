FROM quay.io/jupyter/base-notebook

# RUN pip install networkx numpy matplotlib

# To avoid reinstalling all the packages whenever is needed to add something
RUN pip install networkx
RUN pip install numpy
RUN pip install matplotlib