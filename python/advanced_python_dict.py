import numpy as np
#from itertools import islice
#import re
import collections
import pprint


class Faculty(object):

    def __init__(self, data):
        """Initializes an instance of Faculty. Parses a faculty data file 
        into an array for a given department.
        """
        f = open(data, 'r')
        lines = f.readlines()[1:]
        stripped = [line.strip('\n') for line in lines]
        parsed = [line.split(',') for line in stripped]
        self.parsed_array = np.asarray(parsed)
        f.close()
      
    def stand_dict(self, value):
        """Standardizes dictionary entries from faculty dataset. Takes self 
        and a list of at least two values as arguments. (Expects value[0] to
        be degree and value[1] to be title.)
        """
        
        # Degree: 
        if 'Ph' in value[0]:
            value[0] = 'Ph.D'
        elif 'Sc' in value[0]:
            value[0] = 'Sc.D'
        elif '0' in value[0]:
            value[0] = ''
        else:
            pass
        
        # Title:
        if 'Assistant' in value[1]:
            value[1] = 'Assistant Professor'
        elif 'Associate' in value[1]:
            value[1] = 'Associate Professor'
        else:
            value[1] = 'Professor'
      
        # Email: no values to standardize yet       
      
    def populate_lastname_dict(self):
        """Populates Faculty.dict with the following key-value pairs:
        keys: last names of faculty
        values: degree, title, email
        """               
        faculty_dict = collections.OrderedDict()      
        
        for row in self.parsed_array: 
            key = row[0].rsplit(None, 1)[-1]
            value = [row[1], row[2], row[3]]        
            Faculty.stand_dict(upenn_biostats, value)
            if key in faculty_dict:
                #faculty_dict[key] = [faculty_dict[key]]          
                faculty_dict[key].append(value) 
            else:
                faculty_dict[key] = value
        
        return faculty_dict
        
    def populate_firstlast_dict(self):
        """Populates Faculty.dict with the following key-value pairs:
        keys: first name, last name (tuple)
        values: degree, title, email (list)
        """               
        professor_dict = collections.OrderedDict()        
        
        for row in self.parsed_array: 
            key = row[0].split()
            key = (key[0], key[-1])
            key = tuple(key)        
            value = [row[1], row[2], row[3]]            
            Faculty.stand_dict(upenn_biostats, value)
            professor_dict[key] = value
       
        return professor_dict    

    def populate_lastfirst_dict(self):
        """Populates Faculty.dict with the following key-value pairs:
        keys: last name, first name (tuple)
        values: degree, title, email (list)
        """  
        professor_dict = collections.OrderedDict()        
        
        for row in self.parsed_array: 
            key = row[0].split()
            key = (key[-1], key[0])
            key = tuple(key)        
            value = [row[1], row[2], row[3]]            
            Faculty.stand_dict(upenn_biostats, value)
            professor_dict[key] = value
       
        return professor_dict    

    def print_dict_first_n(self, d, n):
        c = 0
        print "{",
        for k in d:
            if c >= n:
                break
            else:
                print "%s: [\ \n%s\n]," % (k, d[k])
                c += 1
        print "}"                
        

upenn_biostats = Faculty('/Users/Ben/ds/metis/prework/dsp/python/faculty.csv')    

Q6 = Faculty.populate_lastname_dict(upenn_biostats)
print Faculty.print_dict_first_n(upenn_biostats, Q6, 3)

Q7 = Faculty.populate_firstlast_dict(upenn_biostats)
Faculty.print_dict_first_n(upenn_biostats, Q7, 3)

Q8 = Faculty.populate_lastfirst_dict(upenn_biostats)
Faculty.print_dict_first_n(upenn_biostats, Q8, 3)
