#!/bin/bash python3

import subprocess, xlrd, platform, sys, os

spreadsheetIn = open("spreadsheet", "r")
spreadsheetOut = open("spreadsheetOut", "rw+")
log = open("log", "a")
os = ""
sheet_name = ""
invalidPairings = {}

def openWorkbook():
	global rows
	# try to open the spreadsheet
	try:
		xl_workbook = xlrd.open_workbook(spreadsheetIn)
	except FileNotFoundError:
		print("[!] Could not find " + spreadsheetIn + ", please check the file path and name")
		sys.exit(0)
	# try to open the sheet
	try:
		xl_sheet = xl_workbook.sheet_by_name(sheet_name)
	except xlrd.biffh.XLRDError:
		print("[!] Could not find sheet named 172.25.16.0.\r\nExiting...")
		sys.exit(0)
	rows = [[data.value for data in xl_sheet.row(n)] for n in range(2, xl_sheet.nrows)]
	return rows
#	for n in range(0, len(rows)):
#		del rows[n][2:]

def validatePairing(rows):
	ipHostname = []
	for row in rows:
		ipHostname.append()

def pingHost():
	pass

def updateSpreadsheet():
	pass

def logWrite():
	pass

if __name__ == "__main__":
	os = platform.system()

	validatePairing(openWorkbook())
