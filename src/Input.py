import serial
import numpy as np
import struct

class Input(object):
    def __init__(self, inp='/dev/ttyACM0', baudRate=115200):
        self.ser = serial.Serial(inp, baudRate)
    def read_input(self, width=64, height=8):
        #Get beginning of read_in
        read_char = self.ser.readline()
        while not read_char[:len(read_char)-2]=='A':
            read_char = self.ser.readline()
        #Might have bs'ed this entire line :P
        '''
        full_input = self.ser.read(height * width * 2 + 4)
        full_input_arr= full_input[1:].split(" ")
        '''
        
        full_input_arr = []
        while len(full_input_arr) < width * height:
            read_int = self.ser.readline()
            read_int = read_int[:len(read_int)-2]
            if read_int != '\r' and read_int != ' ' and read_int != '' and read_int != 'A' and read_int != '\n':
                full_input_arr.append(int(read_int))
        #Format of string: (space)(character)*width+1
        #+1 is for extra space at end of line
        arr = np.zeros((0, 0)).astype('float32')
        print full_input_arr, len(full_input_arr)
        for i in range(0, height):
            #Convert it to a string. Need to break by delimiters
            arr_append = np.array(map(int,full_input_arr[i*width:(i+1)*width])).astype('float32')
            print "arr_append: "
            print arr_append,len(arr_append)
            arr = np.append(arr, arr_append)
        arr = np.reshape(arr, (height, width))
        print arr
        return arr

if __name__ == "__main__":
    inp = Input()
    inp.ser.read(1000)
    while True:
        inp.read_input(width=16, height = 5)
