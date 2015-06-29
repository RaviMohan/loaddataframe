import random
import string

# write row of  n random integers into a file
def generate_integers_only_data_set_row(f,separator,n,a,b):
    #assumed f is an open file handle. closing left to caller
    #f = open(fname,'w')

    #write n-1 ints followed by commas
    for i in range (1,n):
        #the comma should be replaced by the passed in separator
        f.write("%d," % random.randint(a,b))
    #then the n-th int, no comma
    f.write("%d" % random.randint(a,b))
   
def generate_integers_only_data_set(fname, numrows, numcols,a,b,sep):
    f = open(fname,'w')
    #generate n-1 rows
    for i in range (1,numrows):
        generate_data_set_row(f,sep,numcols,a,b)
        f.write("%s" % "\n")
    #generate last row without following \n
    generate_data_set_row(f,sep,numcols,a,b)
    f.close()



    
def generate_random_string_of_size(N):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

# write a row of  n (INT,FLOAT,STRING) sequences into a file
def generate_mixed_type_data_set_row(f,separator,n,a,b):
    #assumed f is an open file handle. closing left to caller
  

    #write n-1  (int + float + string sequence)
    for i in range (1,n):
        #the comma should be replaced by the passed in separator, but for now hardcode comma
        f.write("%d," % random.randint(a,b))
        f.write("%f," % random.random())
        #generate random 3 character string
        f.write("%s," % generate_random_string_of_size(3))

    #then the n-th int+float+string, no following comma
    f.write("%d," % random.randint(a,b))
    f.write("%f," % random.random())
    f.write("%s" % generate_random_string_of_size(3))

def generate_mixed_types_data_set(fname, numrows, numcols,a,b,sep):
    f = open(fname,'w')
    #generate n-1 rows
    for i in range (1,numrows):
        generate_mixed_type_data_set_row(f,sep,numcols,a,b)
        f.write("%s" % "\n")
    #generate last row without following \n
    generate_mixed_type_data_set_row(f,sep,numcols,a,b)
    f.close()

 
#generate_integers_only_data_set("hundredmillionrowdataset.csv", 100000000,25,1,1000,",")


# generates 24 column dataset . 8 sequences of int, float, string
#generate_mixed_types_data_set("mixedthousandrowdataset.csv", 1000,8,1,1000,",")
#generate_mixed_types_data_set("mixedtenthousandrowdataset.csv", 10000,8,1,1000,",")
#generate_mixed_types_data_set("mixedhundredthousandrowdataset.csv", 100000,8,1,1000,",")
#generate_mixed_types_data_set("mixedmillionrowdataset.csv", 1000000,8,1,1000,",")
#generate_mixed_types_data_set("mixedtenmillionrowdataset.csv", 10000000,8,1,1000,",")

#generate_mixed_types_data_set("mixedhundredmillionrowdataset.csv", 100000000,8,1,1000,",")


