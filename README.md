This program will determine if the word carries the attribute of "beautiful." A string is defined as "beautiful" if no letter beats a higher letter in frequency. 
Highest letters are at the top of the alphabet, A being highest, Z being lowest. 
If two letters tie in frequency, the word can still be beautiful. If A and B appear in equal frequency, the word can still be beautiful.
If B appears more than A, the word cannot be beautiful.
If any other lower letter appears more than any higher letter, the word cannot be beautiful.
The input string at the top is only a sample; that can be modified.
The program works by sorting the input string, counting the frequency sorted, looping to ensure that the max-frequency is always held by the earlier of any two sorted
