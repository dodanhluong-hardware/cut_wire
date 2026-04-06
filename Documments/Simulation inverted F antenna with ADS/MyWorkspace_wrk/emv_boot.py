# -*- coding: utf-8 -*-

import empro.toolkit.adv as adv

def main():
	path=r"C:/Users/DELL/MyWorkspace_wrk"
	lib=r"MyLibrary_lib"
	subst=r"MyLibrary_lib/substrate1.subst"
	substlib=r"MyLibrary_lib"
	substname=r"substrate1"
	cell=r"Version1"
	view=r"layout"
	libS3D=r"simulation/MyLibrary_lib/%Version1/_3%D%Viewer/proj_libS3D.xml"
	varDictionary={}
	exprDictionary={}
	adv.loadDesign(path=path, lib=lib, subst=subst, substlib=substlib, substname=substname, cell=cell, view=view, libS3D=libS3D, var_dict=varDictionary, expr_dict=exprDictionary)
