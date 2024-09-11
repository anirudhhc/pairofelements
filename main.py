# Create a class
class pair_elements:

    def twoSums(self,nums,target):
        # Create a empty dictionary
        hello={}

        # itirate through tuple
        for i, num in enumerate(nums):
            if target-num in hello:
                return (hello[target-num],i)
            hello[num]=i
# Take input from the user
value=int(input("Enter the sum for which you want to search"))
print("index1=%d, index2=%d")
pair_elements().twoSum((10,20,30,40,50,60,70),value)

