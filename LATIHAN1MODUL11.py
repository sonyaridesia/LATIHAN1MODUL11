#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:01:22 2022

@author: sonyaridesia
"""

class biodata():
    empCount = 0
    def init(self,nama,nim,angkatan):        
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
    
    def dis_input(self):
        self.nama = input("Masukan Nama anda:")
        self.nim = input("Masukan NIM anda: ")
        self.angkatan = input ("Angkatan: ")
        biodata.empCount +=1
        
    def dis_count(self):
        print("Jumlah Mahasiswa %d" % biodata.empCount)
 
    def dis_biodata(self):
        print ("Biodata anda: ")
        print ("Nama: ", self.nama)
        print ("NIM: ", self.nim)
        print ("Angkatan: ", self.angkatan)
        
datamhs = biodata()
datamhs.dis_input()
datamhs.dis_biodata()
print("Total Mahasiswa %d" % biodata.empCount)
