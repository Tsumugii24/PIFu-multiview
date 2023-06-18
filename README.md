# PIFu-multiview
Multiview Reconstruction of PIFu

## run detect.py
You can easily convey the inference process of multiview PIFu reconstruction by running 'dectect.py' in a terminal, without having to use the original shell command 'tesh.sh'. This may great facilitates users of the Windows operating system.

## run gradio_demo.py 
You can run this python file to provide a simple and intuitive web demonstration for multiview PIFu reconstruction results using the API provided by Gradio. With this, you can directly view the reconstructed model of multiview PIFu on a web page without the need to separately download MeshLab and open the model in the software. This makes the entire process more convenient and efficient. However, please remember to install the necessary dependencies for Gradio by running 'pip install gradio'.

## PIFu reconstruction from an arbitrary number of viewpoints
This project theoretically supports reconstruction from an arbitrary number of viewpoints. One can achieve this by modifying the relevant parameters and adjusting the number of input images.


The origin paper: "[PIFu: Pixel-Aligned Implicit Function for High-Resolution Clothed Human Digitization](https://shunsukesaito.github.io/PIFu/)"
