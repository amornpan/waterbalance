# Use the official Jupyter Notebook base image
FROM jupyter/base-notebook:latest

# # Copy your system_configuration.py file into the container
#COPY ./system_configuration.py /etc/jupyter/system_configuration.py
#COPY notebook_config.py /etc/jupyter/notebook_config.py

# Disable the Jupyter Notebook token
ENV JUPYTER_TOKEN ''


# Expose the Jupyter Notebook port
EXPOSE 8888

# Run Jupyter Notebook with the custom configuration
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--config=/etc/jupyter/system_configuration.py", "--allow-root"]
