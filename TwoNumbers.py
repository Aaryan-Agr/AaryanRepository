class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
	Description:
	This functions finds two unique index numbers that when added up gives the value the same as target.
		
	Parameters:
	Nums - List of int
	target - int

	Returns:
	arr - List of all possible indices that match the target (Stored as pairs)
 
		
        '''
        arr = []
	  
	  #Loop to iterate for the first index
        for i in range(len(nums)):
		#Loop to iterate for the second index
            for j in range(len(nums)):
		    #Checking for conditions :- values at index i,j give the same value;i and j are not already in 'arr'; i and j are not the same index
                if nums[i]+nums[j] == target and ((i not in arr)and (j not in arr)) and i!=j:
                    arr.append(i)
                    arr.append(j)

        return arr
