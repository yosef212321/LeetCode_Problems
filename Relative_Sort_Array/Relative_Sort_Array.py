class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        list1 = []
        list2 = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    list1.append(arr2[i])
        for k in arr1:
            if k not in list1:
                list2.append(k)
        list2.sort()
        list1.extend(list2)
        return list1
