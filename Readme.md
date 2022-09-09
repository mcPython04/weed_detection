# Weed Detection with YOLOv5

## Hardware Specifications
Computer: Nvidia's Jetson Nano

Camera: "camera info"

OS: Ubuntu 18.04

**More information about Jetson Nano can be found [here](https://developer.nvidia.com/embedded/jetson-nano-developer-kit)


## Environment Setup
1. Run `bash venv_setup.txt` . This will create a virtual environment called `venv` and clone the YOLOv5 repository.

2. Run `source venv/bin/activate` to activate the virtual environment.

3. Within the virtual environment run `pip install -r requirements.txt` to install the dependencies.

4. Run `deactivate` to close the virtual environment.


## Running the Inference
To run command line inference: `bash exec/cli_inf.txt`

To run PyTorch inference: `bash exec/pytorch_inf.txt`

Inference videos can be found within the `media` folder.

<b>**NOTE: </b> You may need to replace the arguments within the `--source` parameter (within the .txt file) with the registered device_id on your computer. 


## Setup for PyTorch Inference: Signal Output
<img src="./media/1-pin-diagram-nvidia-jetson-nano.jpg" width="450" height="350">
"Pin Layout Info"

<img src="./media/breadboard_pic.jpeg" width="450" height="350">
"Picture of Breadboard and Pin setup"

