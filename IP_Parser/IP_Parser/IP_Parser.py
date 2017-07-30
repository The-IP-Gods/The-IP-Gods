import json

class IP_Parser(object):
    def __init__(self, filename=None):
        self.ipgod = {}

    def Parse(self):
        file = open('../../Data/ipgod107.csv','r')

        temp_ipgod = []
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
            temp_ipgod.append((key, temp_list))
        self.ipgod = dict(temp_ipgod)

        with open('../../Data/ipgod107.json', 'w') as outfile:
            json.dump(self.ipgod, outfile)

    def Read_In_JSON(self):
        with open('../../Data/ipgod107.json', 'r') as infile:
            self.ipgod = json.load(infile)

    def Search_JSON(self):
        #print keys to select from
        #select key and allow search
        #show results
        ###Not implemented yet

        ipgod_search = self.ipgod.copy()
        search_query = ''

        self.Read_In_JSON()
        x=1
        keys = list(self.ipgod.keys())
        for key in keys:
            print ('{}.'.format(x), key)
            x=x+1
        cat_search_num = input('Search #: ')
        cat_search = keys[(int(cat_search_num))-1]
        search_query = input('Search query: ')
        print(list(self.ipgod.values()))

        #if search_query in the category /= sear_query, remove


if __name__ == '__main__':
    p = IP_Parser()
    p.Parse()
    #p.Read_In_JSON()
    #p.Search_JSON()