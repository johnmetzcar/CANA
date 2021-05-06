# -*- coding: utf-8 -*-
"""
Biological Boolean Networks
=================================

Some of the commonly used biological boolean networks


"""
#   Copyright (C) 2017 by
#   Alex Gates <ajgates42@gmail.com>
#   Rion Brattig Correia <rionbr@gmail.com>
#   Thomas Parmer <tjparmer@indiana.edu>
#   All rights reserved.
#   MIT license.
import os
from .. boolean_network import BooleanNetwork


_path = os.path.dirname(os.path.realpath(__file__))
""" Make sure we know what the current directory is """


def Regan2012Apoptosis():
    """Boolean network model of apoptosis

    The network is defined in :cite:`ASK HERBERT SIZEK!!!!!!`.

    Returns:
        (BooleanNetwork)
    """
    return BooleanNetwork.from_file(_path + '/Regan2012ApoptosisReg.txt', name="Arabidopsis Thaliana", keep_constants=True)

_regan_pi3k_networks = [
    'Regan2012Apoptosis',
    'Regan2014Combined',
    'Regan2014PhaseSwitch',
    'Regan2014RestrictionSwitch',
    'Regan2019ApoptoticSwitch',
    'Regan2019OriginLicensingSwitch',
    'Regan2019PhaseSwitch',
    'Regan2019PI3K',
    'Regan2019PI3Kcellcycleapoptosis',
    'Regan2019RestrictionSwitch',
    'PI3Kcellcycleapoptosis']

def load_regan_PI3K_network_models(name=None):
    """Loads one of the Regan PI3K models.

    Args:
        name (str): the name of the model to be loaded.
            Accepts: ["Regan2012Apoptosis", "Regan2014Combined", ...,
            "Regan2019PI3Kcellcycleapoptosis", "Regan2019RestrictionSwitch"]

    Returns:
        (BooleanNetwork)

    Note: see bio.py load_cell_collective models function for original implementation
    """

    #
    if name not in _regan_pi3k_networks:
        models_str = "'" + "','".join(_regan_pi3k_networks) + "'"
        raise TypeError('Model name could not be found. Please specify one of the following models: {models:s}.'.format(models=models_str))
    else:
        return BooleanNetwork.from_file(_path + '/regan_pi3k/' + name + '.txt', type='logical', name=name, keep_constants=True)


def pi3kcellcycleapoptosis():

    return BooleanNetwork.from_file(_path + '/regan_pi3k/' + 'PI3Kcellcycleapoptosis_from_Sizek_et_al_2019.txt', type='logical', name='PI3Kcellcycleapoptosis', keep_constants=True)

def load_all_regan_pi3k_models():
    """Load all the Regan PI3K models, instanciating 10 models.

    Returns:
        (list)

    Note: see source code for full list of models.
    """
    print('this worked')
    return [load_regan_PI3K_network_models(name=name) for name in _regan_pi3k_networks]
