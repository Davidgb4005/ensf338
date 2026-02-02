1. Interpolation search is a vairient of binary search and is better in many aspects 2 of which being its adaptilty because it doesnt always have to start at the midpoint and can make estimates of where the value will be, this leading to the second aspect which is its faster average case time complexity which due to the reasons stated previously will lead to overall faster preformace.

2. If the data is not sorted the algorithm may preform very poorly as its estimates on values are dependeant on the if the data is sorted so if it is not it will lead to worse time complexity than a normal binary search.

3. The following code would need to be modified: ((high - low) / (arr[high] - arr[low])) * (x - arr[low]).

4. Both binary and interpolation search require a sorted dataset so if the dataset provided isnt sorted you will have to use a linear search to go through and check every value in the dataset.

5. In small datasets where dividing the data will cause uneccasary overhead when using interpolation or binary while linear will be able to get through it faster. Also as previously mention in question 4 if the data isnt sorted linear will be more effective.

6. For interpolation search if the data is following a skewed distribution we can apply some data transformation techniqes that will allow us to normalize the data making the search viable or even modify the interpolation formula so that it compensates for the skew. For binary search one way would be to change into an interpolation search as that is already a modified version of a binary search or by using binary search trees we can make sure that the data will always remained sorted for a binary search.
