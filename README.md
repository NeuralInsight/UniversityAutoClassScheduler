# University Timetable Scheduling Using Adaptive-Elitist Genetic Algorithm

![alt text](https://upload.wikimedia.org/wikipedia/fa/3/39/Tehranshomallogo.png)
### Bachelor's final project

# Installation & Run
- Install [`Python 3.7`](https://www.python.org/downloads/)
- Create a new virtual environment
```
    python3 -m venv venv
```
- Activate the virtual environment
```
    source venv/bin/activate
```
- Install all the requirements using
```
    pip install -r requirements.txt 
```
- To use sample Data copy the file 'sample_gas.db' to main directory and rename it to 'gas.db'
- Run the program using
```
    python3 main.py
```
### Usage:
1. Add instructors
2. Add rooms
3. Add subjects
4. Add sections
5. Generate solution
6. Export or View Result

### Dependencies:
1. Numpy
2. PyQT5
3. psutil
4. logging
5. xlsxwriter


## TODO:

### Genetic Algorithm
- [X] Changing TimeSlot form 0.5 to 0.75
- [X] Shouldn't run the Evalution with 0 point !

### GUI
- [X] fix tableView toggle bug
- [x] fix Class tree
- [x] Add sorting to Header Labels of class tree
- [x] add search 
- [x] add some qss file :)
- [x] add icons
- [x] add Alternating Row Colors
- [ ] fix database, some data should be unique 
