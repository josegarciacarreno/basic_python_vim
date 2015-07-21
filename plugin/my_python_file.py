import vim
import ConfigParser
import sys, os


vim.current.buffer.append("'Path and name of current buffer if it exists:'")
vim.current.buffer.append(vim.current.buffer.name)

#save current working directory to restore it later
work_path=os.getcwd()
#set and read config file
config=ConfigParser.RawConfigParser()
os.chdir(sys.argv[0])
config.read('my_config_file.cfg')
#restore directory
os.chdir(work_path)

#show config file values
vim.current.buffer.append("")
vim.current.buffer.append("'Plugin folder path and user entered arguments:'")
vim.current.buffer.append(sys.argv)
vim.current.buffer.append("")
vim.current.buffer.append("'sample config file values:'")
vim.current.buffer.append(config.get('default','name'))
vim.current.buffer.append(config.get('default','email'))
vim.current.buffer.append(config.get('more','foo'))
vim.current.buffer.append(config.get('more','bar'))
