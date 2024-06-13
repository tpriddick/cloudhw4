# Cloud HW4

This repository has my attempt to build a mapper and reducer for a mapred streaming command. For whatever reason, my mapper will not work. I do not know what is failing, and I really do not know how to even get map reduce to run in a python environment. Please refer to the mapper and reducer in this repository. 

The mapred script I attempted to use was the one from the readme guide:

mapred streaming \
  -input /user/sandbox/books \
  -output /user/sandbox/words \
  -mapper mapper.py \
  -reducer reducer.py \
  -file scripts/mapper.py \
  -file scripts/reducer.py

where I added my own mapper and reducer from this repository. I attempted to use Hamlet's monologue by William Shakespeare, but it did not seem to work. I am sorry, but I really struggled with this assignment.
