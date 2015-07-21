"save paths to python file and plugin folder for later use
let s:path = fnamemodify(resolve(expand('<sfile>:p')), ':h') . '\my_python_file.py'
let s:config = fnamemodify(resolve(expand('<sfile>:p')), ':h')


function! Up(...)
    python import sys
    python import vim
    python arglist= vim.eval("a:000")
    python path_to_folder= vim.eval("s:config")
    python sys.argv = [path_to_folder] + arglist
    execute 'pyfile ' . s:path

endfunction
command! -nargs=* Up call Up(<f-args>)
