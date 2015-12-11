# Choose and learn your editor(s)


Computing's interface is text. To work effectively, you need to be fluent with this interface.


### Typing

It may sound silly, but [make sure](http://www.typingtest.com/) you know how to type. You should be comfortable typing with perfect accuracy at 60 words per minute, at least. If you currently can't, practice until you can.

A lot of your work will be done in a text editor. You have to know how to use your editor. Any editor will work, but knowing a powerful editor well will make you faster, more comfortable, and more effective.


### Terminal Editor

Sometimes you will need to use a non-graphical text editor. This means an editor that will run entirely inside a terminal window, without spawning a new window, entirely without mouse input.

Make sure that you know at least one of these well enough to do basic editing in a terminal:

 * Emacs
 * vim
 * nano

You should know at least enough vim to be able to get out of it, because it is the default on many systems and you might find yourself in it even if you didn't mean to be.

If you intend to use a graphical editor that doesn't run in a terminal, nano might be a good choice for you because it is very simple.

Both Emacs and vim have built-in interactive tutorials that you can try.

---

What terminal editor will you use? How did you make your decision?

>> After reading, tutorial-ing, and playing around (or trying to), I'm leaning toward entering the Emacs camp. Ultimately, Emacs seems to be the most useful/powerful tool out of Emacs, Vim, and Nano ("more than a text editor," Emacs can do the most things), and so seems most worth my while to learn. I also aim to familiarize myself with basic vi/Vim commands. 

---


### Graphical Editor

You will probably spend most of your time with access to a graphical interface, where you have more choices in editors and integrated development environments.

Popular editors and IDEs include:

 * Emacs
 * vim
 * Sublime
 * Atom
 * Spyder
 * PyCharm

If you choose Emacs or vim, you will have essentially the same editor experience across graphical and non-graphical environments, which is nice. It's also nice to be able to work without ever having to use a mouse. Emacs and vim have somewhat steep learning curves, but they give you the ability to customize your environment quite a lot to make it exactly what you want.

Sublime is probably the most popular editor for new coders. You can set it up to integrate with Python fairly well. Atom is pretty similar to Sublime but has an interesting open architecture and is developed by folks at GitHub.

Spyder and PyCharm are IDEs for Python. They try to give you a fully configured setup out of the box.

We will also use Jupyter (IPython) notebooks, but this does not remove the need for proficiency in an editor or IDE.

---

What graphical editor will you use? How did you make your decision? What are some interesting features of your editor? What are some useful keyboard shortcuts for your editor? How do you customize your editor?

>> I'm planning to go with Spyder. My hunch is that ultimately I'll want to transition to Emacs, but after checking out various options I think that for now, Spyder is the way to go. It comes fully configured for Python, so has lots of cool Python-specific features. The most obvious and probably most useful is the IPython console right next to the editor, just begging to be used for more efficient debugging. (Another option available for running a code snippet would be to run it in its own tab in the separate Console window.) I like how I can chunk code into "cells" and then test these cells in the IPython console in an orderly way (I can also just run one cell, or even one line or group of lines, at a time). More, Spyder keeps track of objects, variables, and files for me, which seems like it'll make for more fluid coding. I still don't get how best to use the actual debugging menu, but it seems potentially useful, e.g. for plugging in different values for a variable without having to return to the source code to do so.
 
>> Useful Spyder keyboard shortcuts include:
>> - `F5`, which executes the current editor file in the console
>> - `Tab`, which auto-completes names or gives you a list of names to choose from, once you've defined them and are wanting to write them again
>> - `Cmd+Enter`, which executes the current cell (from editor, to console)
>> - `Shift+Enter`, executes current cell and moves to next one
>> - `Alt+<Up Arrow>` or `+<Down arrow>` moves highlighted or current line(s) up or down
>> - `Shift+Cmd+Alt+M`, which maximizes the current window or changes maximized window back to normal
>> - `Cmd+/-`, to change font size
>> - `Cmd+S`, to save
>> - `Cmd+I`, which, when pressed while the cursor is on an object, opens documentation for that object in the object inspector
>> - `u`, `d` at the debugger, which navigates the inspection point up or down the stack.

>> Also useful are `%pandas inline` and `%pandas qt`, to get figures to appear inline in IPython console or in their own window (Qt window)

>> Plugins and toolbars can be arranged as needed, and any one window can be maximized with `Shift+Cmd+Alt+M`. Calling `spyder --reset` from the command line resets all customization.

---
