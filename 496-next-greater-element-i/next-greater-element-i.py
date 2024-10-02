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
        res = [-1] * len(nums1)

        for i in range (len(nums2)):
            if nums2[i] in nums1:
                index = nums1.index(nums2[i])
                for j in range(i+1, len(nums2)):
                    if nums2[j] > nums2[i]:
                        res[index] = nums2[j]
                        break

        return res                                

        