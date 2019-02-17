#!/usr/bin/python 
# -*- coding: utf-8 -*-
"""
###########################################
#   Tidak ada yang namanya  Recode, Edit, #
# Menjual kembali, atau ganti author di   #
# script kami !!!.                        #
###########################################
#           MAClook (MAC lookup)          #
###########################################
#         GAUSAH DI RECODE BOSS!!         #
#    TINGGAL PAKAI APA SUSAHNYA SIH???    #
#      Tolong Hargai sang Developer.      #
# DAN INGAT, BAHWA MENGEDIT SCRIPT ORANG  #
# LAIN TIDAK AKAN MEMBUATMU MENJADI PRO.  #
# BAHKAN KAMI ANGGAP ANDA NOOB!!!.        #
###########################################
#  Made By : Kemah (0wL) & DedSecTL       #
#  Team    : Surabaya Black Hat           #
#            BlackHole Security           #
#            Lead Cyber Team              #
#  Date    : 18-Feb-2019 (04:13)          #
#  Name    : MAC 1.1-dev                  #
###########################################
"""

from os import *
from urllib import *
from time import *
import sys
import json
import os

banner = """\033[1;34m
.___ ___,._______,._______,.__,              .__.
|   Y   ||   _   ||   _   ||  |.-----..-----.|  |--.
|       ||   1   ||   1___||  ||  _  ||  _  ||    <.
|\033[0m.\033[1;34m \_/  ||\033[0m.\033[1;34m  _   ||\033[0m.\033[1;34m  |___ |__||_____||_____||__|__|
|\033[0m:\033[1;34m  |   ||\033[0m:\033[1;34m  |   ||\033[0m:\033[1;34m  1   |\033[1;37m Author\033[1;30m :\033[1;37m Kemah (\033[1;32m0wL\033[1;37m)\033[1;34m
|\033[0m::.\033[1;34m|\033[0m:.\033[1;34m ||\033[0m::.\033[1;34m|\033[0m:.\033[1;34m ||\033[0m::.. .\033[1;34m |\033[1;37m Team\033[1;30m - \033[1;32m\033[104mSurabaya BlackHat\033[0m\033[1;34m
`--- ---'`--- ---'`-------'\033[1;30m      - \033[1;37m\033[100mBlackHole Security\033[0m
\033[1;37m    MAClook (\033[1;32mMAC Lookup\033[1;37m)\033[1;30m         - \033[1;37m\033[101mLead Cyber Team\033[0m
\033[1;37m        Version\033[1;32m 1.1\033[0m
=====================================================
"""
print banner
target = raw_input("Enter Your MAC Target :\033[1;32m ")
url1 = "https://api.macaddress.io/v1?apiKey=at_q7YvVhjh8ECTue4SqpgktUEe2O1rH&output=json&search="+target
url2 = "https://macvendors.co/api/"+target
dat1 = urlopen(url1).read().decode("utf-8")
dat2 = urlopen(url2).read().decode("utf-8")
data1 = json.loads(dat1)
data2 = json.loads(dat2)
print "\033[1;32m  [\033[1;37m#\033[1;32m]\033[1;37m Data Server 1 >>"
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mOUI\033[1;30m :\033[32m", str(data1["vendorDetails"]["oui"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mPrivate\033[1;30m :\033[32m", str(data1["vendorDetails"]["isPrivate"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mCompany Name\033[1;30m :\033[32m", str(data1["vendorDetails"]["companyName"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mCompany Address\033[1;30m :\033[32m", str(data1["vendorDetails"]["companyAddress"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mCountry Code\033[1;30m :\033[32m", str(data1["vendorDetails"]["countryCode"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mBlock Found\033[1;30m :\033[32m", str(data1["blockDetails"]["blockFound"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mBorder Left\033[1;30m :\033[32m", str(data1["blockDetails"]["borderLeft"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mBorder Right\033[1;30m :\033[32m", str(data1["blockDetails"]["borderRight"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mBlock Size\033[1;30m :\033[32m", str(data1["blockDetails"]["blockSize"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mBorder Left\033[1;30m :\033[32m", str(data1["blockDetails"]["borderLeft"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mAssignment\033[1;30m :\033[32m", str(data1["blockDetails"]["assignmentBlockSize"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mData Created\033[1;30m :\033[32m", str(data1["blockDetails"]["dateCreated"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mData Updated\033[1;30m :\033[32m", str(data1["blockDetails"]["dateUpdated"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mValid\033[1;30m :\033[32m", str(data1["macAddressDetails"]["isValid"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mVirtual Machine\033[1;30m :\033[32m", str(data1["macAddressDetails"]["virtualMachine"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mApplications\033[1;30m :\033[32m", str(data1["macAddressDetails"]["applications"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mApplications\033[1;30m :\033[32m", str(data1["macAddressDetails"]["applications"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mTransmission Type\033[1;30m :\033[32m", str(data1["macAddressDetails"]["transmissionType"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mAdministration Type\033[1;30m :\033[32m", str(data1["macAddressDetails"]["administrationType"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mWhireShark Note\033[1;30m :\033[32m", str(data1["macAddressDetails"]["wiresharkNotes"]);
print "\033[1;33m  [\033[1;32m+\033[1;33m]\033[1;37m MAC Prefix\033[1;30m :\033[1;32m", (data2['result']['mac_prefix']);
print "\033[1;33m  [\033[1;32m+\033[1;33m] \033[1;37mComment\033[1;30m :\033[32m", str(data1["macAddressDetails"]["comment"]);

print "\033[0m"
