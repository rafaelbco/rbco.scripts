from os.path import basename
import re

from rbco.commandwrap import decorators as cmd
from prdg.util.file import file_to_str, str_to_file, remove_extension

EXTENSIONS_TO_CLEAN = ('aux', 'bbl', 'blg', 'log', 'out', 'toc')

COMMAND_PATTERN = r'\\%s\s*{\s*(.*)\s*}'
BIB_PATTERN = COMMAND_PATTERN % 'bibliography'

def get_master_name(path):
    return remove_extension(basename(path))


@cmd.output_none
@cmd.check_status
@cmd.run_command
@cmd.wrap_command('pdflatex -interaction %(interaction)s %(kwargs)s %(path)s')
def pdflatex(path, interaction='nonstopmode', **kwargs): pass

@cmd.output_none
@cmd.check_status
@cmd.run_command
@cmd.wrap_command('bibtex %(kwargs)s %(master_name)s')
def bibtex(master_name, **kwargs): pass

@cmd.output_none
@cmd.check_status
@cmd.run_command
@cmd.wrap_command('rm %(kwargs)s %(path)s %(args)s')
def rm(path, *args, **kwargs): pass

def clean(master_name, extra_extensions=set()):
    ext = set(EXTENSIONS_TO_CLEAN) | set(extra_extensions)
    glob = '%s.{%s}' % (master_name, ','.join(ext))
    rm(glob, f=True)    
    
def make_callable(a):
    return (callable(a) and a) or (lambda *args, **kwargs: a)    
    
def replace_command(command_name, repl, text):
    """
    Replace all occurrences of "\`command_name`{`arg`}" in `text`. `repl` is 
    either a string or a function which accepts `arg` as argument
    and return the replacement text.
    """    
    repl_func = make_callable(repl)
        
        
    def low_level_repl(match_obj):
        arg = match_obj.group(1)
        return repl_func(arg)
    
    return re.sub(COMMAND_PATTERN % command_name, low_level_repl, text)
        
def replace_command_argument(command_name, arg_repl, text):
    """
    Replace all occurrences of "\`command_name`{`arg`}" in text. `arg_repl` is 
    either a string to replace `arg` or a callable which accepts `arg` argument
    and return the replacement text.
    """    
    arg_repl_func = make_callable(arg_repl)
            
    command_template = '\\' + command_name + '{%s}'
    
    return replace_command(
        command_name, 
        lambda arg: command_template % arg_repl_func(arg), 
        text
    )       
    
def get_bibs_str(text):
    print BIB_PATTERN
    return re.findall(BIB_PATTERN, text, re.I)    

def get_bibs_file(path):
    text = file_to_str(path)
    return get_bibs_str(text)
