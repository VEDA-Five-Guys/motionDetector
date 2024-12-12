# motionDetector

## Instruction
On Raspberry Pi, you need to set a python virtual environment.
Firstly, clone this repository.
```bash
git clone https://github.com/VEDA-Five-Guys/motionDetector.git
```
In the directory, set up the virtual environment and install required libraries.
```bash
cd motionDetector
python3 -m venv venv
source /venv/bin/activate
pip install mediapipe opencv-python numpy picamera2
```
Now, build the program with the following commands.
```bash
mkdir build
cd build
cmake ..
make
```
Then you can see the executable file named 'motion_detector'. You can execute the file with the following command.
```bash
./motion_detector
```
Note that you need to run this program on virtual environment.
