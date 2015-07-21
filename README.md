
I uploaded here a skeleton to set up some basic scripting in python for the Vim editor. There are many tutorials in the net for inline python within regular vimscript, or examples of python code thrown in the vim/plugin folder, but when I tried to set up a pathogen friendly plugin (wich lives in \vimfiles\bundle), problems arose with paths, and the relevant info about how to set data files and arguments was very scattered in the docs, online tutorials and stackoverflow answers. Mind I'm no expert on the matter and some things may be done differently/much better, but this works for me as a platform to learn more and it may help others. Some things are crude and basic and may well be improved. I'd love to get some feedback from the experts here.

My main requirement is setup vimscript so that i can promptly forget it and code in python. This needed:

  - a proper setting of the path to the python file. This is not obvious for the beginner.
  - learning how to set a config or data file and access it.
  - passing command arguments to python

###Requirements

Vim, compiled with python support. If you don't know how to test this, just type in the Vim editor

`:echo has(python)

The result must be a '1' displayed in the same command area. Else, a 0, you need to reinstall python.

This code was tested only in a Windows7 box, but it should be ok for all flavors of windows. I'm not into Linux or OsX. It should also work because it only uses internal vim/python path management, but I didn't test it, and I cannot give any advice on the matter. I'd like to know if it is cross-platform.

###Install

With Pathogen: to do

###What does this plugin do:

Not much. Just provide a minimal plugin setup. It calls a py file and runs it. The py file has access to a config file. When typing its only command (:Up) it appends to the current buffer the name of the current file, the path to the plugin, the arguments given (not programmed: you can just type ':Up yadda gadda foo bar' as arguments and they will be duly echoed. Finally, the plugin appends to the current buffer the contents of a dummy config file set up with configparser (a INI like file module)

###+Info:

Paths: The first hurdle is setting an apparently sound vimscript to call a py file. To avoid the 'File not found' errors, its better to construct an s:path variable that points to the python file (see my_vim_plugin.vim file) and then, inside the vim function, call 'pyfile' from within an 'execute' command. What is executed is a string wich concatenates pyfile with the path to the python file.

Then the python file needs a path so it can access a config file (or any other data file you'd need). The solution is to build a s:config variable, nearly identical to s:path, wich contains the path to the plugin folder. Then is passed to python, first as a python variable

`python path_to_folder= vim.eval("s:config")

and then is stored as the first item of an argument list created explicitly:

`python sys.argv = [path_to_folder] + arglist

Here arglist is constructed by assigning to it the internal vim argument list stored in a:000

`python arglist= vim.eval("a:000")

I opted here for a variable number of args (it can be 0) for max flexibility (see :help nargs in Vim for more info). That is what is set with the -nargs=* option and the ... in the function arguments.

And thats it. A lot has to be improved/developed depending on the kind of plugin to be written, and theres a lot of complexity to be learned. But this is a good starting point for me, after had to look around and ask a lot to set some of the vimscript syntax quirks.
