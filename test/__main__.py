import glob, os
from unittest import TestCase, main

from tailread import readlines



class TestReadLines(TestCase):

    def test_readlines(self):
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
            
            tailines = None
            with open(path, 'rb') as fp:
                tailines = list(readlines(fp, batch_size=2048))

            for rnorm, tails in zip(normalines, tailines):
                self.assertEqual(rnorm, tails)
                line_count +=1

        print('file_count:', '{} files'.format(file_count))
        print('line_count:', '{} lines'.format(line_count))




# tested
# file_count: 551 files
# line_count: 221713 lines

if __name__ == '__main__':
    main()
