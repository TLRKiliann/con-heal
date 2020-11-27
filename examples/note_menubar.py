#!/usr/bin/python3
# -*- coding: utf-8 -*-


#To destroy or call MenuBar :

	self.mBar = MenuBar(self)
	self.mBar.pack(side=TOP, fill=X, expand=YES)

	self.mBar.destroy()


#To update second page :

	self.master.destroy()
	Application.__init__(self)
	self.showPatients()