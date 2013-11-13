def generate_list(file_path):
    '''
        return list of list's containing file data.'''

    data_list=None   #local variable    
    try:
        file_obj = open(file_path,'r')
        try:
            gen = (line.split(',') for line in file_obj)  #generator, to generate one line each time until EOF (End of File)
            for j,line in enumerate(gen):
                if not data_list:
                    #if dl is None then create list containing n empty lists, where n will be number of columns.
                    data_list = [[] for i in range(len(line))]
                    if line[-1].find('\n'):
                        line[-1] = line[-1][:-1] #to remove last list element's '\n' character

                #loop to convert numbers from string to float, and leave others as strings only
                for i,l in enumerate(line):
                    if i >=2 and j >= 1:
                        data_list[i].append(float(l))
                    else:            
                        data_list[i].append(l)
        except IOError, io_except:
            print io_except
        finally:
            file_obj.close()
    except IOError, io_exception:
        print io_exception

    return data_list

def generate_result(file_path):
    '''
        return list of tuples containing (max price, year, month,
company name).
    '''
    data_list = generate_list(file_path)
    re=[]   #list to store results in tuple formet as follow [(max_price, year, month, company_name), ....]
    if data_list:
        for i,d in enumerate(data_list):
            if i >= 2:
                m = max(data_list[i][1:])      #max_price for the company
                idx = data_list[i].index(m)    #getting index of max_price in the list
                yr = data_list[0][idx]          #getting year by using index of max_price in list
                mon = data_list[1][idx]        #getting month by using index of max_price in list
                com = data_list[i][0]          #getting company_name
                re.append((m,yr,mon,com))
        return re


if __name__ == '__main__':
    file_path = 'C:/data2.csv'
    re = generate_result(file_path)
    print 'result ', re