import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing import image as i
from colors import COLORS
import math


class PetClassification:

    def __init__(self):
        self.model = tf.keras.models.load_model("unet_dejando_huella_v1.h5")
        self.image = None
        self.masked_image = None


    def main(self, image):
        # Parse and preprocess the image
        self.parse_image(image)
        # Get masked image
        self.masked_image = self.get_masked_image()
        # get the color dict
        return(self.euclidian_color())
        #! uncomment when debugging
        #self.show_img()

    
    def parse_image(self, image):
        """
        The images have to be resized and normalized; this function will 
        return a prepared image to be used by the model.
        """
        img = i.load_img(image, target_size=(128, 128))
        self.image = i.img_to_array(img)
        self.image = np.expand_dims(self.image, axis=0)  # Add batch dimension
        self.image /= 255.0  # Normalize image


    def create_mask(self, pred_mask):
        pred_mask = tf.math.argmax(pred_mask, axis=-1)
        pred_mask = pred_mask[..., tf.newaxis]
        return pred_mask[0]


    def get_masked_image(self):
        """
        Having the image resized and normalized, this function will
        return the masked image with a green background and the pet as 
        original.
        """
        # Get prediction from model
        pred_mask = self.model.predict(self.image)
        mask = self.create_mask(pred_mask)
        
        # Remove batch dimension from the image
        image = np.squeeze(self.image, axis=0)

        # Apply the mask to the image
        masked_image = np.where(mask == 1, [57, 255, 20], image * 255).astype(np.uint8)

        return masked_image


    def show_img(self):
        """
        Gets the masked image and displays it with the mask on.
        """
        plt.figure(figsize=(8, 8))
        plt.imshow(self.masked_image)
        plt.axis('off')
        plt.show()


    def distance(self, color):
        """
        Returns the closest euclidian color to that color.
        """
        smallest_distance = math.inf
        smallest_color = None
        for c, rgb in COLORS.items():
            r2 = (rgb[0] - color[0])**2
            g2 = (rgb[1] - color[1])**2
            b2 = (rgb[2] - color[2])**2
            euclidian = math.sqrt(r2 + g2 + b2)
            # check if it's closest to the past color
            if euclidian < smallest_distance:
                smallest_distance = euclidian
                smallest_color = c
        
        return smallest_color


    def euclidian_color(self):
        """
        Returns a dictionary with the color count based on the 
        euclidian distance to COLORS
        """
        # map color
        map_color = {}

        for i in range(128):
            for j in range(128):
                # calculate euclidian if not green
                if not np.array_equal(self.masked_image[i][j], [57, 255, 20]):
                    # add color if not in dict
                    color = self.distance(self.masked_image[i][j])
                    if color not in map_color:
                        map_color[color] = 0
                    map_color[color] += 1

        return map_color


if __name__ == "__main__":
    img = ""
    pet = PetClassification()
    pet.main(img)
