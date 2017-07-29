import json

class IP_Parser(object):
    def __init__(self, filename=None):
        pass

    def Parse(self):
        #open file
        #check if already open, else break
        #create dict with keys for each column, and the associated values 
        #each dict key will the name from row one for each respective column
        #each value in the same column will be in a listz   

        file = open('../../Data/ipgod101.csv','r')

        ipgod = []
        read_lines = []

        ###setting up dict keys
        #read in the top line
        keys=file.readline()

        #split up top line wth comma ',' as delimter
        keys=keys.rstrip().split(',')
        
        #ipgod.append(keys)
        #then loop each element in the "keys" list so that each new 
        for key in keys:
            pass

        for line in file:
            line = line.rstrip().split(',')
            read_lines.append(line)

        for key in keys:
            temp_list = []
            for line in read_lines:
                if not line:
                    break
                temp_list.insert(0, line.pop(0))
            ipgod.insert(0,(key, temp_list))
        b = dict(ipgod)
        with open('../../Data/ipgod101JSON.json', 'w') as outfile:
            json.dump(b, outfile)

    def Read_In_JSON(self):
        ipgod = {}
        with open('../../Data/ipgod101JSON.json', 'r') as infile:
            ipgod = json.load(infile)
            
        pass


if __name__ == '__main__':
    p = IP_Parser()
    #p.Parse()
    p.Read_In_JSON()