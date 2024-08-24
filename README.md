# pet_classifier_unet

## Description
This repository stores a UNET neural network trained with the [Oxford iiit](https://www.robots.ox.ac.uk/~vgg/data/pets/) dataset, containerized in an Ubuntu 20.04 Docker container. The neural network was trained in a Google Colab Notebook and stored in the file `dejando_huella.ipynb`, since the training takes considerably less time with a GPU, a colab T4 GPU.

## Usage
### Testing and Debugging
To debug and test the python script, there's no need for the container to run, keep in mind that this version of the neural network will only work versions of tensorflow lesser than 2.0, this means that it cannot be ran on Windows, it runs perfectly on Ubuntu 20.04. To parse an image and send it to the neural network, follow these steps:

```
pip install -r requirements.txt
```
Change the following `img` variable to teh path to the image to be parsed.
```
if __name__ == "__main__":
    img = ""
    pet = PetClassification()
    pet.main(img)
```
And then run the pet class.
```
python3 pet_class.py
```
### Normal usage
Since this neural network is ran in a Docker container, Docker is a requierement that needs to be installed. Then, the following commands must be ran sequentially.
First, build the Docker image.
```
sudo docker build -t pet-classification .
```
Then, after the image has been built, run the container ensuring that port 5000 is free.
```
sudo docker run -p 5000:5000 pet-classification
```
The container will listen non-stop, to communicate with the container, the following cURL command is used:
```
curl -X POST -F "image=@" http://localhost:5000/classify
```
