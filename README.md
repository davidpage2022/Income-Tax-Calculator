# Income-Tax-Calculator
A little personal program I wrote to help me calculate the totals of my pay slips for an income tax return.

Tax time was looming and I wanted to find out if my payslips added up to the right value. There were a lot of them and I didn't want to count them so I wrote a program to do it. **Note that this is very specific to my payslip files and would be unlikely to work for anyone else.**

My payslips were in PDF format, so I used PyPDF4 to read my data. In retrospect I probably should have used PyPDF2, as that seems to be more mature and better supported.

In the end this project probably took longer than it would take to count the totals manually, but it was good practice and worked.
