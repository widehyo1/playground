

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


	:browse oldfiles
<	1: ~/.viminfo ~
	2: ~/text/resume.txt ~
	3: /tmp/draft ~
	-- More --

You get the same list of files as with |:oldfiles|.  If you want to edit
"resume.txt" first press "q" to stop the listing.  You will get a prompt:

	Type number and <Enter> (empty cancels): ~

Type "2" and press <Enter> to edit the second file.

   The following command creates a session file: >

	:mksession vimbook.vim

Later if you want to restore this session, you can use this command: >

	:source vimbook.vim

If you want to start Vim and restore a specific session, you can use the
following command: >

	vim -S vimbook.vim

	:wall
	:mksession! ~/.vim/secret.vim
	:source ~/.vim/boring.vim

	:mksession! ~/.vim/secret.vim
	:wviminfo! ~/.vim/secret.viminfo

And to restore this again: >

	:source ~/.vim/secret.vim
	:rviminfo! ~/.vim/secret.viminfo

	:mkview
	:loadview

	:mkview ~/.vim/main.vim
	:source ~/.vim/main.vim

WINDOW LOCAL DIRECTORY

When you split a window, both windows use the same current directory.  When
you want to edit a number of files somewhere else in the new window, you can
make it use a different directory, without changing the current directory in
the other window.  This is called a local directory. >

	:pwd
	/home/Bram/VeryLongFileName
	:split
	:lcd /etc
	:pwd
	/etc
	CTRL-W w
	:pwd
	/home/Bram/VeryLongFileName

TAB LOCAL DIRECTORY

directory of the current tab page using the `:tcd` command. All the windows in

You are editing a C program that contains this line:

	#include "inits.h" ~

You want to see what is in that "inits.h" file.  Move the cursor on the name
of the file and type: >

	gf

Vim will find the file and edit it.
   What if the file is not in the current directory?  Vim will use the 'path'
option to find the file.  This option is a list of directory names where to
look for your file.

	:find inits.h

Vim will then use the 'path' option to try and locate the file.  This is the
same as the ":edit" command, except for the use of 'path'.

To open the found file in a new window use CTRL-W f instead of "gf", or use
":sfind" instead of ":find".

   To open a buffer in a new window: >

	:sbuffer 3

*23.1*	DOS, Mac and Unix files

Back in the early days, the old Teletype machines used two characters to
start a new line.  One to move the carriage back to the first position
(carriage return, <CR>), another to move the paper up (line feed, <LF>).
   When computers came out, storage was expensive.  Some people decided that
they did not need two characters for end-of-line.  The UNIX people decided
they could use <New Line> or <NL> only for end-of-line.  The Apple people
standardized on <CR>.  The Microsoft Windows folks decided to keep the old
<CR><NL> (we use <NL> for line feed in the help text).

	unix		<NL>
	dos		<CR><NL>
	mac		<CR>

The following command, for example, tells Vim to
try UNIX format first and MS-DOS format second: 
	:set fileformats=unix,dos

OVERRULING THE FORMAT

If you use the good old Vi and try to edit an MS-DOS format file, you will
find that each line ends with a ^M character.  (^M is <CR>).  The automatic
detection avoids this.  Suppose you do want to edit the file that way?  Then
you need to overrule the format: >

	:edit ++ff=unix file.txt

The "++" string is an item that tells Vim that an option name follows, which
overrules the default for this single command.  "++ff" is used for
'fileformat'.  You could also use "++ff=mac" or "++ff=dos".
   This doesn't work for any option, only "++ff" and "++enc" are currently
implemented.  The full names "++fileformat" and "++encoding" also work.

CONVERSION

You can use the 'fileformat' option to convert from one file format to
another.  Suppose, for example, that you have an MS-DOS file named README.TXT
that you want to convert to UNIX format.  Start by editing the MS-DOS format
file: >
	vim README.TXT

Vim will recognize this as a dos format file.  Now change the file format to
UNIX: >

	:set fileformat=unix
	:write

The file is written in Unix format.


COMPLETING SPECIFIC ITEMS

If you know what you are looking for, you can use these commands to complete
with a certain type of item:

	CTRL-X CTRL-F		file names
	CTRL-X CTRL-L		whole lines
	CTRL-X CTRL-D		macro definitions (also in included files)
	CTRL-X CTRL-I		current and included files
	CTRL-X CTRL-K		words from a dictionary
	CTRL-X CTRL-T		words from a thesaurus
	CTRL-X CTRL-]		tags
	CTRL-X CTRL-V		Vim command line

The key to Omni completion is CTRL-X CTRL-O.  Obviously the O stands for Omni
here, so that you can remember it easier.  Let's use an example for editing C
source:

	{ ~
	    struct foo *p; ~
	    p-> ~

The cursor is after "p->".  Now type CTRL-X CTRL-O.  Vim will offer you a list
of alternatives, which are the items that "struct foo" contains.  That is
quite different from using CTRL-P, which would complete any word, while only
members of "struct foo" are valid here.

For Omni completion to work you may need to do some setup.  At least make sure
filetype plugins are enabled.  Your vimrc file should contain a line like
this: >
	filetype plugin on
Or: >
	filetype plugin indent on

For C code you need to create a tags file and set the 'tags' option.  That is
explained |ft-c-omni|.  For other filetypes you may need to do something
similar, look below |compl-omni-filetypes|.  It only works for specific
filetypes.  Check the value of the 'omnifunc' option to find out if it would
work.

If you press CTRL-A, the editor inserts the text you typed the last time you
were in Insert mode.

The CTRL-@ command does a CTRL-A and then exits Insert mode.  That's a quick
way of doing exactly the same insertion again.

*24.5*	Copying from another line

The CTRL-Y command inserts the character above the cursor.  This is useful
when you are duplicating a previous line.  For example, you have this line of
C code:

	b_array[i]->s_next = a_array[i]->s_next; ~

Now you need to type the same line, but with "s_prev" instead of "s_next".
Start the new line, and press CTRL-Y 14 times, until you are at the "n" of
"next":

	b_array[i]->s_next = a_array[i]->s_next; ~
	b_array[i]->s_ ~

Now you type "prev":

	b_array[i]->s_next = a_array[i]->s_next; ~
	b_array[i]->s_prev ~

Continue pressing CTRL-Y until the following "next":

	b_array[i]->s_next = a_array[i]->s_next; ~
	b_array[i]->s_prev = a_array[i]->s_ ~

Now type "prev;" to finish it off.

The CTRL-E command acts like CTRL-Y except it inserts the character below the
cursor.


	:set textwidth=30

Now you start typing (ruler added):

		 1	   2	     3
	12345678901234567890123456789012345
	I taught programming for a whi ~

If you type "l" next, this makes the line longer than the 30-character limit.
When Vim sees this, it inserts a line break and you get the following:

		 1	   2	     3
	12345678901234567890123456789012345
	I taught programming for a ~
	whil ~

aejaf ljesof esaoifjesalfj
oiesjfil asefieasj filjaself
jsaelfj aoisejfli
asejfliasejfil ji
jawesilfjaslie jfliasejf
liasejfiljas elfjaselj
fieasljflasdejf lilj
aselifjlias


`~/.vim/ftplugin/python.vim`

set textwidth=80



	nice table	  test 1	test 2	    test 3 ~
	input A		  0.534 ~
	input B		  0.913 ~

You need to enter numbers in the third column.  You could move to the second
line, use "A", enter a lot of spaces and type the text.
   For this kind of editing there is a special option: >

	set virtualedit=all

Go back to non-virtual cursor movements with: >

	:set virtualedit=


   The Ex mode commands you need are as follows: >

	%s/-person-/Jones/g
	write tempfile
	quit

You put these commands in the file "change.vim".  Now to run the editor in
batch mode, use this shell script: >

	for file in *.txt; do
	  vim -e -s $file < change.vim
	  lpr -r tempfile
	done

	ls | vim -

	producer | vim -S change.vim -

Another way is to record the commands while you perform them manually.  This
is how you do that: >

	vim -w script file.txt ...

All typed keys will be written to "script".  If you make a small mistake you
can just continue and remember to edit the script later.
   The "-w" argument appends to an existing script.  That is good when you
want to record the script bit by bit.  If you want to start from scratch and
start all over, use the "-W" argument.  It overwrites any existing file.


   To check for a line break in a specific place, use the "\n" item: >

	/one\ntwo

This will match at a line that ends in "one" and the next line starts with
"two".  To match "one two" as well, you need to match a space or a line
break.  The item to use for it is "\_s": >

	/one\_stwo

To allow any amount of white space: >

	/one\_s\+two

This also matches when "one  " is at the end of a line and "   two" at the
start of the next one.

Another example is "\_[]", a character range that includes a line break: >

	/"\_[^"]*"

This finds a text in double quotes that may be split up in several lines.

FINDING AN IDENTIFIER

In C programs (and many other computer languages) an identifier starts with a
letter and further consists of letters and digits.  Underscores can be used
too.  This can be found with: >

	/\<\h\w*\>

"\<" and "\>" are used to find only whole words.  "\h" stands for "[A-Za-z_]"
and "\w" for "[0-9A-Za-z_]".


Try it out: Position the cursor in a paragraph and type: >

	zfap

	zf	F-old creation
	zo	O-pen a fold
	zc	C-lose a fold

Suppose you have created several folds, and now want to view all the text.
You could go to each fold and type "zo".  To do this faster, use this command: >

	zr

This will R-educe the folding.  The opposite is: >

	zm

This folds M-ore.  You can repeat "zr" and "zm" to open and close nested folds
of several levels.

If you have nested several levels deep, you can open all of them with: >

	zR

This R-educes folds until there are none left.  And you can close all folds
with: >

	zM

This folds M-ore and M-ore.

You can quickly disable the folding with the |zn| command.  Then |zN| brings
back the folding as it was.  |zi| toggles between the two.  This is a useful
way of working:
- create folds to get overview on your file
- move around to where you want to do your work
- do |zi| to look at the text and edit it
- do |zi| again to go back to moving around

More about manual folding in the reference manual: |fold-manual|



Try this by setting the 'foldmethod' option: >

	:set foldmethod=indent

Then you can use the |zm| and |zr| commands to fold more and reduce folding.
It's easy to see on this example text:


This line is not indented
	This line is indented once
		This line is indented twice
		This line is indented twice
	This line is indented once
This line is not indented
	This line is indented once
	This line is indented once

						*'foldmethod'* *'fdm'*
'foldmethod' 'fdm'	string (default: "manual")
			local to window
			{not available when compiled without the |+folding|
			feature}
	The kind of folding used for the current window.  Possible values:
	|fold-manual|	manual	    Folds are created manually.
	|fold-indent|	indent	    Lines with equal indent form a fold.
	|fold-expr|	expr	    'foldexpr' gives the fold level of a line.
	|fold-marker|	marker	    Markers are used to specify folds.
	|fold-syntax|	syntax	    Syntax highlighting items specify folds.
	|fold-diff|	diff	    Fold text that is not changed.

SYNTAX						*fold-syntax*

A fold is defined by syntax items that have the "fold" argument. |:syn-fold|

The fold level is defined by nesting folds.  The nesting of folds is limited
with 'foldnestmax'.

Be careful to specify proper syntax syncing.  If this is not done right, folds
may differ from the displayed highlighting.  This is especially relevant when
using patterns that match more than one line.  In case of doubt, try using
brute-force syncing: >
	:syn sync fromstart


fold							*:syn-fold*

The "fold" argument makes the fold level increase by one for this item.
Example: >
   :syn region myFold start="{" end="}" transparent fold
   :syn sync fromstart
   :set foldmethod=syntax
This will make each {} block form one fold.

The fold will start on the line where the item starts, and end where the item
ends.  If the start and end are within the same line, there is no fold.
The 'foldnestmax' option limits the nesting of syntax folds.
See |:syn-foldlevel| to control how the foldlevel of a line is computed
from its syntax items.
{not available when Vim was compiled without |+folding| feature}


				int func1(void)
				{
					return 1;
		  +---------->  }
		  |
	      []  |		int func2(void)
		  |	   +->	{
		  |    [[  |		if (flag)
	start	  +--	   +--			return flag;
		  |    ][  |		return 2;
		  |	   +->	}
	      ]]  |
		  |		int func3(void)
		  +---------->	{
					return 3;
				}


							*format-comments*

- A comment string that repeats at the start of each line.  An example is the
  type of comment used in shell scripts, starting with "#".
- A comment string that occurs only in the first line, not in the following
  lines.  An example is this list with dashes.
- Three-piece comments that have a start string, an end string, and optional
  lines in between.  The strings for the start, middle and end are different.
  An example is the C style comment:
	/*
	 * this is a C comment
	 */

The 'comments' option is a comma-separated list of parts.  Each part defines a
type of comment string.  A part consists of:
	{flags}:{string}

{string} is the literal text that must appear.

{flags}:
  n	Nested comment.  Nesting with mixed parts is allowed.  If 'comments'
	is "n:),n:>" a line starting with "> ) >" is a comment.

  b	Blank (<Space>, <Tab> or <EOL>) required after {string}.

  f	Only the first line has the comment string.  Do not repeat comment on
	the next line, but preserve indentation (e.g., a bullet-list).

  s	Start of three-piece comment

  m	Middle of a three-piece comment

  e	End of a three-piece comment

  l	Left align. Used together with 's' or 'e', the leftmost character of
	start or end will line up with the leftmost character from the middle.
	This is the default and can be omitted. See below for more details.

  r	Right align. Same as above but rightmost instead of leftmost. See
	below for more details.

  O	Don't consider this comment for the "O" command.

  x	Allows three-piece comments to be ended by just typing the last
	character of the end-comment string as the first action on a new
	line when the middle-comment string has been inserted automatically.
	See below for more details.

  {digits}
	When together with 's' or 'e': add {digit} amount of offset to an
	automatically inserted middle or end comment leader. The offset begins
	from a left alignment. See below for more details.

  -{digits}
	Like {digits} but reduce the indent.  This only works when there is
	some indent for the start or end part that can be removed.

When a string has none of the 'f', 's', 'm' or 'e' flags, Vim assumes the
comment string repeats at the start of each line.  The flags field may be
empty.

Any blank space in the text before and after the {string} is part of the
{string}, so do not include leading or trailing blanks unless the blanks are a
required part of the comment string.

When one comment leader is part of another, specify the part after the whole.
For example, to include both "-" and "->", use >
	:set comments=f:->,f:-

A three-piece comment must always be given as start,middle,end, with no other
parts in between.  An example of a three-piece comment is >
	sr:/*,mb:*,ex:*/
for C-comments.  To avoid recognizing "*ptr" as a comment, the middle string
includes the 'b' flag.  For three-piece comments, Vim checks the text after
the start and middle strings for the end string.  If Vim finds the end string,
the comment does not continue on the next line.  Three-piece comments must
have a middle string because otherwise Vim can't recognize the middle lines.

Notice the use of the "x" flag in the above three-piece comment definition.
When you hit Return in a C-comment, Vim will insert the middle comment leader
for the new line: " * ".  To close this comment you just have to type "/"
before typing anything else on the new line.  This will replace the
middle-comment leader with the end-comment leader and apply any specified
alignment, leaving just " */".  There is no need to hit Backspace first.

When there is a match with a middle part, but there also is a matching end
part which is longer, the end part is used.  This makes a C style comment work
without requiring the middle part to end with a space.

Here is an example of alignment flags at work to make a comment stand out
(kind of looks like a 1 too). Consider comment string: >
	:set comments=sr:/***,m:**,ex-2:******/
<
                                   /*** ~
                                     **<--right aligned from "r" flag ~
                                     ** ~
offset 2 spaces for the "-2" flag--->** ~
                                   ******/ ~
In this case, the first comment was typed, then return was pressed 4 times,
then "/" was pressed to end the comment.

Here are some finer points of three part comments. There are three times when
alignment and offset flags are taken into consideration: opening a new line
after a start-comment, opening a new line before an end-comment, and
automatically ending a three-piece comment.  The end alignment flag has a
backwards perspective; the result is that the same alignment flag used with
"s" and "e" will result in the same indent for the starting and ending pieces.
Only one alignment per comment part is meant to be used, but an offset number
will override the "r" and "l" flag.

Enabling 'cindent' will override the alignment flags in many cases.
Reindenting using a different method like |gq| or |=| will not consult
alignment flags either. The same behaviour can be defined in those other
formatting options. One consideration is that 'cindent' has additional options
for context based indenting of comments but cannot replicate many three piece
indent alignments.  However, 'indentexpr' has the ability to work better with
three piece comments.

Other examples: >
   "b:*"	Includes lines starting with "*", but not if the "*" is
		followed by a non-blank.  This avoids a pointer dereference
		like "*str" to be recognized as a comment.
   "n:>"	Includes a line starting with ">", ">>", ">>>", etc.
   "fb:-"	Format a list that starts with "- ".

By default, "b:#" is included.  This means that a line that starts with
"#include" is not recognized as a comment line.  But a line that starts with
"# define" is recognized.  This is a compromise.


	{flags}:{text}

	:set comments=://
	:set comments=s1:/*,mb:*,ex:*/

	:set comments=n:>,n:!
	> ! Did you see that site? ~
	> ! It looks really great. ~
	> I don't like it.  The ~
	> colors are terrible. ~
	What is the URL of that ~
	site? ~


	:set browsedir=current
	:set browsedir=buffer

	last		Use the last directory browsed (default)
	buffer		Use the same directory as the current buffer
	current		use the current directory

	:browse split /etc
