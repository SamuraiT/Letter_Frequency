Discription 
===================
By This module, you can compare a statistic date of letter frequency(file name: *frequency_of_letter.txt* )
with the letter frequency from a file or 
just some words or sentences you pass/input.

How to use
--------------------
If you have a file:

use this <code>campare( filename )</code>
where <code>filename</code> should be the file you'd like to examine.

If you don't have a file and would like to examine any setnences or words:

use this <code>compare_string( message )</code>, where <code>message</code>
should be a string you'd like to examine.

There are also other available modules. 

Example
----------------------------
if you'd like to pass a string, do this:

    from letter_frequency import compare_string
    message = 'hello, thank you for trying to run this module. if you have a problem, suggestion, comment,or question,fe    el free to ask me ! thank you'
    compare_string(message)

  
the results will be like this:

    o 12.50 e 12.51 
    e 11.54 t 9.25 
    t 8.65 a 8.04 
    u 6.73 o 7.60 
    n 6.73 i 7.26 
    r 5.77 n 7.09 
    s 4.81 s 6.54  <- bingo
    m 4.81 r 6.12 
    l 4.81 h 5.49 
    i 4.81 l 4.14 
    h 4.81 d 3.99 
    a 4.81 c 3.06 
    y 3.85 u 2.71 
    f 3.85 m 2.53 
    k 2.88 f 2.30 
    g 2.88 p 2.00 
    v 0.96 g 1.96 
    q 0.96 w 1.92 
    p 0.96 y 1.73 
    d 0.96 b 1.54 
    c 0.96 v 0.99 
    b 0.96 k 0.67 
    z 0.00 x 0.19 
    x 0.00 j 0.16 
    w 0.00 q 0.11 
    j 0.00 z 0.09 
  
If you have a file and you'd like to examine, do this:

    from letter_frequency import compare
    
    filename = 'sample.txt'
    compare(filename)

The result would look like the previous one

  
