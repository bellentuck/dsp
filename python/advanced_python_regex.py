import numpy as np


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
        
        self.emails = [ ]

    def print_stats(self):
        """Displays array contents.
        """
        return self.parsed_array

    def degree_types(self):
        """Counts degree type instances for different categories.
        """
        degrees = {'Ph.D': 0, 'Sc.D': 0}        
        pedigree = np.asarray([line[1].split() for line in \
                   self.parsed_array])   
                   
        for p in pedigree:
            for title in p: 
                if 'Ph' in title: 
                    degrees['Ph.D'] += 1
                elif 'Sc' in title:          
                    degrees['Sc.D'] += 1
                elif '0' in title:
                    continue 
                elif title in degrees:
                    degrees[title] += 1
                else:
                    degrees[title] = 1
        return degrees

    def title_types(self):
        """Counts job title instances for different categories.
        """    
        titles = { }        
        for line in self.parsed_array:
            if line[2] in titles:
                titles[line[2]] += 1
            elif line[2] == 'Assistant Professor is Biostatistics':
                titles['Assistant Professor of Biostatistics'] += 1
            else:
                titles[line[2]] = 1
        return titles

    def frequencies(self, types):
        """Counts categories. Produces a dictionary of categories \
        and their frequencies.
        """
        total = 0
        freq = {}
        for category in types:
            total += types[category]
            # Test: print category 
            # Test: print types[category] 
            # Test: print total 
        for category in types:
            #freq[category] = float(types[category]) / float(total)
            freq[category] = '%f%%' % ((float(types[category]) / 
                             float(total))*100.0)
        return freq

    def get_emails(self):
        """Constructs a list of email addresses for faculty from a given
        department array.
        """
        for line in self.parsed_array:
            self.emails.append(line[3])
        return self.emails
             
    def diff_emails(self):
        """Identifies unique email domains from the email list for a given 
        department's faculty.
        """
        local_emails = [email.split('@') for email in self.emails]
        domains = set()
        domains = {d[1] for d in local_emails if d[1] not in domains}
        return domains

# Test: call up the Faculty class on UPenn BioStats Dept
upenn_biostats = Faculty('/Users/Ben/ds/metis/prework/dsp/python/faculty.csv')
print '\n'
# Q1a
print "How many different types of degrees are held by faculty? \
%d" % len(Faculty.degree_types(upenn_biostats))  
# Q1b
print "Frequency of degrees:", Faculty.frequencies(
                                                  upenn_biostats, Faculty.\
                                                  degree_types(upenn_biostats)
                                                  )
print '\n'
# Q2a
print "How many different kinds of titles are held by faculty? \
%d" % len(Faculty.title_types(upenn_biostats)) 
# Q2b
print "Frequency of titles:", Faculty.frequencies(
                                                 upenn_biostats, Faculty.\
                                                 title_types(upenn_biostats)
                                                 ) 
print '\n'                                                
# Q3
Faculty.get_emails(upenn_biostats)
print "Faculty email addresses:", upenn_biostats.emails
print '\n'
# Q4
print "How many different email domains are there? \
%d" % len(Faculty.diff_emails(upenn_biostats))
print "Unique email domains:", Faculty.diff_emails(upenn_biostats)
