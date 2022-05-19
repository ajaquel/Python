# Arbitrary numbers of position arguments using *args.
def sandwich(bread, meat, *args):
    print('%s on %s' % (meat, bread), end=' ')
    if len(args) > 0:
        print('with', end=' ')
    for extra in args:
        print(extra, end=' ')
    print("")


sandwich('sourdough', 'turkey', 'mayo')
sandwich('wheat', 'ham', 'mustard', 'tomato', 'lettuce')



# Arbitrary numbers of keyword arguments using **kwargs.
def sandwich(bread, meat, **kwargs):
    print('%s on %s' % (bread, meat))
    for category, extra in kwargs.items():
        print('   %s: %s' % (category, extra))

sandwich('sourdough', 'turkey', sauce='mayo')
sandwich('wheat', 'ham', sauce1='mustard', veggie1='tomato', veggie2='lettuce')




# Arbitrary numbers of arguments using *args and **kwargs.
def gen_command(application, **kwargs):
    command = application
    for argument in kwargs:
        command += ' --%s=%s' % (argument, kwargs[argument])
    return command

print (gen_command('notepad.exe'))  # No options
print (gen_command('Powerpoint.exe', file='pres.ppt', start=True, slide=3))


