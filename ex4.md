1. Based on the information given by the sign, the most logical implementation would be using a linear search method.

2. It would take the algorithm 14 steps to find room EY128, assuming we know that rooms only exist in multiples of two, where each step involves walking to and checking the room number of each room to see if it matches the room number we are looking for.

3. This is neither a best-case nor worst-case scenario, as the room we are looking for is near the middle of the so-called array of rooms.

4. With this particular sign and floor layout, the best-case scenario would be looking for room EY100, since it will be found right away because it is the first room in the layout. The worst-case scenario would be looking for room EY138, since it would be the last room in the array of rooms, meaning we checked every room in the floorplan and were only able to find it at the very end of the hall.

5. I would improve the linear search algorithm by implementing a check statement to see if the room number we are looking for is greater than or less than room EY118 (since it is equally distant from the sign). If the room number is lower, tell the algorithm to take the left path and count rooms upwards, and if the number is higher, take the right path, counting rooms downwards. This will reduce the number of rooms needed to be checked by 2, making the new worst-case room EY118, instead of EY138. The sign should be changed to "Rooms 100-118" on the left and "Rooms 118-130" on the right.