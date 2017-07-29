class IP_Parser(object):
    def __init__(self, filename=None):
        pass

    def Parse(self):
        #open file
        #check if already open, else break
        #create dict with keys for each column, and the associated values 
        #each dict key will the name from row one for each respective column
        #each value in the same column will be in a listz   

        file = open('ipgod101.csv','r')

        ipgod = []

        ###setting up dict keys
        #read in the top line
        keys=file.readline()

        #split up top line wth comma ',' as delimter
        keys=keys.rstrip().split(',')
        
        ipgod.append(keys)
        #then loop each element in the "keys" list so that each new 
        for key in keys:
            pass

        for line in file:
            line = file.readline()
            line = line.rstrip().split(',')
            ipgod.append(line)

        return ipgod


if __name__ == '__main__':
    p = IP_Parser()
    p.Parse()