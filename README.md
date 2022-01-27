# TimedDict

The TimedDict is a dictionary that saves the time the key was inserted

When trying to get that key it might have been expired and will throw an error

If trying to insert a key beyond the dictionary size, it will remove the oldest value inserted