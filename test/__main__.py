import glob, os
from tailread import readlines



def main():
    line_count = 0
    file_count = 0
    for path in glob.glob('./**/*.*', recursive=True):
        fn, ext = os.path.splitext(path)

        if fn == '__main__':
            continue

        if ext in ['.exe', '.pyc', '.dist-info', '.egg-info', '.gz', '.odt']:
            continue
        
        file_count += 1
        normalines = []
        with open(path, 'rb') as fp:
            normalines = reversed(fp.readlines())
        
        tailines = readlines(open(path, 'rb'))

        for rnorm, tails in zip(normalines, tailines):
            if rnorm != tails:
                print(path)
            assert rnorm == tails
            line_count +=1
    
    print('file_count:', '{} files'.format(file_count))
    print('line_count:', '{} lines'.format(line_count))

# tested
# file_count: 551 files
# line_count: 221713 lines

if __name__ == '__main__':
    main()
