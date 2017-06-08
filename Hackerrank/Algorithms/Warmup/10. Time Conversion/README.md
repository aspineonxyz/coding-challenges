# [Time Conversion](https://www.hackerrank.com/challenges/time-conversion)

Given a time in [12-hour AM/PM format](https://en.wikipedia.org/wiki/12-hour_clock), convert it to military (24-hour) time.

__Note:__ Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

#### Input Format
A single string containing a time in 12-hour clock format (i.e.: __hh:mm:ssAM__ or __hh:mm:ssPM__), where __*01 <= hh <= 12*__ and __*00 <= mm, ss <= 59*__.

#### Output Format
Convert and print the given time in 24-hour format, where __*00 <= hh <= 23*__.

#### Sample Input
```
07:05:45PM
```
#### Sample Output
```
19:05:45
```
