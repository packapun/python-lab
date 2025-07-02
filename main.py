input = [[1,4],[0,4]]

sorted_input = sorted(input, key= lambda x: x[0])
print(sorted_input)
start = None
end = None
output = []
for interval in sorted_input: 
    curr_start,curr_end = interval[0],interval[1]
    if start is None or end is None:
        print("base case, updating start and end")
        start = curr_start 
        end = curr_end
        print(curr_start,curr_end, start,end)
        continue 
    
    print(curr_start,curr_end, start,end)

    if curr_start > end:
        print("Move to the next interval ")
        # Move to the next interval 
        output.append([start,end])
        start = curr_start 
        end = curr_end
    elif curr_start <= end and curr_end > end:
        print("Update end ")
        end = curr_end

    print(curr_start,curr_end, start,end)

output.append([start,end])

print(output)        




