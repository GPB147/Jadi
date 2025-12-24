# Web, Regex, Network Access, Web Scriping, reading and giving part of internet by Regex
# . in Regex means everything, \d means digits, \w means words, \s means whitespace(Space, Tap, Enter) 
# example = \s....\s for asdfwefa in adsf asdfwefa  
# * means 0 to infinity, + means one to infinity, \. means ., () means spacially(group), example = @(.*)\. for gmail in godcraft1380@gmail.com
# [asd] means one of a or s or d, {a,z} means min a and max z, {a} means a times, [^asd] means everything without asd
# ^ means start of line, $ means finish of line, example = ^\d+$ for all phone numbers in fist of line 
# Reading Regex is complecated and writing this is easy, Regex for every language is different 
# Example = ^phone:(\s{11})$ for all phone numbers in a website, Regex are greedy so they want get all and we most to limitaded them
# ? means lasy(limitaded), example = \<.*?\> for a html(without ? Regex get all html)
# in regex we can grow and going to deeper and deeper 
# \n means enter(new line), \t means tab, \r means return 
# Example = ^(\w+)\.*(\w*)\.(\w+) for every names like mohammad.amiri and ehsan.valid.amiri an ...
