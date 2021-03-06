# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.4
# *
# * Copyright 2018. Benoit Michau. ANSSI. P1sec.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_csn1dir/si3_rest_octet.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.34 SI 3 Rest Octets
# top-level object: SI3 Rest Octet



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

gprs_indicator = CSN1List(name='gprs_indicator', list=[
  CSN1Bit(name='ra_colour', bit=3),
  CSN1Bit(name='si13_position')])

early_classmark_sending_control = CSN1Alt(name='early_classmark_sending_control', alt={
  'H': ('', []),
  'L': ('', [])})

selection_parameters = CSN1List(name='selection_parameters', list=[
  CSN1Bit(name='cbq'),
  CSN1Bit(name='cell_reselect_offset', bit=6),
  CSN1Bit(name='temporary_offset', bit=3),
  CSN1Bit(name='penalty_time', bit=5)])

scheduling_if_and_where = CSN1Alt(name='scheduling_if_and_where', alt={
  'H': ('', [
  CSN1Bit(name='where', bit=3)]),
  'L': ('', [])})

system_information_21_indicator = CSN1Alt(name='system_information_21_indicator', alt={
  'H': ('', [
  CSN1Bit(name='si21_position')]),
  'L': ('', [])})

system_information_2ter_indicator = CSN1Alt(name='system_information_2ter_indicator', alt={
  'H': ('', []),
  'L': ('', [])})

iu_indicator = CSN1Bit(name='iu_indicator')

optional_power_offset = CSN1Alt(name='optional_power_offset', alt={
  'H': ('', [
  CSN1Bit(name='power_offset', bit=2)]),
  'L': ('', [])})

_3g_early_classmark_sending_restriction = CSN1Alt(name='_3g_early_classmark_sending_restriction', alt={
  'H': ('', []),
  'L': ('', [])})

si2quater_indicator_struct = CSN1Bit(name='si2quater_indicator_struct')

optional_selection_parameters = CSN1Alt(name='optional_selection_parameters', alt={
  'H': ('', [
  CSN1Ref(obj=selection_parameters)]),
  'L': ('', [])})

si3_rest_octet = CSN1List(name='si3_rest_octet', list=[
  CSN1Ref(obj=optional_selection_parameters),
  CSN1Ref(obj=optional_power_offset),
  CSN1Ref(obj=system_information_2ter_indicator),
  CSN1Ref(obj=early_classmark_sending_control),
  CSN1Ref(obj=scheduling_if_and_where),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Ref(obj=gprs_indicator)]),
    'L': ('', [])}),
  CSN1Ref(obj=_3g_early_classmark_sending_restriction),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Ref(name='si2quater_indicator', obj=si2quater_indicator_struct)]),
    'L': ('', [])}),
  CSN1Ref(obj=iu_indicator),
  CSN1Ref(obj=system_information_21_indicator),
  CSN1Ref(obj=spare_padding)])

