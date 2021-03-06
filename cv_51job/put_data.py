#!/usr/bin/env python
# -*- coding:utf8 -*-

from spider.ipin.savedb import Bin2DB
import cv51
import re
import sys


class Dis51PageStore(cv51.CV51PageStore):
    def save_time_log(self, indexUrl, cur_tm):
        return

    def do_save(self, odoc, content, fnpath=None, offset=None):
        odoc.update({'pageContentPath': "binf::%s::%d" % (fnpath, offset)})
        return self.upsert_doc(odoc['indexUrl'], odoc)


class CV51Bin2DB(Bin2DB):
    def __init__(self):
        Bin2DB.__init__(self)
        self.pagestore = Dis51PageStore()

    def parse_name(self, n):
        m = re.match(r'cv_51job\.(\d+)\.(\d+)', n)
        if m:
            return m.group(2), m.group(1)
        return None, None

    def get_pagestore(self):
        return self.pagestore

    def get_url(self, jdid):
        return "http://fake/%s" % jdid


if __name__ == "__main__":
    sb = CV51Bin2DB()
    for fn in sys.argv[1:]:
        sb.save(fn)
