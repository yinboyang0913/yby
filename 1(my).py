data=[5,3,8,1,9,2]
def find_max(nums):
    max_val=nums[0]
    for num in nums:
        if num>max_val:
            max_val=num
    return max_val
def sort_list(nums):
    result=list(nums)
    n=len(result)
    for i in range(n-1):
        for j in range(n-1-i):
            if result[j]>result[j+1]:
                result[j],result[j+1]=result[j+1],result[j]
    return result
def search(nums,target):
    for i,val in enumerate(nums):
        if val==target:
            return i
    return -1
if __name__ == "__main__":
    print("原始列表:", data)
    max_value = find_max(data)
    print("最大值:", max_value)
    sorted_data = sort_list(data)
    print("排序后:", sorted_data)
    for i in range(max_value + 1):
        print(f"查找{i}的索引: {search(data, i)}")
