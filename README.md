# University Timetable Scheduling Using Adaptive-Elitist Genetic Algorithm

<img src="https://upload.wikimedia.org/wikipedia/fa/3/39/Tehranshomallogo.png" width="150" />

### Bachelor's final project
The purpose of this project is to use genetic algorithm to solve university class scheduling problems.

# Installation & Run
- Install [`Python 3.9`](https://www.python.org/downloads/)
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

# Documentation
Full documentation and program instructions and statistics in Persian language 
- [`Download PDF file`](Documentation/AutoUniversityScheduler.pdf)
# GUI Usage:
1. Add instructors
2. Add rooms
3. Add subjects
4. Add sections
5. Generate solution
6. Export or View Result

# Dependencies:
1. numpy==1.23.1
2. packaging==21.3
3. psutil==5.9.1
4. pyparsing==3.0.9
5. PyQt5==5.15.7
6. PyQt5-Qt5==5.15.2
7. PyQt5-sip==12.11.0
8. QtAwesome==1.1.1
9. QtPy==2.1.0
10. XlsxWriter==3.0.3



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


Special thanks to Dr. Mobasheri
