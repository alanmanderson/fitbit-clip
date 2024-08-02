
fn = '62045739986.tcx'

tag = '<DistanceMeters>'
end_tag = '</DistanceMeters>'

total_distance = 0
with open(fn, 'r') as fd:
    for line in fd:
        idx = line.find(tag)
        if idx >= 0:
            idx += len(tag)
            print(line)
            end = line.find(end_tag)
            print(idx, end)
            distance = line[idx:end]
            total_distance += float(distance)
    
print(distance)
print(total_distance)
            
