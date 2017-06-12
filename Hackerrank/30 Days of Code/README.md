# [30 Days of Code](https://www.hackerrank.com/domains/tutorials/30-days-of-code)

```python
class Days(object):
  def __init__(self):
    self.day = 0
  def __iter__(self):
    return self
  def __next__(self):
    if self.day == 30:
      raise StopIteration
    else:
      self.day += 1
      return "Day " + str(self.day)

days = Days()
for d in days:
  print(d)
```
