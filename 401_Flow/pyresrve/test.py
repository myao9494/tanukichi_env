# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) Mineo Sudo
#
###############################################################################

import pandas as pd

class redmine_tanuki(object):
    """test
    
    Args:
        object (nan): nan
    """

    def __init__(self):
        """shokiatai
        """

        self.tag="sss"

    def pri(self):
        """print tag
        """

        print(self.tag)

    def mk_pd(self):
        """make dataframe
        """

        self.df=pd.DataFrame()

if __name__ == '__main__':
    obj=redmine_tanuki()
    obj.pri()
    # obj.mk_pd()