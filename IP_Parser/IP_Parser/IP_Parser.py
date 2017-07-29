import json

class IP_Parser(object):
    def __init__(self, filename=None):
        pass

    def Parse(self):
        file = open('../../Data/ipgod101_SmallSizeSample.csv','r')

        ipgod = []
        read_lines = []

        ###setting up dict keys
        #read in the top line
        keys=file.readline()

        #split up top line wth comma ',' as delimter
        keys=keys.rstrip().split(',')

        #read in data and split with comma ',' as delimeter.
        for line in file:
            line = line.rstrip().split(',')
            read_lines.insert(0,line)

        #for every key, pop the data in the same column and append
        for key in keys:
            temp_list = []
            for line in read_lines:
                if not line:
                    break
                temp_list.insert(0, line.pop(0))
            ipgod.append((key, temp_list))
        b = dict(ipgod)

        with open('../../Data/ipgod101_SmallSampleSize.json', 'w') as outfile:
            json.dump(b, outfile)

    def Read_In_JSON(self):
        ipgod = {}
        with open('../../Data/ipgod101JSON.json', 'r') as infile:
            ipgod = json.load(infile)
        
        pass


if __name__ == '__main__':
    p = IP_Parser()
    p.Parse()
    #p.Read_In_JSON()