```vim
" perl
nnoremap <leader>pls <cmd>e ~/script.pl<CR>
nnoremap <leader>plp <cmd>read ! perl ~/script.pl<CR>
```

```pl
#!/usr/bin/perl
print "Hello, world!\n";
```

```pl
#!/usr/bin/perl
# use 5.34.0; # works
use 5.034; # works
say "Hello, world!";
```


```bash
$ perldoc perlfaq
You need to install the perl-doc package to use this program.

$ sudo apt install perl-doc
```


```pl
#!/usr/bin/perl
@lines = `perldoc -u -f atan2`;
foreach (@lines) {
    s/\w<([^>]+)>/\U$1/g;
    print;
}
```

```txt
=over 8

=item atan2 Y,X
ATAN2 ARCTANGENT TAN TANGENT

=for Pod::Functions arctangent of Y/X in the range -PI to PI

Returns the arctangent of Y/X in the range -PI to PI.

For the tangent operation, you may use the
C<MATH::TRIG::TAN|Math::Trig/TAN> function, or use the familiar
relation:

    sub tan { sin($_[0]) / cos($_[0])  }

The return value for ATAN2(0,0) is implementation-defined; consult
your ATAN2(3) manpage for more information.

Portability issues: PERLPORT/ATAN2.

=back
```

---

```bash
$meal = "brontosaurus steak";
$barney = "fead ate a $meal";
$barney = 'fead ate a $meal';

print "$meal";
print "$barney";


```

```pl
#!/usr/bin/perl
use warnings;
$n = 1;
while ($n < 10) {
    $sum += $n;
    $n += 2;
}
print "The total was $sum.\n";
```
```txt
The total was 25.
```
```pl
#!/usr/bin/perl
use warnings;
print  2 * 3.1415926534 * 12.5
```
78.539816335

```pl
#!/usr/bin/perl
use warnings;
print  2 * 3.1415926534 * <STDIN>
```


```pl
#!/usr/bin/perl
use warnings;
$input1 = <STDIN>;
$input2 = <STDIN>;
print $input1 * $input2;
```


```pl
#!/usr/bin/perl
use warnings;
print "input text: ";
$input = <STDIN>;
print "input count: ";
$count = <STDIN>;
print $input x $count
```


