# inspiration
小脚本
计算出差补助小脚本

输入平时和休息日的价格

计算补助

# vim学习

========= basic ==========
left : h
right : l
up : k
down : j
undo the previous motion: u
undo the previous motion of the line : U
undo undo : ctrl+R
word : w
end : e
insert : i
append : a
paste : p
replace a char ：r
replace a word : R
copy a word: yw  (paste is p!!)
copy some words : v+y
show the numbers of line : set number
to the line end : $
command prompt : ctrl + d  / tab
($ is means the end of the line)
(w is means word)
(e is means end) 
======== delete ========== d+motion
delete a char: x
delete to word : dw
delete to end : de
left delete : dj
right delete : dl
delete to line : d$
delete line : dd
======= number to execute =====
move to second word : 2w
move to second word end : 2e
to the end of the line : 0
delete 2 words : d2w
delete 2 lines : 2dd
======= the command of place =====
delete a line and paste it below the current line : dd + p
replace a word : r + word
change a word to the end of the word : cw/ce
change to the end of the row : c$
change to second word : c2w
======= location and file status =====
go to the first line : gg
go to the last line : G
show file status : ctrl+g
====== search command ==========
search word in order :  /+word (n:next one ;N:the previous one)
search word in reverse : ?+word
find matched brackets(查找匹配的括号) : %
replace word in this line : :/s/oldword/newword
replace word all : :/s/oldword/newword/g
replace word all and confirm everyone :  :/s/oldword/newword/gc
replace word between line1 and line3 : :1,3/oldword/newword/g
====== others =========
use external instruction in vim : :!+commad(eg: :!ls)
save file in another file : :w+filename(eg: :w test)
merge other file in this file : :r + filename(insert to now location)           
insert mode
insert line under the line : o
insert line upon the line : O
