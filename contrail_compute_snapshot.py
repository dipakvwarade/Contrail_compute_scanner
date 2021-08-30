#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding=utf-8
__author__ = "Dipak Warade <dipakvwarade@gmail.com>"
__copyright__ = "Dipak Warade <dipakvwarade@gmail.com>"

import subprocess
import os
import sys
import requests
import time
import datetime
import logging
from logging.handlers import TimedRotatingFileHandler


def get_facts(cmd):
      mycmd = "/bin/contrail-vrouter-agent-cli read" + cmd
      fact = subprocess.check_output(mycmd, shell=True)
      return fact

def tell_me_your_name_compute(): 
  node_name = os.uname()[1]
  #print("\nINFO: Contrail Compute Snapshot : Working on node {}".format(node_name))
  return node_name 


if __name__ == '__main__':
  node_name = tell_me_your_name_compute()
  covered_commands = [ " kernel mpls list",
  " kernel nh list",
  " kernel qc list",
  " kernel route list",
  " kernel vrfassign list",
  " kernel vrfstats list",
  " kernel vxlan list",
  " ksync nexthop list",
  " oper acl list",
  " oper application policy set list",
  " oper fc list",
  " oper interface list",
  " oper mirror list",
  " oper mirror vn list",
  " oper mpls list",
  " oper nexthop list",
  " oper qc instances list",
  " oper route inet4 list",
  " oper route inet6 list",
  " oper route l2 list",
  " oper sg list",
  " oper unresolvednh list",
  " oper unresolvedroute list",
  " oper vm list",
  " oper vm list",
  " oper vn list",
  " oper vrf list",
  " oper vxlan config list",
  " oper vxlan list",
  " pkt flow stats list",
  " pkt flowtable info",
  " pkttrace info",
  " vmuuidvnuuid to vmiuuid list" ]

  file_name = "/tmp/"+node_name+"-contrail_snapshot.txt"
  logHandler = TimedRotatingFileHandler(file_name,when="M",interval=1, backupCount=10)
  logger = logging.getLogger( 'MyLogger' )
  logger.addHandler( logHandler )
  logger.setLevel( logging.INFO )

  for cmd in covered_commands:
    myfact = get_facts(cmd)
    print(myfact)
    logger.info(myfact)
