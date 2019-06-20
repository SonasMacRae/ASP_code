# Name surrounded by stars challenge

In this challenge, the goal is to write an application that prompt the user for an input, before outputting the input surrounded by stars, an example output is:

<img width="291" alt="Screenshot 2019-06-06 at 11 50 36" src="https://user-images.githubusercontent.com/36636474/59027759-caf08680-8851-11e9-8764-106fadc04c2e.png">

You may write this in any langauge, although the solution is written in Python.


## Pseudocode

temp = <b>PROMPT</b> user for input<br/>
output = ""<br/>
<b>LOOP</b> (length(temp)+4):<br/>
&nbsp;&nbsp;&nbsp;output = output + "*"<br/>
<b>END LOOP</b><br/>
<b>PRINT</b>(output)<br/>
<b>PRINT</b>("\* temp *")<br/>
<b>PRINT</b>(output)<br/>
