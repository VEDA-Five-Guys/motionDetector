# motionDetector

## Prequisite
you need to install some libraies with the following commands below.  
```
sudo apt-get update
sudo apt-get install g++ cmake python3-dev libboost-all-dev libssl-dev libcamera-dev
```

## Instruction
On Raspberry Pi, you need to set a python virtual environment.
Firstly, clone this repository.
```bash
git clone https://github.com/VEDA-Five-Guys/motionDetector.git
```
In the directory, set up the virtual environment and install required libraries.
```bash
cd motionDetector
python3 -m venv --system-site-packages venv
source venv/bin/activate
pip install opencv-python mediapipe numpy picamera2
```
Build the program with the following commands.
```bash
mkdir build
cd build
cmake ..
make
```
Then you can see the executable file named 'motion_detector'.  
Now, you can execute the program with the following command.
```bash
./motion_detector
```
Note that you need to run this program on virtual environment.

https://github.com/user-attachments/assets/9b0f8ad1-e40d-49d4-b86b-08350869989b
