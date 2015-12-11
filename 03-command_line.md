# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > Command Line Cheat Sheet:

> > FILES

> > 1. `touch x.txt` = make a new file, `x.txt`

> > 2. `cp x.txt y.txt` = copy file contents (could also copy to a directory). `cp -r x y` = copies files from directory `x` to directory `y`.

> > 3. `less/more x.txt` = displays file separately/in-line. `cat` is a\
 more extreme version of `more`.

> > 4. `grep "Hello, world" x.txt` = search for text in file; pulls up matches on command li\
ne. (`find` = find files)

> > 5. `mv x y` = rename `x` as `y` (can be files or directories)

> > 6. `rm x.txt y.txt` = deletes files. `rm -rf x y` = for directories.


> > DIRECTORIES

> > 7. `pwd` = print working directory. see where you are

> > 8. `ls` = list working directory contents

> > 9. `cd` = change directory

> > 10. `mkdir x` = make a new directory, `x`

> > 11. `rmdir x` = remove directory `x` 

> > 12. `pushd x/y/z` = "save where I am, then go to directory `z` [path `x/y/z`]". With no arguments, loops btwn current directory and last one you pushd from.

> > 13. `popd` = takes you back to last directory you `pushd` from. Doesn't take arguments. (Takes you back up the "directory stack" it's been keeping track of, until you reach the beginning of the `pushd` chain at which point the stack is empty.)


> > REDIRECTION 

> > 14. `x-command|y-command` = pipe `x-command`-output to `y-command` as input

> > 15. `program<file` = sends `file` input to `program`

> > 16. `command>file` = write `command`-output to `file`. Just `cat>file` allows you to write into a file from command line. Close the file with `CTRL-d`! (`C-d` in Emacs)

> > 17. `command>>file` = append `command`-output to `file`


> > MISC

> > 18. `echo $X` = print some argument(s) `X`

> > 19. `export X=""` = export/set a new environment variable, `X`

> > 20. `unset X` = remove `X` from environment


---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > `ls` lists working directory contents (w/o arguments = current working directory). Lists `ls -a` include directory entries whose names begin with a dot (.). Lists `ls -l` use Long Format, displaying all info about files/directories, and lists `ls -lh` amend `ls -l` by displaying file size in human-readable format (M=MB, K=KB, G=GB). `-lh` takes precedence over just plain `-l`. Combining `-l` or `-lh` with `-a` (e.g., `ls -a -lh`) allows for additional info display for entries whose names begin with a dot. 

---


---

What does `xargs` do? Give an `example` of how to use it.

> > `xargs` takes in and executes a given command (`xargs command`) on input, such that `X | xargs Y` (where `X` and `Y` are commands) is the most commonly used elaboration of `xargs`. 

> > Other uses of `xargs`:
> > - just plain `xargs`: enter input, press CTRL-d, and input gets echoed back; delimiters `-d` can be applied to take each input character literally, e.g. `-d\n` for newlines; option `-p` can be applied to confirm `xargs` command execution from user
> > - `xargs -n num`, where num = number of items per line in the `xargs` output
> > - `xargs -t`, which will execute the command `/bin/echo X` where `X`=input
> > - `find X | xargs Y`, where `X`=what there is to be found (seems like this tends to be a name) and `Y` is a command. 

> > Here's an `example` of this common use of `xargs`: 

> > ```$ ls

> > abc.a  abc.b  abc.c  bca.a  bca.b  bca.c

> > $ find . -name "*.c" | xargs rm -rf

> > $ ls

> > abc.a  abc.b  bca.a  bca.b
```

> > The above example forces the recursive removal of its `xargs` input, viz., all files ending in `".c"`. Adding `-print0` after `"*.c"` and `-0` after `xargs` will additionally include filenames containing spaces in the `xargs` input.

> > The `find X | xargs Y` form might also incorporate `grep` in command `Y`, in order to find a particular string in a particular set of files.

> > Here's an `example` (for the sake of this example let's say we haven't yet recursively removed all files ending in `".c"`):

> > ```$ ls

> > abc.a  abc.b  abc.c  bca.a  bca.b  bca.c

> > $ find . -name "*.c" | xargs grep "[string contained once in abc.a, once in abc.b, twice in abc.c, and once in bca.c]"

> > ./abc.c:[line containing first instance of string]

> > ./abc.c:[line containing second instance of string]

> > ./bca.c:[line containing first instance of string]
```
> >

> > As a final note, `X | xargs Y` is not a more redundant form of `X | Y`. `xargs` makes it possible to "batch" arguments together, thereby avoiding "Argument list too long" messages on older kernels for long command lines. And `xargs` is useful when wanting to both know what the output contents from `X` are and be able to execute a new command, `Y`, on them (e.g., for directory listings).

---

