# encoding: utf-8
from __future__ import print_function
import os
from urllib.request import urlopen
import sys

# Name script for header
name_script = 'Domain.Uptime v1.0'
# path and file *.csv with name;domain
path_file = 'domains.csv'
# delimiter csv file
delimiter = ','
# output line size
width = 59
# TO DO: remove OS dependencies
os.system('clear')


def requestUrl(url):
    try:
        resp = urlopen(url, timeout=30)
        status = str(resp.getcode())
        return status
    except Exception as e:
        status = '\nFail Detail:\n>> ' + str(e) + '\n'
        return status


def printResult(name, status):
    if 'Fail' in status:
        print(name + '{:.>{w}} '.format(
            '!![ FAIL ]!!', w=str(width-len(name))) + status)
        return
    else:
        status = '[OK :: ' + status + ']'
        print(name + '{:.>{w}}'.format(status, w=str(width-len(name))))
        return


def printEvaluating():
    print(domain[0] + '{:.>{w}}'.format(
        'Evaluating!', w=str(width-len(domain[0]))))
    sys.stdout.write('\033[1A')
    return


if __name__ == "__main__":
    print('#'*width + '\n{:^{w}}\n'.format(
        name_script, w=str(width)) + '#'*width + '\n')
    try:
        with open(path_file, 'r') as f:
            for l in f:
                i = l.replace('\n', '')
                domain = i.split(delimiter)
                printEvaluating()
                status = requestUrl(domain[1])
                printResult(domain[0], status)
    except Exception as e:
        print('{:.^{w}}'.format(
            '!! GERAL ERROR !!', w=str(width)
                ) + "\n>>Fail Detail:\n>>%s" % e)
