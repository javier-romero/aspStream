# aspStream
A simple approach to stream reasoning in clingo.

# Files
* README.md: This file
* aspStream/
  + stream_controller.py: Controller for stream reasoning in clingo
  + streamed_program_basic.py: Simple streamed program that can be used by the Controller
  + streamed_program_job.py: Simple streamed program for job scheduling that can be used by the Controller
  + job.lp: Logic program for job scheduling
  + stream.lp: Logic program extending job.lp for streamed job scheduling
  + stream_extended: Logic program extending the previous two for extended streamed job scheduling
  + examples: Folder with some examples

# Usage
To run all the examples, simply type:
```bash
$ cd aspStream
$ python stream_controller.py
```

