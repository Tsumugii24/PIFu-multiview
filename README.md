## PIFu-multiview
Multiview Implementation of PIFu

### detect
Instead of having to use the original Shell Command for inference  ``sh ./scripts/test.sh``.

You can easily convey the same process by running  ``python dectect.py``  in a Terminal. This change may facilitates researchers of the windows operating system.

### gradio_demo
You can run this script to provide a simple and intuitive web demonstration for Multiview-PIFu results using the API provided by Gradio. Then, you can directly view the 3D model on a web page without the need to additionally download MeshLab which is suggested by the official. This makes the entire process more convenient and efficient. 

However, please remember to install the necessary dependencies for Gradio by using the following command line

```
pip install gradio
```

Now, try to run 

```
python gradio_demo
```

and then click the link to go to the web page

### PIFu reconstruction from an arbitrary number of viewpoints

The project theoretically supports reconstruction from an arbitrary number of viewpoints. One can achieve this by modifying the relevant parameters and adjusting the number of corresponding input images.

### References

The origin paper: [PIFu: Pixel-Aligned Implicit Function for High-Resolution Clothed Human Digitization](https://shunsukesaito.github.io/PIFu/)

The origin repository: [shunsukesaito/PIFu: This repository contains the code for the paper "PIFu: Pixel-Aligned Implicit Function for High-Resolution Clothed Human Digitization" (github.com)](https://github.com/shunsukesaito/PIFu)

