from PyQt5 import QtCore
from components import Settings,Utilities
from operator import itemgetter
from collections import Counter
import copy
import itertools
import numpy as np
import logging


#Creating and Configuring Logger
Log_Format = "%(levelname)s %(asctime)s - %(message)s"


logging.basicConfig(filename = "logfile.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.DEBUG,
                    encoding='utf-8')

# Logging Level = debug, info, warning, error

logger = logging.getLogger()

logger.info("init Genetic Algorithm")


class GeneticAlgorithm(QtCore.QThread):
    # Current phase of the algorithm
    statusSignal = QtCore.pyqtSignal(str)
    # Genetic algorithm variable details
    detailsSignal = QtCore.pyqtSignal(list)
    # Running process type
    operationSignal = QtCore.pyqtSignal(int)
    # List of chromosomes for preview
    dataSignal = QtCore.pyqtSignal(list)
    # Operation ProgressBar
    progressBarSignal = QtCore.pyqtSignal(int)
    # Operation Progress Status
    progressSignal = QtCore.pyqtSignal(str)

    def __init__(self, data):
        self.averageFitness = 0
        self.pastAverageFitness = 0
        self.running = True
        self.chromosomes = []
        self.data = {
            'rooms': [],
            'instructors': [],
            'sections': [],
            'subjects': []
        }
        self.tournamentSize = .04
        self.elitePercent = .05
        self.lowVariety = 55
        self.highestFitness = 0
        self.lowestFitness = 100
        self.elites = []
        self.matingPool = []
        self.offsprings = []
        self.tempChromosome = None
        self.tempSections = None
        self.data = data
        self.settings = Settings.getSettings()
        self.stopWhenMaxFitnessAt = self.settings['maximum_fitness']
        self.mutationRate = self.settings['mutation_rate_base']
        self.mutationRateStep = self.settings['mutation_rate_step']
        super().__init__()

    def initialization(self):
        # Generate population based on minimum population
        self.generateChromosome(self.settings['minimum_population'])

    def generateChromosome(self, quantity):
        self.progressBarSignal.emit(0)
        for i in range(quantity):
            self.statusSignal.emit('ایجاد #{} از {} کروموزوم'.format(i, quantity)) # Display Chromosome creation
            self.progressBarSignal.emit(int(i * 100 / quantity))
            self.tempChromosome = Chromosome(self.data) # Create new Chromosome
            # {id: [[subjectIds](roomId)]}
            self.tempSections = sections = {key: [value[2], value[3]] for (key, value) in 
                                            copy.deepcopy(self.data['sections']).items()}
            # [roomIds]
            self.rooms = rooms = list(self.data['rooms'].keys()) # Get all roomIds

            self.generateSubjectPlacementsForSections(sections)
            self.chromosomes.append(self.tempChromosome)

    # {id: [[subjectIds](roomId]}
    def generateSubjectPlacementsForSections(self, sections):
        # Maximum length of section subjects
        maxSubjects = max(len(subjects[0]) for subjects in sections.values())
        # Put one random section subject per turn
        for i in range(maxSubjects):
            for section in sections:
                subjectList = sections[section][0]
                if not len(subjectList):
                    continue
                subjectToPlace = np.random.randint(0, len(subjectList))
                result = self.generateSubjectPlacement([section], subjectList[subjectToPlace])
                if not result:
                    self.tempChromosome.data['unplaced']['sections'][section].append(subjectList[subjectToPlace])
                sections[section][0].pop(subjectToPlace)

    # Section = [id], Subject = int (id)
    def generateSubjectPlacement(self, section, subject):
        generating = True
        generationAttempt = 0
        error = None

        subjectDetails = self.data['subjects'][subject] # Get All Subject Details

        room = None
        # [[day/s], startingTimeSlot, length]
        timeDetails = []
        instructor = None

        while generating:
            # Control generation to avoid impossible combinations
            generationAttempt += 1
            #  Check to reach maximum generation attempts
            if generationAttempt > self.settings['generation_tolerance']: 
                generating = False
                return False
            # First time generation
            if not error:
                # Select a random room
                room = self.selectRoom(subject)
                # Select instructors for the subjects
                if len(subjectDetails[4]) > 1:
                    instructor = self.selectInstructor(subject) #Select Random Instructor
                elif len(subjectDetails[4]):
                    instructor = subjectDetails[4][0]
                else:
                    instructor = False
                # Select time slot for the subject
                timeDetails = self.selectTimeDetails(subject)
            else:
                # Randomly select if choosing new entry or replacing subject time details
                if error == 1 or error == 2:
                    if np.random.randint(0, 2):
                        error = 3
                    elif error == 1:
                        room = self.selectRoom(subject)
                    else:
                        if len(subjectDetails[4]) > 1:
                            instructor = self.selectInstructor(subject)
                        else:
                            error = 3
                # Select subject time details
                elif error == 3 or error == 4:
                    # timeDetails = [meetingPattern (days), startingTimeslot, int(hours)]
                    timeDetails = self.selectTimeDetails(subject)

            # [roomId, [sectionId], subjectId, instructorID, [day / s], startingTS, length]
            scheduleToInsert = [room, section, subject, instructor, *timeDetails]
            # Check if subject can be inserted
            error = self.tempChromosome.insertSchedule(scheduleToInsert)
            if error is False:
                return True

    def selectRoom(self, subject):
        room = None
        while not room:
            candidate = np.random.choice(self.rooms)
            if self.data['subjects'][subject][6] == self.data['rooms'][candidate][1]:
                room = candidate
        return room

    def selectInstructor(self, subject):
        instructor = None
        subjectInstructors = self.data['subjects'][subject][4]
        while not instructor and len(subjectInstructors):
            instructor = np.random.choice(subjectInstructors)
        return instructor

    def selectTimeDetails(self, subject):
        days = [0, 1, 2, 3, 4, 5]
        np.random.shuffle(days)
        hours = self.data['subjects'][subject][1]
        # Check if hours can be splitted with minimum session of 1 hour or 2 timeslot
        selected_day = [np.random.randint(0, 6)]
        # To convert hours into timetable timeslots
        # hours = hours / .5
        startingTimeslot_status = False
        # Starting slot selection
        startingTime = self.settings['starting_time']
        endingTime = self.settings['ending_time']
        while not startingTimeslot_status:
            candidate = np.random.randint(startingTime, endingTime - startingTime)
            # Validate if subject will not overpass operation time
            if (candidate + hours) <= endingTime:
                startingTimeslot = candidate
                startingTimeslot_status = True
        return [selected_day, int(startingTimeslot), int(hours)]

    def evaluate(self):
        totalChromosomeFitness = 0
        self.pastAverageFitness = copy.deepcopy(self.averageFitness) 
        self.lowestFitness = 100
        self.highestFitness = 0
        self.progressBarSignal.emit(0)
        for index, chromosome in enumerate(self.chromosomes): # For each chromosome
            self.statusSignal.emit('ارزیابی کروموزم #{} از {}'.format(index + 1, len(self.chromosomes)))
            self.progressBarSignal.emit(int((index + 1) * 100 / len(self.chromosomes)))
            chromosome.fitness = self.evaluateAll(chromosome)
            totalChromosomeFitness += chromosome.fitness # Add chromosome fitness to total fitness
            self.averageFitness = totalChromosomeFitness / len(self.chromosomes) 
            self.highestFitness = chromosome.fitness if chromosome.fitness > self.highestFitness else self.highestFitness # Update Highest Fitness
            self.lowestFitness = chromosome.fitness if chromosome.fitness < self.lowestFitness else self.lowestFitness # Update Lowest Fitness
        chromosomeFitness = sorted(enumerate(map(lambda chromosome: chromosome.fitness, self.chromosomes)),
                                   key=itemgetter(1))  # Sort chromosomes by fitness
        # Emit top five chromosomes
        self.dataSignal.emit(
            list(map(lambda chromosome: [self.chromosomes[chromosome[0]], chromosome[1]], chromosomeFitness[-5:])))

    # Evaluation weight depends on settings
    def evaluateAll(self, chromosome):
        matrix = self.settings['evaluation_matrix'] # Get evaluation matrix
        # If subject placement is enabled else 0
        subjectPlacement = self.evaluateSubjectPlacements(chromosome) if matrix['subject_placement'] !=0 else 0
        # If idle time is enabled else 0
        idleTime = self.evaluateInstructorIdleTime(chromosome) if matrix['idle_time'] !=0 else 0
        
        chromosome.fitnessDetails = copy.deepcopy([subjectPlacement, idleTime])
        return (
            (subjectPlacement * matrix['subject_placement'] / 100) +
            (idleTime * matrix['idle_time'] / 100) 
        )

    # = ((subjects - unplacedSubjects) / subjects) * 100
    def evaluateSubjectPlacements(self, chromosome):
        sections = copy.deepcopy({key: value[2] for key, value in self.data['sections'].items()})

        chromosomeUnplacedData = chromosome.data['unplaced'] # Get chromosome unplaced data
        chromosomePlacedData = chromosome.data['sections'][1]['details'] # Get chromosome placed data
        len_chromosomeUnPlacedData = 0
        len_chromosomePlacedData = 0
        for key in chromosomePlacedData: # For each chromosome placed data
            if chromosomePlacedData[key] == []: # If chromosome placed data is empty
                len_chromosomeUnPlacedData += 1 # Add to unplaced data length
                continue # Continue to next iteration
            len_chromosomePlacedData += 1 # Add to placed data length

        # logger.debug("Placed Subject: {}".format(chromosomePlacedData))
        # logger.debug('Placed Data Length: {}'.format(len_chromosomePlacedData))
        # get chromosome id
        chromosomeId = self.chromosomes.index(chromosome)
        # logger.debug("chromosome {} unplaced subjects: {}".format(chromosomeId, chromosomeUnplacedData['sections'][1]))
        # Combined list of section subjects
        sectionSubjects = len(list(itertools.chain.from_iterable(sections.values())))
        # logger.debug("section subjects: {}".format(sectionSubjects))
        # Combined list of subjects
        totalSubjects = sectionSubjects
        # Length of unplaced section subjects
        unplacedSectionSubjects = len(list(itertools.chain.from_iterable(chromosomeUnplacedData['sections'].values())))
        # logger.debug("unplaced section subjects: {}".format(unplacedSectionSubjects))
        totalUnplacedSubjects = len_chromosomeUnPlacedData
        # logger.debug("len_chromosomeUnPlacedData: {}".format(totalUnplacedSubjects))
        return round(((totalSubjects - totalUnplacedSubjects) / totalSubjects) * 100, 2)

    # = ((idleTime / totalTime) * 100)
    def evaluateInstructorIdleTime(self, chromosome):
        instructor_id = 0
        instructor_fitnesses = []
        # script to fine 1(None)*1 Pattern in the list
        for instructor in chromosome.data['instructors'].values():
            # Instructor week 
            instructor_id += 1
            week = {day: [] for day in range(6)}
            for timeslot, timeslotRow in enumerate(instructor):
                for day, value in enumerate(timeslotRow):
                    week[day].append(value)

            week_fitnesses = []
            for day in week.values():
                # find the number of None in day list
                day_free_timeslots = [x for x in day if x is None]
                n_free_timeslots = len(day_free_timeslots) # number of free timeslots
                n_subjects = Utilities.find_numberOfSubject(day) # number of subjects
                # x = Utilities.find_StartgapTimeSlot(day)
                # logger.debug("instructor {} day: {} StartGap: {}".format(instructor_id, day, x))
                # if there is atleast two subject
                if n_subjects:  
                    n_day_gapslots = Utilities.find_gapTimeSlot(day) # number of gap timeslots
                    day_fitness = (((n_free_timeslots - n_day_gapslots) / n_free_timeslots) * 100) # fitness of day
                    week_fitnesses.append(day_fitness) # add fitness of day to week fitnesses
            
            # if there is atleast one day with valid fitness       
            if len(week_fitnesses) != 0:
                # find the average fitness of the week
                instructor_fitness = (sum(week_fitnesses) / len(week_fitnesses))
                # add fitness of week to instructor fitnesses
                instructor_fitnesses.append(instructor_fitness)
                
        # if there is atleast one instructor with valid fitness
        if len(instructor_fitnesses) != 0:
            # find the average fitness of the instructor
            return (sum(instructor_fitnesses) / len(instructor_fitnesses))
        else: 
            return 0.0000

    def evaluateSubjectsStartTime(self, chromosome):
        pass
    

    def getAllFitness(self):
        return [chromosome.fitness for chromosome in self.chromosomes]

    def adapt(self):
        deviation = self.getFitnessDeviation() # it returns sigma & sigma instances
        self.alignPopulation(deviation[0], deviation[1])
        self.adjustMutationRate()

    # Function to find Mean Deviation of fitnesses
    # sigma = [sigma], sigmaInstances = {sigma: instance%}
    def getFitnessDeviation(self):
        populationCount = len(self.chromosomes) # find number of population
        fitnesses = [chromosome.fitness for chromosome in self.chromosomes]
        mean = np.mean(fitnesses)
        sigmas = [int(fitness - mean) for fitness in fitnesses]
        sigmaInstances = {sigma: (instance / populationCount) * 100 for sigma, instance in
                          dict(Counter(sigmas)).items()}
        return [sigmas, sigmaInstances]

    def alignPopulation(self, sigmas, sigmaInstances):
        populationCount = len(self.chromosomes) # find number of population
        sigmaStartingInstance = list(sigmaInstances.values())[0] # get first sigmaInstance value
        if sigmaStartingInstance > self.lowVariety: #TODO: Check lowVariety
            # Add the excess percentage of instances on first sigma to population
            generate = int((int(sigmaStartingInstance - self.lowVariety) / 100) * populationCount)
            while generate + populationCount > self.settings['maximum_population']:
                generate -= 1
            self.generateChromosome(generate)
        else:
            # Remove the excess percentage of instances on first sigma to population
            sortedSigmas = sorted(enumerate(sigmas), key=itemgetter(1))
            remove = int((int(self.lowVariety - sigmaStartingInstance) / 100) * populationCount)
            while populationCount - remove < self.settings['minimum_population']:
                remove -= 1
            remove = [sortedSigmas[index][0] for index in range(remove)]
            self.chromosomes = [chromosome for index, chromosome in enumerate(self.chromosomes) if index not in remove]

    # Increase mutation rate for low performing generations and decrease for good performance
    def adjustMutationRate(self):
        # Three condition will increase the mutationRate
        ## 1) PastFitnessAverage is Greater than currentFitnessAverage
        ## 2) fitness Difference is lower than mutation_rate_trigger_adjustment
        
        # if mutationRate Increment >= 100 mutationRate will Decrease
        if (self.averageFitness - self.pastAverageFitness < 0) or (
                abs(self.averageFitness - self.pastAverageFitness) <= self.settings[
            'mutation_rate_adjustment_trigger']) and not self.mutationRate >= 100:
            self.mutationRate += .1
        elif self.mutationRate > .10:
            self.mutationRate -= .1

        # Round the mutationRate
        self.mutationRate = round(self.mutationRate, 2)

    # Selects top 5% of population and performs tournament to generate remaining candidates
    def selection(self):
        population = len(self.chromosomes)
        # Get All Chromosome Fitnesses
        chromosomeFitness = [self.chromosomes[chromosome].fitness for chromosome in range(len(self.chromosomes))]
        # Select number of elites that will ensure there will be even offspring to be generated
        eliteCount = round(population * self.elitePercent) # Calculate Elite population
        if population % 2 == 0:
            eliteCount = eliteCount if eliteCount % 2 == 0 else eliteCount + 1
        else:
            eliteCount = eliteCount if eliteCount % 2 != 0 else eliteCount + 1
        self.progressBarSignal.emit(100)
        self.statusSignal.emit('انتخاب {} Elites'.format(eliteCount))
        sortedFitness = sorted(enumerate(chromosomeFitness), key=itemgetter(1))
        elites = list(map(lambda chromosome: chromosome[0], sortedFitness[eliteCount * -1:]))
        matingPool = []
        matingPoolSize = int((population - eliteCount) / 2)
        tournamentSize = int(self.tournamentSize * population)
        if tournamentSize > 25:
            tournamentSize = 25
        # Fill mating pool with couples selected by multiple tournaments
        self.progressBarSignal.emit(0)
        for i in range(matingPoolSize):
            self.statusSignal.emit('ایجاد #{} از {} زوج'.format(i + 1, matingPoolSize))
            self.progressBarSignal.emit(int((i / matingPoolSize) * 100))
            couple = []
            while len(couple) != 2:
                winner = self.createTournament(tournamentSize, chromosomeFitness)
                if winner not in couple:
                    couple.append(winner)
            matingPool.append(couple)
        self.elites = elites
        self.matingPool = matingPool

    # size = int, population = [fitness]
    def createTournament(self, size, population):
        participants = []
        # Select participants
        for i in range(size):
            candidate = False
            while candidate is False:
                candidate = np.random.randint(0, len(population))
                if candidate in participants:
                    candidate = False
                    continue
            participants.append(candidate)
        winner = participants[0]
        for participant in participants:
            if population[participant] > population[winner]:
                winner = participant
        return winner

    def crossover(self):
        offspringCount = 1
        self.offsprings = []
        for couple in self.matingPool:
            self.statusSignal.emit(
                'ایجاد #{} از {} فرزند'.format(offspringCount, len(self.chromosomes) - len(self.elites)))
            self.progressBarSignal.emit(int((offspringCount / (len(self.chromosomes) - len(self.elites))) * 100))
            self.offsprings.append(self.createOffspring(couple))
            offspringCount += 1
            couple.reverse()
            self.statusSignal.emit(
                'ایجاد #{} از {} فرزند'.format(offspringCount, len(self.chromosomes) - len(self.elites)))
            self.progressBarSignal.emit(int((offspringCount / (len(self.chromosomes) - len(self.elites))) * 100))
            self.offsprings.append(self.createOffspring(couple))
            offspringCount += 1
        self.elites = list(map(lambda elite: copy.deepcopy(self.chromosomes[elite]), self.elites))
        self.chromosomes = self.offsprings + self.elites

    # Returns a chromosome containing a mix of parents genes
    def createOffspring(self, parent):
        self.tempChromosome = offspring = Chromosome(self.data)
        parentA = self.chromosomes[parent[0]]
        parentB = self.chromosomes[parent[1]]
        parentAShareables = {
            'sections': {}
        }
        
        parentASections = {}
        for section, value in copy.deepcopy(parentA.data['sections']).items():
            parentASections[section] = value['details']
        parentASections = {key: value for key, value in filter(lambda item: len(item[1]) > 1, parentASections.items())}
        # Calculate the shareables of each section
        for section, values in parentASections.items():
            # Amount of section subjects to share
            sectionCarve = round(len(values) / 3)
            # Middlemost element with bias to left
            startingPoint = int(len(values) / 2) - (sectionCarve - 1)
            subjects = [id for id in values.keys()]
            for index in range(startingPoint, startingPoint + sectionCarve):
                if section not in parentAShareables['sections']:
                    parentAShareables['sections'][section] = {}
                parentAShareables['sections'][section][subjects[index]] = values[subjects[index]]
        parentBShareables = {
            'sections': {}
        }
        # Create list of parent B sections
        parentBSections = {}
        for section, value in copy.deepcopy(parentB.data['sections']).items():
            parentBSections[section] = value['details']
        # Create list of subjects that are not in parent A shareables
        for section in parentBSections:
            parentBShareables['sections'][section] = {}
            for id, subject in parentBSections[section].items():
                if not (id in list(parentAShareables['sections'][section].keys())):
                    parentBShareables['sections'][section][id] = subject
        # List of unplaced subjects with or without data
        unplacedSectionSubjects = {}
        # Insert parent A section subjects into chromosome
        for section, subjects in parentAShareables['sections'].items():
            if section not in unplacedSectionSubjects.keys():
                unplacedSectionSubjects[section] = {}
            for subject, details in subjects.items():
                if not len(details):
                    unplacedSectionSubjects[section][subject] = []
                    continue
                if offspring.insertSchedule([details[0], [section], subject, details[1], *details[2:5]]):
                    unplacedSectionSubjects[section][subject] = details
        # Insert parent B section subjects into chromosome
        for section, subjects in parentBShareables['sections'].items():
            if section not in unplacedSectionSubjects.keys():
                unplacedSectionSubjects[section] = {}
            for subject, details in subjects.items():
                if not len(details):
                    unplacedSectionSubjects[section][subject] = []
                    continue
                if offspring.insertSchedule([details[0], [section], subject, details[1], *details[2:5]]):
                    unplacedSectionSubjects[section][subject] = details
        # Attempt to insert unplaced section subjects
        for section, subjects in copy.deepcopy(unplacedSectionSubjects).items():
            for subject, detail in subjects.items():
                if self.generateSubjectPlacement([section], subject):
                    unplacedSectionSubjects[section].pop(subject)
        return offspring

    def mutation(self):
        sections = self.data['sections']
        mutationCandidates = {
            'sections': {},
        }
        
        for section, data in copy.deepcopy(sections).items():
            mutationCandidates['sections'][section] = data[2]
        for section in copy.deepcopy(mutationCandidates['sections']):
            if not len(mutationCandidates['sections'][section]):
                mutationCandidates['sections'].pop(section)
        # Randomly select chromosomes to mutate
        self.progressBarSignal.emit(0)
        self.progressSignal.emit('ایجاد جهش در کروموزوم ها')
        for index, chromosome in enumerate(copy.deepcopy(self.chromosomes)):
            #TODO: Change the random condition of mutation
            if np.random.randint(100) > (self.mutationRate * 100) - 1:
                continue
            self.statusSignal.emit('جهش کروموزوم #{}'.format(index + 1))
            self.progressBarSignal.emit(int((index / len(self.chromosomes)) * 100))
            self.tempChromosome = Chromosome(self.data)
            # Select a gene to mutate
            section = np.random.choice(list(mutationCandidates['sections'].keys()))
            mutating = ['sections', section, np.random.choice(mutationCandidates['sections'][section])]
            # Replicate chromosome except the mutating gene
            for section, subjects in mutationCandidates['sections'].items():
                for subject in subjects:
                    if mutating[0] == 'sections' and mutating[1] == section and mutating[2] == subject:
                        continue
                    details = chromosome.data['sections'][section]['details'][subject]
                    if len(details):
                        self.tempChromosome.insertSchedule([details[0], [section], subject, details[1], *details[2:5]])
            # Generate mutation
            self.generateSubjectPlacement([mutating[1]], mutating[2])
            self.chromosomes[index] = copy.deepcopy(self.tempChromosome)

    def run(self):
        self.progressBarSignal.emit(0)
        self.statusSignal.emit('آماده سازی')
        self.progressSignal.emit('آماده سازی')
        self.initialization() # Initialize chromosomes (Create first Generation)
        generation = 0
        runThread = True
        while (runThread):
            if self.running:
                generation += 1
                self.statusSignal.emit('آماده شدن برای ارزیابی')
                self.progressSignal.emit('آماده شدن برای ارزیابی')
                self.evaluate()
                self.detailsSignal.emit(
                    [generation, len(self.chromosomes), int(self.mutationRate * 100), round(self.averageFitness, 2),
                     round(self.pastAverageFitness, 2), self.highestFitness, self.lowestFitness, round((self.highestFitness / self.settings['maximum_fitness']) * 100,2)])
                if self.highestFitness >= self.settings['maximum_fitness']:
                    self.statusSignal.emit('رسیدن به بالاترین حد فیتنس')
                    self.progressSignal.emit('پایان عملیات')
                    self.progressBarSignal.emit(100)
                    self.operationSignal.emit(1)
                    self.running = runThread = False
                    break
                if self.settings['maximum_generations'] < generation - 1:
                    self.statusSignal.emit('رسیدن به بالاترین حد ایجاد نسل')
                    self.progressSignal.emit('پایان عملیات')
                    self.progressBarSignal.emit(100)
                    self.operationSignal.emit(1)
                    self.running = runThread = False
                    break
                self.statusSignal.emit('بهبود محیط')
                self.progressSignal.emit('بهبود محیط')
                self.adapt()
                self.statusSignal.emit('آماده سازی برای selection')
                self.progressSignal.emit('آماده سازی برای selection')
                self.selection()
                self.statusSignal.emit('ایجاد Cross Over')
                self.progressSignal.emit('ایجاد Cross Over')
                self.crossover()
                self.statusSignal.emit('آماده سازی برای مرحله جهش')
                self.progressSignal.emit('آماده سازی برای مرحله جهش')
                self.mutation()


class Chromosome:
    # data = {
    #     sections: {
    #         id: {
    #             details: {
    #                 subject: [roomId,
    #                   instructorId,
    #                   [day / s],
    #                   startingTS,
    #                   length
    #                 ]
    #             },
    #             schedule: [days]
    #         }
    #     },
    #     instructors && rooms: {
    #         id: [
    #             [days] // Timeslots
    #             [1, None, 1, None, 1, False] // Example
    #             None = Vacant, False = Unavailable
    #         ]
    #     },
    #     unplaced: {
    #         'sections': {
    #             id: [] // Section ID and unplaced subjects
    #         }
    #     }
    # }

    def __init__(self, data):
        self.fitness = 0
        self.fitnessDetails = []
        self.data = {
            'sections': {},
            'instructors': {},
            'rooms': {},
            'unplaced': {
                'sections': {}
            }
        }
        self.rawData = data
        self.settings = Settings.getSettings()
        self.buildChromosome()
        self.launchBreak = self.settings['lunchbreak']

    def buildChromosome(self):
        rawData = self.rawData
        # {id: {details: [subject: []], schedule: [days]}}
        sections = rawData['sections']
        for section in sections:
            self.data['sections'][section] = {'details': {}, 'schedule': []}
            self.data['sections'][section]['details'] = {key: [] for key in sections[section][2]}
            sectionTimetable = []
            for timeslotRow in sections[section][1]:
                sectionTimetable.append([None if day == 'Available' else False for day in timeslotRow])
            self.data['sections'][section]['schedule'] = sectionTimetable
            self.data['unplaced']['sections'][section] = []
        # {id: [days]}
        instructors = rawData['instructors']
        for instructor in instructors:
            instructorTimetable = []
            for timeslotRow in instructors[instructor][2]:
                instructorTimetable.append([None if day == 'Available' else False for day in timeslotRow])
            self.data['instructors'][instructor] = instructorTimetable
        # {id: [days]}
        rooms = rawData['rooms']
        for room in rooms:
            roomTimetable = []
            for timeslotRow in rooms[room][2]:
                roomTimetable.append([None if day == 'Available' else False for day in timeslotRow])
            self.data['rooms'][room] = roomTimetable

    # [roomId, [sectionId], subjectId, instructorID, [day/s], startingTS, length]
    def insertSchedule(self, schedule):
        # Validate schedule details
        isValid = self.validateSchedule(copy.deepcopy(schedule))
        if isValid is not True:
            return isValid
        data = self.data
        # [roomId, instructorId, [day/s], startingTS, length]
        subjectDetails = [schedule[0], schedule[3], schedule[4], schedule[5], schedule[6]]
        # Insert details into section data
        for section in schedule[1]:
            data['sections'][section]['details'][schedule[2]] = subjectDetails
        # Update instructor and room timetable
        for timeslot in range(schedule[5], schedule[5] + schedule[6]):
            for day in schedule[4]:
                if schedule[3]:
                    data['instructors'][schedule[3]][timeslot][day] = schedule[1]
                data['rooms'][schedule[0]][timeslot][day] = schedule[1]
        # False signifies no error in insertion
        return False

    def validateSchedule(self, schedule):
        if not self.isRoomTimeslotAvailable(schedule):
            return 1
        if not self.isInstructorTimeslotAvailable(schedule):
            return 2
        if not self.isSectionTimeslotAvailable(schedule):
            return 3
        if self.launchBreak:
            if not self.isLunchTime(schedule):
                return 4
        return True
        
    # schedule: [roomId, [sectionId], subjectId, instructorID, [day/s], startingTS, length]
    
    # we shouldn't have any Class in [12:40, 13:30]
    def isLunchTime(self, schedule):
        subject_timeslot = [timeslots for timeslots in range(schedule[5], schedule[5] + schedule[6])] # Create list of ‌busy timeslots
        if 6 in subject_timeslot: # if [6,7,8] or [5,6] or ...
            return False
        return True
    
    def isRoomTimeslotAvailable(self, schedule):
        room = self.data['rooms'][schedule[0]]
        for timeslotRow in range(schedule[5], schedule[5] + schedule[6]):
            for day in schedule[4]:
                if room[timeslotRow][day] is not None:
                    return False
        return True

    def isSectionTimeslotAvailable(self, schedule):
        rooms = self.data['rooms']
        sections = self.data['sections']
        # Check for each room if on the given subject range, the section has class
        for room in rooms:
            for timeslotRow in range(schedule[5], schedule[5] + schedule[6]):
                for day in schedule[4]:
                    roomDayTimeslot = rooms[room][timeslotRow][day]
                    #logging.debug(roomDayTimeslot)
                    # Check if timeslot is blank
                    if roomDayTimeslot is None:
                        continue
                    # Check if section is in timeslot
                    # for section in schedule[1]:
                    #     if section in roomDayTimeslot:
                    #         return False
        # Check for section unavailable times
        for section in schedule[1]:
            for timeslotRow in range(schedule[5], schedule[5] + schedule[6]):
                for day in schedule[4]:
                    if sections[section]['schedule'][timeslotRow][day] is not None:
                        return False
        return True

    def isInstructorTimeslotAvailable(self, schedule):
        # Pass if no instructor is set
        if not schedule[3]:
            return True
        instructor = self.data['instructors'][schedule[3]]
        for timeslotRow in range(schedule[5], schedule[5] + schedule[6]):
            for day in schedule[4]:
                if instructor[timeslotRow][day] is not None:
                    return False
        # Check if instructor can still teach
        maxLoad = self.rawData['instructors'][schedule[3]][1] * 2
        for timeslotRow in instructor:
            for day in timeslotRow:
                if day:
                    maxLoad -= 1
        if maxLoad < 0:
            return False
        return True
