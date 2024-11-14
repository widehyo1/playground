Output difft.gif

Set FontSize 14
Set Width 1200
Set Height 600

Type "ls --color"
Sleep 500ms
Enter

Type "basename -s .tgz *.tgz"
Sleep 500ms
Enter

Type `basename -s .tgz *.tgz | xargs -I@ echo 'bash -c "mkdir @"'`
Sleep 500ms
Enter

Type `basename -s .tgz *.tgz | xargs -I@ echo 'bash -c "mkdir @ && tar -C @ -xzf @.tgz"'`
Sleep 500ms
Enter

Type `basename -s .tgz *.tgz | xargs -I@ bash -c "mkdir @ && tar -C @ -xzf @.tgz"`
Sleep 500ms
Enter

Enter
Enter

Type "ls --color"
Sleep 500ms
Enter

Type "difft 3f7bc81ae6_core head_core --skip-unchanged"
Sleep 500ms
Enter

# Admire the output for a bit.
Sleep 5s
