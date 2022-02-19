class find(object):
    def __init__(self,arr):
        self.arr = arr
        self.low = 0
        self.high = len(self.arr) - 1
        self.arr_low_high = [] #Array for save low and high indices
        self.arr_max = [] #Array for save max numbers for each 2 numbers
        self.arr_final_max = [] #Array for save final max
        self.ans = [] #Array for answer

    def findmax(self):
        """We Find Max You Can See It:"""
        
        def f(arr_num,low_index,high_index):
            array = arr_num
            if low_index == high_index - 1 or low_index == high_index: #This if is for choose max numbers
                self.arr_low_high.append(array[int(low_index)])
                self.arr_low_high.append(array[int(high_index)])

                self.arr_max.append(max(self.arr_low_high))

                return self.arr_max
        
            else: #In this else we divide array numbers in small arrays
                mid_index = (low_index + high_index) // 2

                left_max = f(array,low_index,mid_index)
                right_max = f(array,mid_index + 1,high_index)

                self.arr_final_max.append(max(right_max)) #Final max
                
                self.arr_low_high.clear()
                self.arr_max.clear()

                return self.arr_final_max
            
        self.ans = f(self.arr,self.low,self.high) #Call Function
        
        return self.ans
