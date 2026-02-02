I go Left then linear search room by room till i reach 128 
as we dont know that its circular we have no way to know the 128 is reachable
by going right

it would take n = 15 steps

this would not be worst case as  room 130 would be the last room checked on the left
as we dont know left and right are linked we assume it could be 2 disjoint sets of [100..130] and [130..138]
path and worse case for the left path is 130 and for right would be 138

i would imagine the size as left [100-118],[120-138]
