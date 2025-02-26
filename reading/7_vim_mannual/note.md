

Another way to move to a line is using the "%" command with a count.  For
example "50%" moves you to halfway the file.  "90%" goes to near the end.



The "zt" command puts the cursor line at the top, "zb" at the bottom.  There
are a few more scrolling commands, see |Q_sc|.  To always keep a few lines of
context around the cursor, use the 'scrolloff' option.



You can use this command to get a list of marks:

	:marks

You will notice a few special marks.  These include:

	''	The cursor position before doing a jump
	"	The cursor position when last editing the file
	[	Start of the last change
	]	End of the last change






GOING TO THE OTHER SIDE

If you have selected some text in Visual mode, and discover that you need to
change the other end of the selection, use the "o" command (Hint: o for other
end).  The cursor will go to the other end, and you can move the cursor to
change where the selection starts.  Pressing "o" again brings you back to the
other end.

When using blockwise selection, you have four corners.  "o" only takes you to
one of the other corners, diagonally.  Use "O" to move to the other corner in
the same line.

Note that "o" and "O" in Visual mode work very differently from Normal mode,
where they open a new line below or above the cursor.


: options
cursorline	highlight the screen line of the cursor
	(local to window)
 	set cul	nocul

splitbelow	a new window is put below the current one
 	set sb	nosb
splitright	a new window is put right of the current one
 	set spr	nospr

showcmd	show (partial) command keys in the status line
 	set sc	nosc
clipboard	"unnamed" to use the * register like unnamed register
	"autoselect" to always put selected text on the clipboard
 	set cb=unnamedplus
backspace	specifies what <BS>, CTRL-W, etc. can do in Insert mode
 	set bs=indent,eol,start
complete	specifies how Insert mode completion works for CTRL-N and CTRL-P
	(local to buffer)
 	set cpt=.,w,b,u,t,i
completeopt	whether to use a popup menu for Insert mode completion
 	set cot=menu,preview
showmatch	when inserting a bracket, briefly jump to its match
 	set sm	nosm
matchpairs	list of pairs that match for the "%" command
	(local to buffer)
 	set mps=(:),{:},[:],<:>
autoread	automatically read a file when it was modified outside of Vim
	(global or local to buffer)
 	set noar	ar
shell	name of the shell program used for external commands
 	set sh=/bin/bash
shellcmdflag	argument for 'shell' to execute a command
 	set shcf=-c
encoding	character encoding used in Vim: "latin1", "utf-8",
	"euc-jp", "big5", etc.
 	set enc=utf-8
fileencoding	character encoding for the current file
	(local to buffer)
 	set fenc=utf-8
fileencodings	automatically detected character encodings
 	set fencs=ucs-bom,utf-8,default,latin1
virtualedit	when to use virtual editing: "block", "insert", "all"
	and/or "onemore"
 	set ve=
gdefault	use the 'g' flag for ":substitute"
 	set gd	nogd
sessionoptions	list of words that specifies what to put in a session file
 	set ssop=blank,buffers,curdir,folds,help,options,tabpages,winsize,terminal
viewoptions	list of words that specifies what to save for :mkview
 	set vop=folds,options,cursor,curdir
viewdir	directory where to store files with :mkview
 	set vdir=/home/widehyo/.vim/view

set autoread
set cursorline
set gdefault


*07.3*	Jumping from file to file

To quickly jump between two files, press CTRL-^ (on English-US keyboards the ^
is above the 6 key).  Example: >

PREDEFINED MARKS

After jumping to another file, you can use two predefined marks which are very
useful: >

	`"

This takes you to the position where the cursor was when you left the file.
Another mark that is remembered is the position where you made the last
change: >

	`.


   So far we were using marks with a lowercase letter.  There are also marks
with an uppercase letter.  These are global, they can be used from any file.
For example suppose that we are editing the file "foo.txt".  Go to halfway
down the file ("50%") and place the F mark there (F for foo): >

	50%mF

Now edit the file "bar.txt" and place the B mark (B for bar) at its last line:
>
	GmB

Now you can use the "'F" command to jump back to halfway foo.txt.  Or edit yet
another file, type "'B" and you are at the end of bar.txt again.

You can delete the stuff you don't need.  Now you need to save the file under
a new name.  The ":saveas" command can be used for this: >

	:saveas move.c

But ":close" prevents you from accidentally exiting Vim when you close the
last window.

If you have opened a whole bunch of windows, but now want to concentrate on
one of them, this command will be useful: >

If you have opened a whole bunch of windows, but now want to concentrate on
one of them, this command will be useful: >

	:only

The ":split" command can take a number argument.  If specified, this will be
the height of the new window.  For example, the following opens a new window
three lines high and starts editing the file alpha.c: >

	:3split alpha.c

To increase the size of a window: >
To decrease it: >

	CTRL-W +
	CTRL-W -

	CTRL-W 10 <
	CTRL-W 10 >

	{height}CTRL-W _

That's: a number {height}, CTRL-W and then an underscore (the - key with Shift
on English-US keyboards).
   To make a window as high as it can be, use the CTRL-W _ command without a
count.


	CTRL-W t	move to the TOP window
	CTRL-W b	move to the BOTTOM window

	CTRL-W K

This uses the uppercase letter K.  What happens is that the window is moved to
the very top.  You will notice that K is again used for moving upwards.
	CTRL-W H	move window to the far left
	CTRL-W J	move window to the bottom
	CTRL-W L	move window to the far right


DIFFING IN VIM

Another way to start in diff mode can be done from inside Vim.  Edit the
"main.c" file, then make a split and show the differences: >

	:edit main.c
	:vertical diffsplit main.c~
	:edit main.c
	:vertical diffpatch main.c.diff

JUMPING TO CHANGES

When you have disabled folding in some way, it may be difficult to find the
changes.  Use this command to jump forward to the next change: >

	]c

To go the other way use: >

	[c

REMOVING CHANGES

You can move text from one window to the other.  This either removes
differences or adds new ones.  Vim doesn't keep the highlighting updated in
all situations.  To update it use this command: >

	:diffupdate

To remove a difference, you can move the text in a highlighted block from one
window to another.  Take the "main.c" and "main.c~" example above.  Move the
cursor to the left window, on the line that was deleted in the other window.
Now type this command: >

	dp

The change will be removed by putting the text of the current window in the
other window.  "dp" stands for "diff put".
   You can also do it the other way around.  Move the cursor to the right
window, to the line where "changed" was inserted.  Now type this command: >

	do

The change will now be removed by getting the text from the other window.
Since there are no changes left now, Vim puts all text in a closed fold.
"do" stands for "diff obtain".  "dg" would have been better, but that already
has a different meaning ("dgg" deletes from the cursor until the first line).

usr_9.txt <<< gVim, pass


	:%s/Professor/Teacher/c

Vim finds the first occurrence of "Professor" and displays the text it is
about to change.  You get the following prompt: >

	replace with Teacher (y/n/a/q/l/^E/^Y)?

	y		Yes; make this change.
	n		No; skip this match.
	a		All; make this change and all remaining ones without
			further confirmation.
	q		Quit; don't make any more changes.
	l		Last; make this change and then quit.
	CTRL-E		Scroll the text one line up.
	CTRL-Y		Scroll the text one line down.


USING A PATTERN IN A RANGE

Suppose you are editing a chapter in a book, and want to replace all
occurrences of "grey" with "gray".  But only in this chapter, not in the next
one.  You know that only chapter boundaries have the word "Chapter" in the
first column.  This command will work then: >

	:?^Chapter?,/^Chapter/s=grey=gray=g

You can see a search pattern is used twice.  The first "?^Chapter?" finds the
line above the current position that matches this pattern.  Thus the ?pattern?
range is used to search backwards.  Similarly, "/^Chapter/" is used to search
forward for the start of the next chapter.
   To avoid confusion with the slashes, the "=" character was used in the
substitute command here.  A slash or another character would have worked as
well.

와 vim에서 앞뒤로 찾아서 범위를 지정하는게 되네


ADD AND SUBTRACT

There is a slight error in the above command: If the title of the next chapter
had included "grey" it would be replaced as well.  Maybe that's what you
wanted, but what if you didn't?  Then you can specify an offset.
   To search for a pattern and then use the line above it: >

	/Chapter/-1

You can use any number instead of the 1.  To address the second line below the
match: >

	/Chapter/+2

The offsets can also be used with the other items in a range.  Look at this
one: >

	:.+3,$-5
	:.,.+4

This specifies the range that starts three lines below the cursor and ends
five lines before the last line in the file.


ex command로 범위에 offset으로 찾을 수 있네


The '< and '> are actually marks, placed at the start and end of the Visual
selection.  The marks remain at their position until another Visual selection
is made.  Thus you can use the "'<" command to jump to position where the
Visual area started.  And you can mix the marks with other items: >

이거 마크였니


	:g+//+s/foobar/barfoo/g

Other commands that change the characters in the block:

	~	swap case	(a -> A and A -> a)
	U	make uppercase  (a -> A and A -> A)
	u	make lowercase  (a -> a and A -> a)

The "J" command joins all selected lines together into one line.  Thus it
removes the line breaks.  Actually, the line break, leading white space and
trailing white space is replaced by one space.  Two spaces are used after a


READING COMMAND OUTPUT

To read the contents of the current directory into the file, use this:

on Unix: >
	:read !ls


  Swap file ".main.c.swp" already exists! ~
  [O]pen Read-Only, (E)dit anyway, (R)ecover, (Q)uit, (A)bort, (D)elete it: ~

O  Open the file readonly.  Use this when you just want to view the file and
   don't need to recover it.  You might want to use this when you know someone
   else is editing the file, but you just want to look in it and not make
   changes.

E  Edit the file anyway.  Use this with caution!  If the file is being edited
   in another Vim, you might end up with two versions of the file.  Vim will
   try to warn you when this happens, but better be safe than sorry.

R  Recover the file from the swap file.  Use this if you know that the swap
   file contains changes that you want to recover.

Q  Quit.  This avoids starting to edit the file.  Use this if there is another
   Vim editing the same file.
      When you just started Vim, this will exit Vim.  When starting Vim with
   files in several windows, Vim quits only if there is a swap file for the
   first one.  When using an edit command, the file will not be loaded and you
   are taken back to the previously edited file.

A  Abort.  Like Quit, but also abort further commands.  This is useful when
   loading a script that edits several files, such as a session with multiple
   windows.

D  Delete the swap file.  Use this when you are sure you no longer need it.
   For example, when it doesn't contain changes, or when the file itself is
   newer than the swap file.
      On Unix this choice is only offered when the process that created the
   swap file does not appear to be running.


	:recover

use the "\<" item to match the start of a word:
Use "\>" to match the end of a word:

"thirtyfour"

	:%s/\<four/4/g
	:%s/\<four\>/4/g

REPLACING IN SEVERAL FILES

	vim *.cpp		Start Vim, defining the argument list to
				contain all the C++ files.  You are now in the
				first file.
	qq			Start recording into the q register
	:%s/\<GetResp\>/GetAnswer/g
				Do the replacements in the first file.
	:wnext			Write this file and move to the next one.
	q			Stop recording.
	@q			Execute the q register.  This will replay the
				substitution and ":wnext".  You can verify
				that this doesn't produce an error message.
	999@q			Execute the q register on the remaining files.

*12.4*	Reverse line order

This also works on a range of lines.  First move to above the first line and
mark it with "mt".  Then move the cursor to the last line in the range and
type: >

	:'t+1,.g/^/m 't

simple way: Move the cursor to the word you want to find help on and press >

	K

*12.7*	Trim blanks
	:%s/\s\+$//
