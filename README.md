# pet_classifier_unet

## Description
This repository stores a UNET neural network trained with the [Oxford iiit](https://www.robots.ox.ac.uk/~vgg/data/pets/) dataset, containerized in an Ubuntu 20.04 Docker container. The neural network was trained in a Google Colab Notebook and stored in the file `dejando_huella.ipynb`, since the training takes considerably less time with a GPU, a colab T4 GPU.

## Usage
### Testing and Debugging
To debug and test the python script, there's no need for the container to run, keep in mind that this version of the neural network will only work versions of tensorflow lesser than 2.0, this means that it cannot be ran on Windows, it runs perfectly on Ubuntu 20.04.
