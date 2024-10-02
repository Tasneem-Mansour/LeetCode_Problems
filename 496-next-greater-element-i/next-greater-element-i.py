class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #### Solution1 -> solved 12/16 testcases####
        # returnList = []
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             if j == len(nums2)-1:
        #                 returnList.append(-1)
        #             else:
        #                 while True:
        #                     if j == len(nums2)-1:
        #                         returnList.append(-1)
        #                         break
        #                     if nums2[j+1] > nums2[j]:
        #                         returnList.append(nums2[j+1])
        #                         break
        #                     j += 1

        # return returnList

        ####Solution 2####
        # res = [-1] * len(nums1)

        # for i in range (len(nums2)):
        #     if nums2[i] in nums1:
        #         index = nums1.index(nums2[i])
        #         for j in range(i+1, len(nums2)):
        #             if nums2[j] > nums2[i]:
        #                 res[index] = nums2[j]
        #                 break
        # return res                                

        ####Solution 3####

        res = [-1] * len(nums1)
        hashIndxNums1 = {}
        for i, n in enumerate(nums1):
            hashIndxNums1[n] = i
        stack = []
        for i in range(len(nums2)):
            
            while stack and nums2[i] > stack[-1]:
                value = stack.pop()
                res[hashIndxNums1[value]] = nums2[i]

            if nums2[i] in hashIndxNums1:
                stack.append(nums2[i])

            # 1 in nums1? yes
            # next num is greater?  no -> append in stack 
                                #   yes -> pop all from stack and aoppend the num in its index in res

        return res


        