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

    def get_emails(self):
        """Constructs a list of email addresses for faculty from a given
        department array.
        """
        for line in self.parsed_array:
            self.emails.append(line[3])
        return self.emails
             
    def write_to_csv(self):
        csv = open('/Users/Ben/ds/metis/prework/dsp/python/emails.csv', 'w')
        csv.truncate()
        for email in self.emails:
            csv.write(email)
            csv.write('\n')
        csv.close()

upenn_biostats = Faculty('/Users/Ben/ds/metis/prework/dsp/python/faculty.csv')
Faculty.get_emails(upenn_biostats)
Faculty.write_to_csv(upenn_biostats)
