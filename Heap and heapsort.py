import math

def GIF(n):
    return int(math.floor(n))  

class heap_Node:                    
    def __init__(self):
        self.value = None
        self.parent = None
        self.left = None
        self.right = None

class heap:                         
    def __init__(self):
        self.root = None
        self.height = 0
        self.heap_array = []

    def build(self, data):
        length = len(data)
        self.height = length

        for i in range(0, length):
            new = heap_Node()
            new.value = data[i]
            
            if (i%2 == 0):
                new.parent = data[GIF(i/2) - 1]
            else:
                new.parent = data[GIF(i/2)]
            
            if (i < GIF(length/2) - 1):
                new.left = data[2*i + 1]
                
            if (i < GIF(length/2) - 1):
                new.right = data[2*i + 2]
                
            if (i == GIF(length/2) - 1):
                if (length % 2 != 0):
                    new.left = data[-2]
                    new.right = data[-1]
                else:
                    new.left = data[-1]
                    new.right = None
                
            self.heap_array.append(new)

        self.root = self.heap_array[0].value
        
        self.heap_array[0].parent = None
            
    def left_index(self, value):           
        return (2*value + 1)
                
    def right_index(self, value):          
        return (2*value + 2)

    def max_heapify(self, i):               
        largest = i
        
        l = self.left_index(i)
        r = self.right_index(i)

        if ((l < self.height) and (self.heap_array[l].value > self.heap_array[i].value)):
            largest = l

        if ((r < self.height) and (self.heap_array[r].value > self.heap_array[largest].value)):
            largest = r

        if largest != i:
            self.heap_array[i].value, self.heap_array[largest].value = self.heap_array[largest].value, self.heap_array[i].value

            if largest == l:
                self.heap_array[i].left = self.heap_array[largest].value
            else:
                self.heap_array[i].right = self.heap_array[largest].value

            if ((i % 2 != 0) and (i < self.height)):
                self.heap_array[GIF(i/2)].left = self.heap_array[i].value
                
                if (largest % 2 != 0):
                    self.heap_array[largest].parent = self.heap_array[i].value
                    if (largest < self.height - 1):
                        self.heap_array[largest + 1].parent = self.heap_array[i].value
                        
                else:
                    self.heap_array[largest - 1].parent = self.heap_array[i].value
                    self.heap_array[largest].parent = self.heap_array[i].value

                
            if ((i % 2 == 0) and (i < self.height)):
                self.heap_array[GIF(i/2) - 1].right = self.heap_array[i].value
                
                if (largest % 2 != 0):
                    self.heap_array[largest].parent = self.heap_array[i].value
                    if (largest < self.height - 1):
                        self.heap_array[largest + 1].parent = self.heap_array[i].value
                else:
                    self.heap_array[largest - 1].parent = self.heap_array[i].value
                    self.heap_array[largest].parent = self.heap_array[i].value

            l_l = self.left_index(largest)
            r_l = self.right_index(largest)

            if (l_l < self.height):
                if (self.heap_array[l_l].value is not None):
                    self.heap_array[l_l].parent = self.heap_array[largest].value
            if (r_l < self.height):
                if (self.heap_array[r_l].value is not None): 
                    self.heap_array[r_l].parent = self.heap_array[largest].value

            self.max_heapify(largest)

    def min_heapify(self, i):            
        largest = i
        
        l = self.left_index(i)
        r = self.right_index(i)

        if ((l < self.height) and (self.heap_array[l].value < self.heap_array[i].value)):
            largest = l

        if ((r < self.height) and (self.heap_array[r].value < self.heap_array[largest].value)):
            largest = r

        if largest != i:
            self.heap_array[i].value, self.heap_array[largest].value = self.heap_array[largest].value, self.heap_array[i].value

            if largest == l:
                self.heap_array[i].left = self.heap_array[largest].value
            else:
                self.heap_array[i].right = self.heap_array[largest].value

            if ((i % 2 != 0) and (i < self.height)):
                self.heap_array[GIF(i/2)].left = self.heap_array[i].value
                
                if (largest % 2 != 0):
                    self.heap_array[largest].parent = self.heap_array[i].value
                    if (largest < self.height - 1):
                        self.heap_array[largest + 1].parent = self.heap_array[i].value
                        
                else:
                    self.heap_array[largest - 1].parent = self.heap_array[i].value
                    self.heap_array[largest].parent = self.heap_array[i].value

                
            if ((i % 2 == 0) and (i < self.height)):
                self.heap_array[GIF(i/2) - 1].right = self.heap_array[i].value
                
                if (largest % 2 != 0):
                    self.heap_array[largest].parent = self.heap_array[i].value
                    if (largest < self.height - 1):
                        self.heap_array[largest + 1].parent = self.heap_array[i].value
                else:
                    self.heap_array[largest - 1].parent = self.heap_array[i].value
                    self.heap_array[largest].parent = self.heap_array[i].value

            l_l = self.left_index(largest)
            r_l = self.right_index(largest)

            if (l_l < self.height):
                if (self.heap_array[l_l].value is not None):
                    self.heap_array[l_l].parent = self.heap_array[largest].value
            if (r_l < self.height):
                if (self.heap_array[r_l].value is not None): 
                    self.heap_array[r_l].parent = self.heap_array[largest].value

            self.min_heapify(largest)


    def build_max_heap(self):

        if (self.height % 2 != 0):
            for i in range(GIF(self.height/2) + 1, -1, -1):
                self.max_heapify(i)
            self.heap_array[self.height - 1].left = None
            self.heap_array[self.height - 1].right = None

        else:
            for i in range(GIF(self.height/2), -1, -1):
                self.max_heapify(i)
            self.heap_array[self.height - 1].left = None
            self.heap_array[self.height - 1].right = None
        self.root = self.heap_array[0].value

    def build_min_heap(self):

        if (self.height % 2 != 0):
            for i in range(GIF(self.height/2) + 1, -1, -1):
                self.min_heapify(i)
            self.heap_array[self.height - 1].left = None
            self.heap_array[self.height - 1].right = None

        else:
            for i in range(GIF(self.height/2), -1, -1):
                self.min_heapify(i)
            self.heap_array[self.height - 1].left = None
            self.heap_array[self.height - 1].right = None
        self.root = self.heap_array[0].value
        
def max_array(array):
    max_heap = heap()
    max_heap.build(array)
    max_heap.build_max_heap()
    new_array = []
    for  i in range(0, max_heap.height):
        new_array.append(max_heap.heap_array[i].value)
    return new_array

def min_array(array):
    min_heap = heap()
    min_heap.build(array)
    min_heap.build_min_heap()
    new_array = []
    for  i in range(0, min_heap.height):
        new_array.append(min_heap.heap_array[i].value)
    return new_array

def desc_heapsort(array):
    
    start_length = len(array)
    start_array = min_array(array)
    array[-1] = start_array[0]
    
    for i in range(1, start_length - 1):
        start_array = start_array[1:]
        do_array = min_array(start_array)
        array[start_length - i - 1] = do_array[0]
        start_array = do_array
        
        if (len(start_array) == 2):
            array[0] = start_array[1]
     
    return array

def incs_heapsort(array):
    
    start_length = len(array)
    start_array = max_array(array)
    array[-1] = start_array[0]
    
    for i in range(1, start_length - 1):
        start_array = start_array[1:]
        do_array = max_array(start_array)
        array[start_length - i - 1] = do_array[0]
        start_array = do_array
        
        if (len(start_array) == 2):
            array[0] = start_array[1]
     
    return array

'''def ins_minh(array, k):
    array.append(k)
    return incs_heapsort(array)

def ins_maxh(array, k):
    array.append(k)
    return desc_heapsort(array)

def del_minh(array, k):
    array.remove(array[k])
    return incs_heapsort(A)

def del_maxh(array, k):
    array.remove(array[k])
    return desc_heapsort(A)

def del_min(array):
    incs_heapsort(array)
    array.remove(array[0])
    return array

def del_max(array):
    desc_heapsort(array)
    array.remove(array[0])
    return array

def minh_cost(array):
    new_array = incs_heapsort(array)
    cost = 0
    cost_array = []
    cost_sum = new_array[0]
    
    for i in range(1, len(new_array)):
        cost_sum += new_array[i]
        cost_array.append(cost_sum)

    for j in range(0, len(cost_array)):
        cost += cost_array[j]
        
    return cost

def maxh_cost(array):
    new_array = desc_heapsort(array)
    cost = 0
    cost_array = []
    cost_sum = new_array[0]
    
    for i in range(1, len(new_array)):
        cost_sum += new_array[i]
        cost_array.append(cost_sum)

    for j in range(0, len(cost_array)):
        cost += cost_array[j]
        
    return cost

def K_largest(array, K):
    new_array = desc_heapsort(array)

    for i in range(0, K):
        print(new_array[i], end = ' ')

def K_smallest(array, K):
    new_array = incs_heapsort(array)

    for i in range(0, K):
        print(new_array[i], end = ' ')'''




        
        
        
        

    




   

    

    
