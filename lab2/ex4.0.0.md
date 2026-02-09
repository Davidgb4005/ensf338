1) I go Left then linear search room by room till i reach 128 
as we dont know that its circular we have no way to know the 128 is reachable
by going right

2) it would take n = 15 steps (assuming first room check is n = 1)

3) this would not be worst case as room 130 would be the last room checked on the left making it the worst case,
as we dont know left and right are linked we assume it would be 2 distinct sets of [100..130] and [130..138]
meaning going left to try and reach 132 would be assumed impossible

4) i would imagine the size as left [100-118],[120-138] and choose left or right depending on which
set contained the room i was looking for allowing me to discard half the choices immediately